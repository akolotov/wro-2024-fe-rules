import os

def read_file_content(file_path):
    """
    Read and return the content of a file.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there's an error reading the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_filename_from_path(file_path: str) -> str:
    """Extract the filename from a file path.
    
    Args:
        file_path (str): The full path to the file
        
    Returns:
        str: The filename without the path
    """
    return os.path.basename(file_path)
