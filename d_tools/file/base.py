from uuid import uuid4


def change_filename_to_uuid4(filename: str, uuid: uuid4 = uuid4()) -> str:
    return f"{uuid}.{filename.split('.')[-1]}"
