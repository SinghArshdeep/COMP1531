from flask import render_template, request, redirect, url_for, abort
from server import app, system
from datetime import datetime
from src.location import Location
# from src.error import BookingError, LoginError
from src.customer import Customer


'''
Dedicated page for "page not found"
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404



'''
Search for Cars
'''
@app.route('/', methods=["GET", "POST"])
def cars():

    if request.method == 'POST':
        make  = request.form.get('make')
        model = request.form.get('model')

        if make == '':
            make = None

        if model == '':
            model = None

        cars = system.search_car(make, model)
        return render_template('cars.html', cars = cars)
    
    return render_template('cars.html', cars = system.cars)




'''
Display car details for the car with given rego
'''
@app.route('/cars/<rego>')
def car(rego):
    car = system.get_car(rego)

    if not car:
        abort(404)

    return render_template('car_details.html', car=car)


'''
Make a booking for a car with given rego
'''
from src.forms import BookingForm
@app.route('/cars/book/<rego>', methods=["GET", "POST"])
def book(rego):
    car = system.get_car(rego)
    error = {}
    error['name'] = ''
    error['licence'] = ''
    error['date1'] = ''
    error['date2'] = ''
    error['loc1'] = ''
    error['loc2'] = ''
    error['period'] = ''
    
    values = {}
    values['name'] = ''
    values['licence'] = ''
    values['date1'] = ''
    values['date2'] = ''
    values['loc1'] = ''
    values['loc2'] = ''
    values['fee'] = ''

    if not car:
        abort(404)
    
    if request.method == 'POST':
        
        form = BookingForm(request.form)
        form._parse(request.form)
        values['name'] = form.customer_name
        values['licence'] = form.customer_licence
        values['loc1'] = form.start_location
        values['loc2'] = form.end_location
        values['date1'] = request.form["start_date"]
        values['date2'] = request.form["end_date"]
        
        
        if form.is_valid == False:
            error['name'] = form.get_error('customer_name')
            error['licence'] = form.get_error('customer_licence')
            error['date1'] = form.get_error('start_date')
            error['date2'] = form.get_error('end_date')
            error['loc1'] = form.get_error('start_location')
            error['loc2'] = form.get_error('end_location')
            error['period'] = form.get_error('period')
        
            return render_template('booking_form.html', car=car, error = error, values = values)
        
        if 'check' in request.form:
            values['fee'] =  system.check_fee(car, form.start_date, form.end_date)
            return render_template('booking_form.html', car=car, error = error, values = values)
        
        elif 'confirm' in request.form:
            name = form.customer_name
            license = form.customer_licence
            customer = Customer(name, license)

            date1 = form.start_date
            date2 = form.end_date

            loc1 = form.start_location
            loc2 = form.end_location
            nbooking = system.make_booking(customer, car, date1, date2, loc1, loc2)
            
        
            return render_template('booking_confirm.html', booking = nbooking)


        '''
        IMPLEMENT THIS SECTION
        '''
        
        # 1. If form is not valid, then display appropriate error messages


        # 2. If the user has pressed the 'check' button, then display the fee


        # 3. Otherwise, if the user has pressed the 'confirm' button, then 
        #   make the booking and display the confirmation page


    return render_template('booking_form.html', car=car, error = error, values = values)



'''
Display list of all bookings for the car with given 'rego'
'''
@app.route('/cars/bookings/<rego>')
def car_bookings(rego):
    return render_template('bookings.html', bookings=system.get_bookings_by_car_rego(rego))




