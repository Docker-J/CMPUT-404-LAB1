import requests

#print(requests.__version__)
#r = requests.get("http://www.google.com")
#print(r.status_code)

r = requests.get("https://raw.githubusercontent.com/Docker-J/CMPUT-404-LAB1/main/lab1.py")
print(r.text)
