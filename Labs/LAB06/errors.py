from datetime import datetime

class BookingError(Exception):
    def __init__(self, name, message):
        self.name = name
        self.message = message
    
    def __str__(self):
        return self.name + ': ' + self.message
    
    '''
    To be completed
    '''
def check_booking_error(start_date, end_date, start_location, end_location):
    errors = {}
    
    if not isinstance(start_location, str) or not isinstance(end_location, str):
        raise BookingError('Invalid Location', 'Please enter valid name for the location ')
    
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise BookingError('Invalid Date', "Incorrect data format, should be YYYY-MM-DD")

    d1 = datetime.strptime(start_date, "%Y-%m-%d")
    d2 = datetime.strptime(end_date, "%Y-%m-%d")
    period = (d2 - d1).days

    if period < 0:
        raise BookingError('Invalid Period', "Specify a valid booking period")

    return errors


