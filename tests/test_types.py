
import pytest
import datetime


from dtguess import types


def test_cell_type():

    c = types.CellType()
    assert isinstance(c, types.CellType)

    c.result_type = str
    assert c.test("cell") == True

    c.result_type = unicode
    assert c.test(u"cell") == True

    c.result_type = int
    assert c.test(123) == True

def test_cell_type_cast():

    assert types.CellType().cast('test') == 'test'
    assert types.CellType().cast(12345) == 12345
    assert types.CellType().cast(None) == None


def test_string_type():

    s = types.StringType()
    assert isinstance(s, types.StringType)

    assert s.cast(1) == "1"
    assert s.cast(True) == "True"
    assert s.cast('abc') == "abc"

    assert s.cast(None) != "None"


def test_string_type_test():

    s = types.StringType()
    assert s.test(5) == True
    assert s.test('5') == True
    assert s.test(True) == True
    assert s.test(None) == True


def test_integer_type():

    i = types.IntegerType()
    assert isinstance(i, types.IntegerType)

    assert i.cast(None) == None
    assert i.cast('') == None
    assert i.cast(5) == 5
    assert i.cast(-5) == -5
    assert i.cast('5') == 5
    assert i.cast('005') == 5
    assert i.cast(' 5 ') == 5
    assert i.cast('5.00') == 5

    with pytest.raises(ValueError):
        assert i.cast('5.01') == 5


def test_decimal_type():

    d = types.DecimalType()
    assert isinstance(d, types.DecimalType)

    assert d.cast(None) == None
    assert d.cast('') == None
    assert d.cast('0') == 0
    assert d.cast(10) == 10
    assert d.cast(10) == 10
    assert d.cast('10') == 10
    assert d.cast('10.0') == 10
    assert d.cast(' 10.00') == 10
    assert d.cast(10.5) == 10.5
    assert d.cast('10.5') == 10.5
    assert d.cast(.5) == 0.5
    assert d.cast('.5') == 0.5
    assert d.cast(-1) == -1
    assert d.cast('-1') == -1

    with pytest.raises(ValueError):
        assert d.cast(',5') == None


def test_boolean_type():

    b = types.BooleanType()
    assert isinstance(b, types.BooleanType)

    assert b.cast(False) == False
    assert b.cast(True) == True
    assert b.cast('') == None
    assert b.cast(' ') == None
    assert b.cast('0') == False
    assert b.cast('1') == True
    assert b.cast('  0') == False
    assert b.cast('  1') == True
    assert b.cast('F') == False
    assert b.cast('T') == True

    with pytest.raises(ValueError):
        assert b.cast('Fault') == False


def test_boolean_custom_type():

    b = types.BooleanType(true_values=('yes',), false_values=('no',))
    assert isinstance(b, types.BooleanType)

    assert b.cast('No') == False
    assert b.cast('Yes') == True


def test_date_type_none_format():

    d = types.DateType(None)
    assert isinstance(d, types.DateType)
    assert d.cast('2016-01-01') == '2016-01-01'


def test_date_type():

    d = types.DateType('%Y-%m-%d %H:%M:%S')
    assert isinstance(d, types.DateType)

    assert d.cast(None) == None
    assert d.cast('') == None

    now = datetime.datetime.now()
    assert d.cast(now) == now

    assert str(d) == "Date(%Y-%m-%d %H:%M:%S)"
    assert hash(types.DateType('%Y')) == hash(types.DateType('%Y'))



def test_date_type_sets_instances():

    di = types.DateTypeSets.instances()
    for i in di:
        assert isinstance(i, types.DateType)


def test_date_type_test():

    d = types.DateType('%Y-%m-%d')
    assert d.test('2016-01-01') == True
    assert d.test('Fail') == False


def test_date_type_compare():

    d1 = types.DateType('%Y-%m-%d %H')
    d2 = types.DateType('%Y-%m-%d %H')
    assert d1 == d2

    d1 = types.DateType('%Y-%m-%d %H')
    d2 = types.DateType('%Y-%m-%d %I')
    assert d1 != d2


def test_date_util_type():

    du = types.DateUtilType()
    assert isinstance(du, types.DateUtilType)

    assert du.cast('') == None
    assert du.cast(None) == None
    assert str(du.cast('2016-01-01')) == '2016-01-01 00:00:00'
    assert str(du.cast('2016-01-01 01:02:03')) == '2016-01-01 01:02:03'


def test_date_util_type_test():

    du = types.DateUtilType()
    assert du.test('2016-01-01') == True
    assert du.test('Fail') == False
    assert du.test("2") == False
