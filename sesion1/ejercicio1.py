class ConfigManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.config = {}
        return cls._instance

    def set_config(self, key, value):
        self.config[key] = value

    def get_congif(self, key):
        return self.config.get(key, None)

    def get_all_config(self):
        return self.config

config1 = ConfigManager()
config2 = ConfigManager()
print(config1 is config2)  # Output: True

config1.set_config("database_url", "mysql://localhost:3306/mydb")
config1.set_config("debug", True)

print(config2.get_congif("database_url"))  # Output: mysql://localhost:3306/mydb
print(config2.get_congif("debug"))  # Output: True

print(config1.get_all_config())  # Output: {'database_url': 'mysql://localhost:3306/mydb', 'debug': True}