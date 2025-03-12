from pathlib import Path
import uuid

app_dir = Path("app")
upload_dir = Path("gallery")
static_dir = Path("static")

def get_unique_filename(file_name):
    ext = Path(file_name).suffix
    unique_filename = uuid.uuid4().hex + ext
    return unique_filename

def save_file(file_content, file_name):
    name = get_unique_filename(file_name)
    file_path = app_dir / static_dir / upload_dir / name
    file_path.write_bytes(file_content)
    return str((upload_dir / name).as_posix())