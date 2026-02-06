import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        heading = f"Result for {directory} directory:\n"
        absolute_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_working_dir, directory))
        valid_target_dir = os.path.commonpath([absolute_working_dir, target_dir]) == absolute_working_dir

        if not valid_target_dir:
            return f'{heading}  Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'{heading}  Error: "{directory}" is not a directory'
        
        list_of_dir = os.listdir(target_dir)

        list_of_info = map(lambda dir: f"- {dir}: file_size={f"{get_file_size(target_dir +"/"+dir)}"} bytes, is_dir={os.path.isdir(target_dir +"/"+dir)}", list_of_dir)

        return  heading + "\n".join(list_of_info)
    except:
        return f"Error: Something went wrong..." 
        


def get_file_size(path):
    return os.path.getsize(path)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)