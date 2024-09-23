import requests
import json

# response = requests.get("http//api.open-notify.org/this-api-doesnt-exist")
# response = requests.get("https://edu-api.21-school.ru/services/21-school/api/v1/events")
response = requests.get("http://api.open-notify.org/astros")
print(response.status_code)

def jprint(obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

jprint(response.json())