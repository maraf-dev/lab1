
import requests
#print("Version of Requests Library:  " + requests.__version__)
resp = requests.get("http://google.com")
print(resp.text)
