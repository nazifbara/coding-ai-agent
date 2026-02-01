import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
        is_valid_path = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir

        if not is_valid_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        if args:
            command.extend(args)
        result = subprocess.run(command, cwd=abs_working_dir,stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True, timeout=30*1000)
        stdout = result.stdout
        stderr = result.stderr
        
        output = ""
        if result.returncode != 0:
            output = f"Process exited with code {result.returncode}\n"
        
        if stderr == "" and stdout == "":
            output += "No output produced"

        if stdout:
            output = f"STDOUT: {stdout}"
        
        if stderr:
            output += f"STDERR: {stderr}"

        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"