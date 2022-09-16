import csv
from datetime import datetime

from helper import config_helper

pairing = config_helper.get_config_variable("currency_pairing")
current_date_time = datetime.today()
csv_name = pairing + "-historical-prices-" + str(current_date_time)
header = ["timestamp", "high_price", "low_price"]


def generate_file():
    with open(csv_name, 'x', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)


def append_klines_to_csv(list_of_klines):
    with open(csv_name, 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for kline in list_of_klines:
            data = [kline.date_time, kline.high_price, kline.low_price]
            writer.writerow(data)
