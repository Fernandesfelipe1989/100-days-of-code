from decouple import config


class InternetSpeedTwitterBot:
    CHROME_DRIVER_PATH = config("CHROME_DRIVER_PATH")
    TWITTER_EMAIL = config('TWITTER_EMAIL')
    TWITTER_PASSWORD = config("TWITTER_PASSWORD")

    def __int__(self):
        pass
