from binance import Client

from helper import config_helper, request_helper

api_key = config_helper.get_config_variable("api_key")
currency_pairing = config_helper.get_config_variable("currency_pairing")
interval = config_helper.get_config_variable("binance_interval")
limit = config_helper.get_config_variable("limit")


def retrieve_klines(start_timestamp):
    request_params = request_helper.create_kline_request(currency_pairing, interval, start_timestamp, limit)
    client = Client(api_key=api_key)
    return list(client.get_klines(**request_params))
