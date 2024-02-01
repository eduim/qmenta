from pydicom import dcmread
from PIL import Image
from io import BytesIO
import numpy as np

def get_dicom_dataset(file_path: str) -> str:
  dicom_file = dcmread(file_path)
  return dicom_file.to_json()

def get_name_from_dicom(file_path: str) -> str:
  dicom_file = dcmread(file_path)
  return dicom_file.PatientName

def dicom_to_png(file_path):
    print(file_path)
    dicom_file = dcmread(file_path)
    pixel_array = dicom_file.pixel_array
    normalized_pixel_data = (pixel_array / pixel_array.max() * 255).astype('uint8')
  
    image = Image.fromarray(normalized_pixel_data)
    # image.save('test.png')
    img_bytes_io = BytesIO()
    image.save(img_bytes_io, format='PNG')

    return img_bytes_io.getvalue()
