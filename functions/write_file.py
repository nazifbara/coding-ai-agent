import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        absolute_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_working_dir, file_path))
        is_valid_path = os.path.commonpath([absolute_working_dir, target_file]) == absolute_working_dir

        if not is_valid_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, 'w') as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except:
        return "Error: Something went wrong while operating the file"
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite files",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write or overwrite, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write"
            )
        },
    ),
)