### what is this?
### it's like including a library. 
### in C it would look like this "include <stdio.h>" for example
import requests
import json
### so we are adding 2 libraries: requests and json


# response = requests.get("http//api.open-notify.org/this-api-doesnt-exist")
# response = requests.get("https://edu-api.21-school.ru/services/21-school/api/v1/events")

### what is this?
### variable named "response", gets result from function "requests.get", and we peredaem ei ssilky as the first argument
response = requests.get("http://api.open-notify.org/astros")
### then it prints status code that it got from function call
print(response.status_code)
### btw, 200 means OK in HTTP. why not 0 tho? who knows ~.~

### what is that?
### function DEFenition. yeah, we create functions this way in python. weird
### i'm so used to "void funct_name() { }" or "int funct_name() { }" that it feels weird to use "def"
### but it is as it is~
def jprint(obj):
        ### then, variable text gets result of function json.dumps.
        ### what are these arguments tho?
        ### obj is an object, in our case an object from response
        ### sort_keys=True tells json.dumps to sort keys in alphabetical order
        ### indent=4, is a number of spaces 
        text = json.dumps(obj, sort_keys=True, indent=1)
        print(text)

### what is this? why won't I just use print?
### cuz jprint is prettier!
### like, for real. try it out! "print" is very basic and hardly readable
jprint(response.json())
# print(response.json())