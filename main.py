import requests
client = requests.session()
#LbWAKMJeoO9KOhGqs2NcnDDfOxdwT3BkiY6MXB4kbeP6lUFONocPNfFdCQsqvJaY
key = "LbWAKMJeoO9KOhGqs2NcnDDfOxdwT3BkiY6MXB4kbeP6lUFONocPNfFdCQsqvJaY"

rr=client.get("http://127.0.0.1:8000/api/loginUser/").text

#print(rr)

#headers = '{username: "daddy", email: "max@max.ru", password: "dick", ' + "csrfmiddlewaretoken: " +

#test = client.post("http://127.0.0.1:8000/api/createUser/", data={
#    'username': "daddy", 'email': "max@max.ru", 'password': "dick", "csrfmiddlewaretoken": key, "next": '/'
#})

test = client.post("http://127.0.0.1:8000/api/loginUser/", data=dict(
    username= "daddy", email= "max@max.ru", password= "dick", csrfmiddlewaretoken= rr, next= '/'
), headers=dict(Referer="http://127.0.0.1:8000/api/loginUser/"))

print(test)
print(test.text)

test = client.post("http://127.0.0.1:8000/api/getData/", data=dict(
    username= "daddy", email= "max@max.ru", password= "dick", csrfmiddlewaretoken= test.cookies.get("csrftoken"), next= '/'
), headers=dict(Referer="http://127.0.0.1:8000/api/loginUser/"))

print(test)
print(test.text)

#import sys
#import requests
#
#URL = 'http://127.0.0.1:8000/api/createUser/'
#
#client = requests.session()
#
## Retrieve the CSRF token first
#client.get(URL)  # sets cookie
##if 'csrftoken' in client.cookies:
##    # Django 1.6 and up
##    csrftoken = client.cookies['csrftoken']
##else:
##    # older versions
##    csrftoken = client.cookies['csrf']
#
#login_data = dict(username="max@max.ru", password="dick", csrfmiddlewaretoken=csrftoken, next='/')
#r = client.post(URL, data=login_data, headers=dict(Referer=URL))