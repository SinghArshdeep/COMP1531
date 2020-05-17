from flask import render_template, request, redirect, url_for, abort
from server import app, system
from src.order import Order
from src.forms import *
from src.management_system import *

'''
Dedicated page for "page not found"
'''

@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404

'''
Home page route
'''

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('home.html')

'''
Order Pages
'''
@app.route('/order', methods=["GET", "POST"])
def order():

    if request.method == "POST":
        oid = request.form["order"]
        order = system.get_order(oid)

        if request.form["form"] == "pageForm":
            if request.form["submit_button"] == "creations":
                return render_template('creations.html', order=order, id = oid)

            elif request.form["submit_button"] == "sides":

                items = system.inventory.sides

                return render_template('sides.html', items = items, order=order, id = oid)

            elif request.form["submit_button"] == "drinks":

                items = system.inventory.drinks

                return render_template('drinks.html', order=order, id = oid, items = items)

            elif request.form["submit_button"] == "checkout":
                return render_template('payment.html', order=order, id = oid)

        elif request.form["form"] == "creation_type":
            if request.form["submit_button"] == "standard":
                standard = True
                items = system.standard_creations
                return render_template('creations.html', standard = standard, items = items, id = oid)
            elif request.form["submit_button"] == "custom":
                items = system.inventory.ingredients
                return render_template('creations.html', custom = True, items = items, id=oid)

        elif request.form["form"] == "standard_creation":
            items = system.standard_creations

            form = StandardCreationForm(request.form, system)

            # get errors with ingredients (check as normal ingredients)
            if len(form.errors) > 0:
                messages = ["The selected item is currently unavailable. Please select a different option"]
                return render_template('creations.html', messages=messages, items = items, id=oid, standard=True)
            # if no errors flash a 'Successfully added to order' message
            messages = ["Successfully added {} to order".format(form.creation.name)]
            order.add_creation(form.creation)
            system.remove_inventory_creation(form.creation)
            # if errors re-show page with error messages
            return render_template('creations.html', messages = messages, standard= True, items=items, id=oid)

        elif request.form["form"] == "custom_creation":
            # convert form into a form class??
            form = CustomOrderForm(request.form, system.inventory)
            items = system.inventory.ingredients

            # check for any errors
            if len(form.errors) > 0:
                messages = ["Errors in order. Please try again"]
                return render_template('creations.html', form = request.form, errors = form.errors, messages=messages, items = items, id=oid, custom=True)

            # if no errors add to order and include a 'Successfully added to order' message
            creation = form.create_creation()
            order.add_creation(creation)
            system.remove_inventory_creation(creation)
            messages = ["Successfully added Custom Creation to order"]
            return render_template('creations.html', messages=messages, items = items, id=oid)


        elif request.form["form"] == "add_sides":
            # convert to dictionary of sides and amounts
            form = CustomSidesForm(request.form, system.inventory)
            item = system.inventory.sides

            # check for errors
            if len(form.errors) > 0:
                messages = ["Errors in order. Please try again"]
                return render_template('sides.html', form = request.form, errors = form.errors, messages=messages, items = item, id = oid)

            # re-show page with errors /flash successful message
            sides = form.add_side(order)
            for s in sides:
                side = system.inventory.get_side(s)
                system.remove_inventory_item(side, int(sides[s]))

            messages = ["Successfully added the sides to the order"]
            return render_template('sides.html', messages=messages, items = item, id=oid)

        elif request.form["form"] == "add_drinks":
            # convert to dictionary of sides and amounts
            form = CustomDrinkForm(request.form, system.inventory)
            item = system.inventory.drinks

            # check for errors and displays them
            if len(form.errors) > 0:
                messages = ["Errors in order. Please try again"]
                return render_template('drinks.html', form = request.form, errors = form.errors, messages=messages, items = item, id = oid)

            # if no errors add to order and include a 'Successfully added to order' message
            drinks = form.add_drink(order)
            for d in drinks:
                drink = system.inventory.get_drink(d)
                system.remove_inventory_item(drink, int(drinks[d]))
            messages = ["Successfully added the drinks to the order"]
            return render_template('drinks.html', messages=messages, items = item, id=oid)

        elif request.form["form"] == "confirmation":
            if request.form["submit_button"] == "cancel":
                system.readd_to_inventory(order)
                system.remove_order(order)
                return render_template('home.html')
            system.confirm_order(order)
            return render_template('order_confirmation.html', pass_id=oid)
    else:
        order = system.add_order()

    return render_template('order.html', order=order, id=order.id)

'''
Status Pages
'''
@app.route('/order/status/', methods = ['GET', 'POST'])
def status():
    if request.method == 'POST':
        try:
            id=request.form['id']
            order = system.check_order_status(int(id))
            return render_template('order_status.html', id=id, order=order)
        except IDError:
            messages = ["Please enter a valid order ID"]
            return render_template('order_status.html', messages=messages)

    return render_template('order_status.html')

@app.route('/order/status/<id>', methods = ['GET', 'POST'])
def status_id(id):
    id = int(id)
    try:
        order = system.check_order_status(int(id))
        return render_template('order_status.html', id=id, order=order)
    except IDError:
        messages = ["Please enter a valid order ID"]
        return render_template('order_status.html', messages=messages)
    return render_template('order_status.html')


@app.route('/order/<id>')
def order_confirmation(id):
    return render_template('order_confirmation.html', pass_id=id)

'''
Staff Pages
'''

@app.route('/staff')
def staff():
    return render_template('staff.html')

@app.route('/staff/orders', methods = ['GET', 'POST'])
def curr_orders():
    if request.method == 'POST':
        value = int(request.form['update_status'])
        system.update_order_status(value)
        return render_template('view_orders.html', order_list=system.current_orders, y=len(system.current_orders))
    return render_template('view_orders.html', order_list=system.current_orders, y=len(system.current_orders))




#Page to redirect to show inventory or the update inventory pages
@app.route('/staff/inventory')
def inventory():
    return render_template('inventory.html')

#Shows the current stocks in the inventory
@app.route('/staff/inventory/view')
def view_inventory():
    return render_template('view_inventory.html', inventory = system.inventory)

#Updates the inventory and will redirect to the show inventory html page
@app.route('/staff/inventory/update', methods=["GET", "POST"])
def update_inventory():
    messages = None

    if request.method == "POST":
        form = UpdateInventory(request.form, system.inventory)
        # check for any errors
        if len(form.errors) > 0:
            messages = ["Errors in updating the inventory. Please try again"]
            #returns to update inventory html with errors to be displayed on the web page
            return render_template('update_inventory.html', inventory = system.inventory, form = request.form, errors = form.errors, messages=messages)
        #Shows the current stock if the inventory gets updated
        return render_template('view_inventory.html', inventory = system.inventory)


    return render_template('update_inventory.html', inventory = system.inventory)
