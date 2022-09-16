import os

from dotenv import load_dotenv

load_dotenv()


def get_config_variable(variable_name):
    value = os.getenv(variable_name)
    if variable_name == 'api_key':
        if value is None:
            raise Exception("api_key must not be null")
    else:
        return value
