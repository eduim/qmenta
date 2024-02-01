import requests
ENDPOINT = "http://localhost:8000/api/auth/login"

username = 'eyR5X@example.com'
password = 'adminsafestpasswordever'

def test_login_successful():
  response = requests.post(ENDPOINT, data={'username': username, 'password': password})
  assert response.status_code == 200

def test_login_unsuccessful():
  response = requests.post(ENDPOINT, data={'username': username, 'password': 'wrongpassword'})
  assert response.status_code == 400