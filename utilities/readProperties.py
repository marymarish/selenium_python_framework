import configparser
config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        # get info from config.ini:
        url = config.get('common info', 'baseURL')
        return url

    # def getSearchURL():
    #     login_url = config.get('common info', 'searchURL')
    #     return login_url

    @staticmethod
    def getUserName():
        # get info from config.ini:
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        # get info from config.ini:
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getExpectedTitleHome():
        expected_title = config.get('common info', 'home_page_expected_title')
        return expected_title

    # @staticmethod
    def getExpectedTitleSearch():
        expected_title = config.get('common info', 'search_page_expected_title')
        return expected_title