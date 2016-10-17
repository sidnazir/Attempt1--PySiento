""" RestClient Document
    for the project.
"""
import requests
import requests.exceptions


class RestClient:
    """RestClient class to communicate with the Server."""
    def __init__(self, url):
        """Constructor defined"""
        self.url = url

    def post(self, post_data):
        """Post method"""
        try:
            response = requests.post(self.url, data=post_data)
            """Communication established with Server"""
            print("Server Output Received :")
            print(response)
            print("\n\n")
        except requests.exceptions.Timeout:
            """Connection failed due to timeout"""
            print("ERROR : Timeout trying to post to " + self.url)
            raise
        except requests.exceptions.ConnectionError:
            print("ERROR : Error in connection to " + self.url)
        except requests.exceptions.InvalidURL:
            print("ERROR : The URL was invalid : " + self.url)
            raise
        except:
            """Error occured"""
            print("ERROR : Unknown error")
            raise

    def get(self):
        """Get method"""
        try:
            response = requests.get(self.url)
            """Serve output received"""
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
            """Error occured and no connection"""
            print("ERROR : Unknown error")
            raise
