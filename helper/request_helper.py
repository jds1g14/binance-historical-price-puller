import math

from binance import helpers

import helper.config_helper

binance_interval = helper.config_helper.get_config_variable("binance_interval")
start_date = helper.config_helper.get_config_variable("start_date")
end_date = helper.config_helper.get_config_variable("end_date")
binance_limit = helper.config_helper.get_config_variable("limit")

step_size_milliseconds = helpers.interval_to_milliseconds(binance_interval)


def create_kline_request(currency_pairing, interval, start_date, limit=1000):
    return {'symbol': currency_pairing,
            'interval': interval,
            'startTime': start_date,
            'limit': limit
            }


def get_no_api_request_required():
    start_timestamp = helpers.date_to_milliseconds(start_date)
    end_timestamp = helpers.date_to_milliseconds(end_date)
    milliseconds_delta = end_timestamp - start_timestamp
    no_klines_required = int(milliseconds_delta / step_size_milliseconds)
    no_api_requests_required = math.ceil(no_klines_required / int(binance_limit))

    return no_api_requests_required


def get_api_request_start_time(klines_response):
    last_kline = klines_response[len(klines_response) - 1]
    last_timestamp = last_kline[0]
    return last_timestamp + step_size_milliseconds
