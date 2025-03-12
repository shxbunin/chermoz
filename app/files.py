from pathlib import Path
import uuid
import boto3
import io
from config import settings

app_dir = Path("app")
upload_dir = Path("gallery")
static_dir = Path("static")
bucket_name = 'chermoz'

s3 = boto3.client(
    service_name=settings.service_name,
    endpoint_url = settings.endpoint_url,
    aws_access_key_id = settings.aws_access_key_id,
    aws_secret_access_key = settings.aws_secret_access_key
)

def get_unique_filename(file_name):
    ext = Path(file_name).suffix
    unique_filename = uuid.uuid4().hex + ext
    return unique_filename

def save_file(file_content, file_name):
    name = get_unique_filename(file_name)
    file_path = upload_dir / name
    file_obj = io.BytesIO(file_content)
    s3.upload_fileobj(file_obj, bucket_name, str(file_path.as_posix()))
    return f"https://{bucket_name}.storage.yandexcloud.net/{str(file_path.as_posix())}"