from model.Kline import Kline


def map_kline_response_to_object(kline_response_element):
    kline = Kline()
    kline.date_time = kline_response_element[0]
    kline.low_price = kline_response_element[3]
    kline.high_price = kline_response_element[2]

    return kline
