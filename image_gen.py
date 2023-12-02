from openai import OpenAI
import os
import base64
from google.cloud import storage
from io import BytesIO

def generate_image(prompt):
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    response = client.images.generate(
    model="dall-e-2",
    prompt=prompt,
    size="256x256",
    n=1,
    response_format="b64_json"
    )
    base64_img = response.data[0].b64_json
    return base64_img

def save_img(id, base64_img):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('dream-journal')
    blob = bucket.blob(blob_name=(str(id) + '.jpg'))
    img = base64.b64decode(base64_img)
    blob.upload_from_file(BytesIO(img), content_type='image/jpeg')

def get_img(id):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('dream-journal')
    blob = bucket.blob(str(id) + '.jpg')
    blob.make_public()
    return blob.public_url
