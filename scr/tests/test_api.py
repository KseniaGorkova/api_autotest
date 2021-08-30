import requests
from scr.pages.http_manager import HttpManager
import allure


@allure.testcase('Check ping')
# blocker critical normal minor trivial
def test_check_ping():
    with allure.step("Check ping"):
        result = HttpManager.get('https://restful-booker.herokuapp.com/ping')
        assert 201 == result.status_code

@allure.testcase('Check auth')
def test_check_auth():
    json_auth = {
        "username": "admin",
        "password": "password123"
    }
    result = HttpManager.post("https://restful-booker.herokuapp.com/auth",
                              json_auth)
    assert 200 == result.status_code
    json_right = "token"
    assert json_right in result.json()

@allure.testcase('Check get booking id')
def test_get_booking_id_all():
    result = HttpManager.get("https://restful-booker.herokuapp.com/booking")
    assert 200 == result.status_code
    json_right1 = [{'bookingid': 2},
                   {'bookingid': 6},
                   {'bookingid': 3},
                   {'bookingid': 7},
                   {'bookingid': 4},
                   {'bookingid': 1},
                   {'bookingid': 9},
                   {'bookingid': 8},
                   {'bookingid': 5},
                   {'bookingid': 10}]
    assert result.json() == json_right1

@allure.testcase('Check get booking id filter by name')
def test_get_booking_filter_by_name():
    result = HttpManager.get("https://restful-booker.herokuapp.com/booking?firstname=Sally")
    assert 200 == result.status_code
    json_right1 = [{'bookingid': 4}, {'bookingid': 6}]
    assert result.json() == json_right1

@allure.testcase('Check get booking check in')
def test_get_booking_checkin():
    result = HttpManager.get("https://restful-booker.herokuapp.com/booking?checkin=2014-03-13&checkout=2014-05-21")
    assert 200 == result.status_code
    json_right1 = []
    assert result.json() == json_right1

@allure.testcase('Check get booking read')
def test_get_booking_read():
    result = HttpManager.get("https://restful-booker.herokuapp.com/booking/5")
    assert 200 == result.status_code
    json_right1 = {'bookingdates': {'checkin': '2016-09-24', 'checkout': '2019-09-26'},
                   'depositpaid': False,
                   'firstname': 'Mary',
                   'lastname': 'Jackson',
                   'totalprice': 282}
    assert result.json() == json_right1

@allure.testcase('Check create booking')
def test_create_booking():
    json_name = {
        "firstname": "J3im",
        "lastname": "B2rown",
        "totalprice": 1111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2021-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    result = HttpManager.post("https://restful-booker.herokuapp.com/booking",
                              json_name)
    assert 200 == result.status_code
    json_right = "bookingid"
    assert json_right in result.json()

@allure.testcase('Check update booking')
def test_update_booking():
    json_auth = {
        "username": "admin",
        "password": "password123"
    }
    result = HttpManager.post("https://restful-booker.herokuapp.com/auth",
                              json_auth)
    assert 200 == result.status_code
    json_right = result.json()['token']
    json_name = {
        "firstname": "Alise",
        "lastname": "Mari",
        "totalprice": 10,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2021-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    result = requests.put("https://restful-booker.herokuapp.com/booking/5", json=json_name,
                          cookies={'token': json_right})
    assert 200 == result.status_code


@allure.testcase('Check partial update booking')
def test_partial_update():
    json_auth = {
        "username": "admin",
        "password": "password123"
    }
    result = HttpManager.post("https://restful-booker.herokuapp.com/auth",
                              json_auth)
    assert 200 == result.status_code
    json_right = result.json()['token']
    json_name = {
        "firstname": "fdge",
        "lastname": "Mari"
    }
    result = requests.patch("https://restful-booker.herokuapp.com/booking/5", json=json_name,
                            cookies={'token': json_right})
    assert 200 == result.status_code

@allure.testcase('Check delete')
def test_delete():
    json_auth = {
        "username": "admin",
        "password": "password123"
    }
    result = HttpManager.post("https://restful-booker.herokuapp.com/auth",
                              json_auth)
    assert 200 == result.status_code
    json_right = result.json()['token']
    result = requests.delete("https://restful-booker.herokuapp.com/booking/5",
                             cookies={'token': json_right})
    assert 201 == result.status_code
