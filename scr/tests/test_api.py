import requests
from scr.pages.http_manager import HttpManager
import allure
from scr.pages.json import Json

@allure.testcase('Check ping')
def test_check_ping():
    with allure.step("Send request GET /ping"):
        result = HttpManager.get('https://restful-booker.herokuapp.com/ping')

    with allure.step("Check 201 status code"):
        assert 201 == result.status_code, f' 201 != {result.status_code}'

@allure.testcase('Check auth')
def test_check_auth():
    with allure.step("Send request POST /auth"):
        result = HttpManager.post("https://restful-booker.herokuapp.com/auth",
                              Json.json_auth)

    with allure.step("Check 200 status code"):
        assert 200 == result.status_code, f' 200 != {result.status_code}'

    with allure.step("Сheck response body"):
        json_right = "token"
        assert json_right in result.json(), f"{result.json()} != {json_right}"

@allure.testcase('Check get booking id')
def test_get_booking_id_all():
    with allure.step("Send request GET /booking"):
        result = HttpManager.get("https://restful-booker.herokuapp.com/booking")

    with allure.step("Check 200 status code"):
        assert 200 == result.status_code, f' 200 != {result.status_code}'

    with allure.step("Сheck response body"):
        assert result.json() == Json.json_get_booking_id_all, f"{result.json()} != {Json.json_get_booking_id_all}"

@allure.testcase('Check get booking id filter by name')
def test_get_booking_filter_by_name():
    with allure.step("Send request GET /booking?filtername"):
        result = HttpManager.get("https://restful-booker.herokuapp.com/booking?firstname=Sally")

    with allure.step("Check 200 status code"):
        assert 200 == result.status_code, f' 200 != {result.status_code}'

    with allure.step("Сheck response body"):
        assert result.json() == Json.json_get_booking_filter_by_name, f"{result.json()} != {Json.json_get_booking_filter_by_name}"

@allure.testcase('Check get booking check in')
def test_get_booking_checkin():
    with allure.step("Send request GET /booking?checkin"):
        result = HttpManager.get("https://restful-booker.herokuapp.com/booking?checkin=2014-03-13&checkout=2014-05-21")

    with allure.step("Check 200 status code"):
        assert 200 == result.status_code, f' 200 != {result.status_code}'

    with allure.step("Сheck response body"):
        json_right1 = []
        assert result.json() == json_right1, f"{result.json()} != {json_right1}"

@allure.testcase('Check get booking read')
def test_get_booking_read():
    with allure.step("Send request GET /booking/number"):
        result = HttpManager.get("https://restful-booker.herokuapp.com/booking/5")

    with allure.step("Check 200 status code"):
        assert 200 == result.status_code, f' 200 != {result.status_code}'

    with allure.step("Сheck response body"):
        assert result.json() == Json.json_get_booking_read, f"{result.json()} != {Json.json_get_booking_read}"

@allure.testcase('Check create booking')
def test_create_booking():
    with allure.step("Send request POST /booking"):
        result = HttpManager.post("https://restful-booker.herokuapp.com/booking",
                              Json.json_create_booking)

    with allure.step("Check 200 status code"):
        assert 200 == result.status_code,f' 200 != {result.status_code}'

    with allure.step("Сheck response body"):
        json_right = "bookingid"
        assert json_right in result.json(), f"{json_right} not in {result.json()}"

@allure.testcase('Check update booking')
def test_update_booking():
    with allure.step("Send request POST /auth"):
        result = HttpManager.post("https://restful-booker.herokuapp.com/auth",
                              Json.json_auth)

    with allure.step("Check 200 status code"):
        assert 200 == result.status_code, f' 200 != {result.status_code}'

    with allure.step("Сheck response body"):
        json_right = result.json()['token']
        result = requests.put("https://restful-booker.herokuapp.com/booking/5", json=Json.json_update_booking,
                              cookies={'token': json_right})
        assert 200 == result.status_code, f' 200 != {result.status_code}'


@allure.testcase('Check partial update booking')
def test_partial_update():
    with allure.step("Send request POST /auth"):
        result = HttpManager.post("https://restful-booker.herokuapp.com/auth",
                              Json.json_auth)

    with allure.step("Check 200 status code"):
        assert 200 == result.status_code, f'200 != {result.status_code}'

    with allure.step("Сheck response body"):
        json_right = result.json()['token'], f'{json_right} not in {result.json()}'

    with allure.step("Send request PATH /booking/number"):
        result = requests.patch("https://restful-booker.herokuapp.com/booking/5", json=Json.json_partial_update,
                            cookies={'token': json_right})

    with allure.step("Check 200 status code"):
        assert 200 == result.status_code, f' 200 != {result.status_code}'

@allure.testcase('Check delete')
def test_delete():
    with allure.step("Send request POST /auth"):
        result = HttpManager.post("https://restful-booker.herokuapp.com/auth",
                              Json.json_auth)

    with allure.step("Check 200 status code"):
        assert 200 == result.status_code, f' 200 != {result.status_code}'

    with allure.step("Сheck response body"):
        json_right = result.json()['token'], f' {json_right} not in {result.json()}'

    with allure.step("Send request DELETE /booking/number"):
        result = requests.delete("https://restful-booker.herokuapp.com/booking/5",
                             cookies={'token': json_right})

    with allure.step("Check 201 status code"):
        assert 201 == result.status_code, f' 201 != {result.status_code}'
    
