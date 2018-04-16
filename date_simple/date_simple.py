
"""date_simple.py --  produce a module, build into a package and write tests for it"""

import datetime


def get_date_object(date=None):
    """ takes an optional string date and returns a date object """
    if date:
        d1 = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        print(d1)
    else:
        d1 = datetime.date.today()
        print(d1)
    return d1

def get_date_string(date_object=None):
    """ takes an optional date object and returns a formatted string """
    if date_object:
        datestr = date_object.strftime('%Y-%m-%d')
    else:
        datestr = datetime.date.today().strftime('%Y-%m-%d')
    return datestr

def get_date_string(date_object=None, format='MM/DD/YYYY'):
    """ takes an optional date object and returns a formatted string """
    if date_object:
        if format == 'DD-Mon-YY':
            datestr = date_object.strftime('%d-%b-%y')
        elif format == 'YYYY-MM-DD':
            datestr = date_object.strftime('%Y-%m-%d')
        else:
            datestr = date_object.strftime('%m/%d/%Y')
    else:
        if format == 'DD-Mon-YY':
            datestr = datetime.date.today().strftime('%d-%b-%y')
        elif format == 'YYYY-MM-DD':
            datestr = datetime.date.today().strftime('%Y-%m-%d')
        else:
            datestr = datetime.date.today().strftime('%m/%d/%Y')
    return datestr

def main():
    dateobj1 = get_date_object()
    dateobj2 = get_date_object(date='2018-02-26')
    datestr = get_date_string()
    datestr = get_date_string(date_object=dateobj2)
    datestr = get_date_string(date_object=dateobj2, format='MM/DD/YYYY')
    datestr = get_date_string(date_object=dateobj2, format='DD-Mon-YY')

if __name__ == '__main__':
    main()

