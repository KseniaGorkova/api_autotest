class Json:
    json_auth = {
        "username": "admin",
        "password": "password123"
    }

    json_get_booking_id_all = [{'bookingid': 2},
                               {'bookingid': 6},
                               {'bookingid': 3},
                               {'bookingid': 7},
                               {'bookingid': 4},
                               {'bookingid': 1},
                               {'bookingid': 9},
                               {'bookingid': 8},
                               {'bookingid': 5},
                               {'bookingid': 10}]

    json_get_booking_filter_by_name = [{'bookingid': 4}, {'bookingid': 6}]

    json_get_booking_read = {'bookingdates': {'checkin': '2016-09-24', 'checkout': '2019-09-26'},
                             'depositpaid': False,
                             'firstname': 'Mary',
                             'lastname': 'Jackson',
                             'totalprice': 282}

    json_create_booking = {
        "firstname": "J3im",
        "lastname": "B2rown",
        "totalprice": 1111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2021-01-01",
            "checkout": "2019-01-01"
        }
    }

    json_update_booking = {{
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
    }

    json_partial_update = {
        "firstname": "fdge",
        "lastname": "Mari"
    }

