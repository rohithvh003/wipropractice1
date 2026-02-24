import configparser
import os


class ConfigReader:

    config = configparser.ConfigParser()

    # Absolute path to config.ini
    config_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "config",
        "config.ini"
    )

    config.read(config_path)

    @classmethod
    def get_base_url(cls):
        return cls.config.get("DEFAULT", "base_url")

    @classmethod
    def get_browser(cls):
        return cls.config.get("DEFAULT", "browser")

    @classmethod
    def get_implicit_wait(cls):
        return cls.config.getint("DEFAULT", "implicit_wait")

    @classmethod
    def get_explicit_wait(cls):
        return cls.config.getint("DEFAULT", "explicit_wait")

    @classmethod
    def get_test_data_path(cls):
        """
        Builds absolute path to data/users.csv
        based on:
        Project/Pytest/data/users.csv
        """
        relative_path = cls.config.get("DEFAULT", "test_data_path")

        # Go up 1 level from config/ → Pytest/
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        return os.path.join(base_dir, relative_path)

    @classmethod
    def get_customer_info_url(cls):
        return cls.config.get("DEFAULT", "customer_info_url")