import requests  # εισαγωγή της βιβλιοθήκης
import datetime

url = input("insert url: ")  # προσδιορισμός του url

#Headers
with requests.get(url) as response:
    headers = response.headers
    print("Response Headers:\n", headers, "\n")

#Server
if "Server" in headers:
    print("Server:",headers["Server"],"\n")
else:
    print("No Server\n")

#Cookies   
if "Set-Cookie" in headers:
    cookies=response.cookies
    print("Cookies:\n")
    i=1
    for cookie in cookies:
        print(i,".")
        print("Name:",cookie.name)
        if cookie.expires is not None:
            print("Expires:",datetime.datetime.fromtimestamp(float(cookie.expires)),"\n")
        else:
            print("Does not expire\n")
        i=i+1
else:
    print("No Cookies\n")
