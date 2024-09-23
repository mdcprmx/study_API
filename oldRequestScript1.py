import requests
import json

class SberClassAPI:
    def __init__(self):
        self.access_token_url = "https://auth.sberclass.ru/auth/realms/EduPowerKeycloack/protocol/openid-connect/token"
        self.client_id = "s21-open-api"

    def get_access_token(self, login, password):
        payload = {
            "grant_type": "password",
            "client_id": self.client_id,
            "username": login,
            "password": password
        }
    
    response = requests.post(self.access_token_url, data=payload)

    if response.status_code == 200:
        # return response.json().get("access token")
        print("success 1")
    else:
        raise Exception(f"Failed to get muh access token bruh: {response.text}")
    
    def make_api_request(self, endpoint, method="GET", data=None, params=None):
        access_token = self.get_access_token()
        headers = {"Authorization": f"Bearer {access_token}"}

        response = requests.request(method, endpoint, json=data, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API failed: {resnonse.text}")
        
api = SberClassAPI()

try:
    # replace with actual credentials
    login = "123@student.21-school.ru"
    password = "123"

    # getting access token
    access_token = api.get_access_token(login, password)
    print(f"Access token: {access_token}")

    # make API requests
    result = api.make_api_request("https://edu-api.21-school.ru/services/21-school/api/v1/events")
    print(json.dumps(result, indent=2))

except Exception as e:
    print(f"Error: {str(e)}")

