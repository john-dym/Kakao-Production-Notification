"""
Kakao Production Notification
By: John Morales

Python 3.7.4

Status: Not Finished

Program parses a text file of an output from a production status screen and will notify users of any changes and can
relay production schedule when requested via Kakao Talk.

"""

# Third-party libraries
import requests

params = dict(client_id=API_KEY, redirect_uri="", response_type="")
test = requests.get("https://kauth.kakao.com/oauth/authorize", params)

def schedule_comparison():
    prod_list_from_txt()
    pass

# Reads "production.txt" and returns as a nested list
def prod_list_from_txt():
    processed_list = []
    with open("production.txt") as f:
        prod_list = f.read()
    prod_list = prod_list.rsplit("\n")
    for element in prod_list:
        processed_list += [element.rsplit(", ")]
    return processed_list

def main():
    pass

if __name__ == "__main__":
    main()
