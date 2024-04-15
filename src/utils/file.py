def file_name(path: str) -> str:
    return path.split('/')[-1].split('.')[0]


def file_extension(file_name: str) -> str:
    return file_name.split('.')[-1].lower()
