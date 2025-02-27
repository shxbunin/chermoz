from pathlib import Path
import uuid

upload_dir = Path("uploads")


def get_unique_filename(file_name):
    ext = Path(file_name).suffix
    unique_filename = uuid.uuid4().hex + ext
    return unique_filename
def save_file(file_content, file_name):
    file_path = upload_dir / get_unique_filename(file_name)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_bytes(file_content)
    print(file_path)
    return str(file_path)