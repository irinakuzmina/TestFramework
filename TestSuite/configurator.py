class Configurator:
    def __init__(self, environment):
        with open('config.json') as f:
            self.config = eval(f.read())
        self.config = self.config[environment]
        # print(self.config)

    def get_database_url(self):
        return self.config['database']

    def get_test_data_folder(self):
        return self.config['test_data_folder']
