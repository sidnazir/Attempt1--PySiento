import requests
import requests.exceptions


class RestClient:

    def __init__(self, url):
        self.url = url

    def post(self, post_data):
        try:
            response = requests.post(self.url, data=post_data)
            print("Server Output Received :")
            print(response)
            print("\n\n")
        except requests.exceptions.Timeout:
            print("ERROR : Timeout trying to post to " + self.url)
            raise
        except requests.exceptions.ConnectionError:
            print("ERROR : Error in connection to " + self.url)
        except requests.exceptions.InvalidURL:
            print("ERROR : The URL was invalid : " + self.url)
            raise
        except:
            print("ERROR : Unknown error")
            raise

    def get(self):
        try:
            response = requests.get(self.url)
            print("Server Output Received :")
            print(response)
            print("\n\n")
        except requests.exceptions.Timeout:
            print("ERROR : Timeout trying to get from " + self.url)
            raise
        except requests.exceptions.ConnectionError:
            print("ERROR : Error in connection to " + self.url)
        except requests.exceptions.InvalidURL:
            print("ERROR : The URL was invalid : " + self.url)
            raise
        except:
            print("ERROR : Unknown error")
            raise
