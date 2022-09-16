import datetime

from binance import Client, helpers

import helper.request_helper
from api import binance_call
from files import csv_generator
from helper import config_helper, request_helper
from mapper import klines_mapper


def main():
    no_api_requests_required = request_helper.get_no_api_request_required()
    current_api_request_no = 1
    start_date = config_helper.get_config_variable("start_date")
    current_timestamp = helpers.date_to_milliseconds(start_date)

    while current_api_request_no <= no_api_requests_required:
        klines_response = binance_call.retrieve_klines(current_timestamp)

        klines_list = []
        for resp_element in klines_response:
            kline = klines_mapper.map_kline_response_to_object(resp_element)
            klines_list.append(kline)

        if current_api_request_no == 1:
            csv_generator.generate_file()

        csv_generator.append_klines_to_csv(klines_list)

        if len(klines_response) != 0:
            current_timestamp = helper.request_helper.get_api_request_start_time(klines_response)

        current_api_request_no += 1


if __name__ == '__main__':
    main()
