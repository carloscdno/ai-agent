import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    absolute_path_wd = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(absolute_path_wd, file_path))
    
    try:
        # Checking whether target_file falls within absolute_path_wd and whether target_file is an actual file
        valid_target_file = os.path.commonpath([absolute_path_wd, target_file]) == absolute_path_wd
        valid_file = os.path.isfile(target_file)
        if valid_target_file is False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not valid_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # Reading the file and checking if it's larger than MAX_CHARS
        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
            
    except Exception as e:
        return f"Error: {e}"