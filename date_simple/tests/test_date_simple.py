import date_simple as ds
import datetime
import pytest

def test_get_date_object_no_arg():
    today = ds.get_date_object()
    assert isinstance(today, datetime.date)
    assert today == datetime.date.today()

def test_get_date_object_arg():
    date = ds.get_date_object('2016-02-26')
    assert date == datetime.date(2016,2,26)

def test_get_date_string_no_arg():
    today = ds.get_date_string()
    assert today == str(datetime.date.today().strftime('%m/%d/%Y'))

def test_get_date_string_arg():
    date = ds.get_date_string(datetime.date(2016,2,26))
    assert date == str(datetime.date(2016,2,26).strftime('%m/%d/%Y'))

def test_get_date_object_value_error():
    with pytest.raises(ValueError):
        ds.get_date_object('02/37/1998')

def test_get_date_object_type_error():
    with pytest.raises(TypeError):
        ds.get_date_object(datetime.date(2016,2,26))

def test_get_date_string_value_error():
    with pytest.raises(ValueError):
        ds.get_date_string(datetime.date(2016,37,26))

