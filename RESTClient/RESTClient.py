import requests
import requests.exceptions


class RestClient:
    @staticmethod
    def post(post_url, post_data):
        try:
            response = requests.post(post_url, data=post_data)
            print("Server Output Received :")
            print(response)
            print("\n\n")
        except requests.exceptions.Timeout:
            print("ERROR : Timeout trying to post to " + post_url)
            raise
        except requests.exceptions.ConnectionError:
            print("ERROR : Error in connection to " + post_url)
        except requests.exceptions.InvalidURL:
            print("ERROR : The URL was invalid : " + post_url)
            raise
        except:
            print("ERROR : Unknown error")
            raise

    @staticmethod
    def get(get_url):
        try:
            response = requests.get(get_url)
            print("Server Output Received :")
            print(response)
            print("\n\n")
        except requests.exceptions.Timeout:
            print("ERROR : Timeout trying to get from " + get_url)
            raise
        except requests.exceptions.ConnectionError:
            print("ERROR : Error in connection to " + get_url)
        except requests.exceptions.InvalidURL:
            print("ERROR : The URL was invalid : " + get_url)
            raise
        except:
            print("ERROR : Unknown error")
            raise
