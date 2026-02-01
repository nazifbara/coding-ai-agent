import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        absolute_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_working_dir, file_path))
        is_valid_path = os.path.commonpath([absolute_working_dir, target_file]) == absolute_working_dir

        if not is_valid_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile:
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file, 'r') as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
    except:
        return "Error: Something went wrong"
