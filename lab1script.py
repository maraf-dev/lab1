
import requests
#print("Version of Requests Library:  " + requests.__version__)
resp = requests.get("https://raw.githubusercontent.com/maraf-dev/lab1/main/lab1script.py")
print(resp.text)
