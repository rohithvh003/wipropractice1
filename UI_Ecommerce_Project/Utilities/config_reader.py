import configparser
import os


class ConfigReader:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CONFIG_PATH = os.path.join(BASE_DIR, "config.ini")

    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)

    @staticmethod
    def get_base_url():
        return ConfigReader.config.get("environment", "base_url")

    @staticmethod
    def get_browser():
        return ConfigReader.config.get("environment", "browser", fallback="chrome")

    @staticmethod
    def get_implicit_wait():
        return ConfigReader.config.getint("environment", "implicit_wait", fallback=10)

    @staticmethod
    def get_test_data_path():
        return os.path.join(ConfigReader.BASE_DIR, "data", "user_data.csv")