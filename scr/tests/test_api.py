import requests
from scr.pages.http_manager import HttpManager
import allure
from scr.pages.json import Json


@allure.testcase('Check ping')
# blocker critical normal minor trivial
def test_check_ping():
    with allure.step("Check ping"):
        result = HttpManager.get('https://restful-booker.herokuapp.com/ping')
        assert 201 == result.status_code

@allure.testcase('Check auth')
def test_check_auth():
    result = HttpManager.post("https://restful-booker.herokuapp.com/auth",
                              Json.json_auth)
    assert 200 == result.status_code
    json_right = "token"
    assert json_right in result.json()

@allure.testcase('Check get booking id')
def test_get_booking_id_all():
    result = HttpManager.get("https://restful-booker.herokuapp.com/booking")
    assert 200 == result.status_code
    assert result.json() == Json.json_get_booking_id_all

@allure.testcase('Check get booking id filter by name')
def test_get_booking_filter_by_name():
    result = HttpManager.get("https://restful-booker.herokuapp.com/booking?firstname=Sally")
    assert 200 == result.status_code
    assert result.json() == Json.json_get_booking_filter_by_name

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
    assert result.json() == Json.json_get_booking_read

@allure.testcase('Check create booking')
def test_create_booking():
    result = HttpManager.post("https://restful-booker.herokuapp.com/booking",
                              Json.json_create_booking)
    assert 200 == result.status_code
    json_right = "bookingid"
    assert json_right in result.json()

@allure.testcase('Check update booking')
def test_update_booking():
    result = HttpManager.post("https://restful-booker.herokuapp.com/auth",
                              Json.json_auth)
    assert 200 == result.status_code
    json_right = result.json()['token']
    result = requests.put("https://restful-booker.herokuapp.com/booking/5", json=Json.json_update_booking,
                          cookies={'token': json_right})
    assert 200 == result.status_code


@allure.testcase('Check partial update booking')
def test_partial_update():
    result = HttpManager.post("https://restful-booker.herokuapp.com/auth",
                              Json.json_auth)
    assert 200 == result.status_code
    json_right = result.json()['token']
    result = requests.patch("https://restful-booker.herokuapp.com/booking/5", json=Json.json_partial_update,
                            cookies={'token': json_right})
    assert 200 == result.status_code

@allure.testcase('Check delete')
def test_delete():
    result = HttpManager.post("https://restful-booker.herokuapp.com/auth",
                              Json.json_auth)
    assert 200 == result.status_code
    json_right = result.json()['token']
    result = requests.delete("https://restful-booker.herokuapp.com/booking/5",
                             cookies={'token': json_right})
    assert 201 == result.status_code
    
