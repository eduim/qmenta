from pydicom import dcmread
import requests 
def get_name_from_dicom(file_path: str) -> str:
  dicom_file = dcmread(file_path)
  return dicom_file.PatientName

async def seed_db():
  # create user 
  image_url = './app/data/MR000003'
  patient_name = get_name_from_dicom(image_url)
  
  requests.post('http://localhost:8000/api/users/create', json={'username': f'{patient_name}', 'email': 'eyR5X@example.com', 'password': 'adminsafestpasswordever'})

  # login user 
  login_response = requests.post('http://localhost:8000/api/auth/login', data={'username': 'eyR5X@example.com', 'password': 'adminsafestpasswordever'})
  
  if login_response.status_code == 200:
  
    json_response = login_response.json()
    token = json_response.get('access_token')
    print(token)
    headers = {
      'Authorization': f'Bearer {token}'
    }
    # craete image 
    image_response = requests.post('http://localhost:8000/api/images/create', headers=headers, json={'image_url':image_url})
    print(image_response.json().get('image_id'))
    if image_response == 200:
      print('Seed successful')

if __name__ == "__main__":
  import asyncio 
  asyncio.run(seed_db())
  