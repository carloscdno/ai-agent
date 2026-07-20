import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    absolute_path_wd = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(absolute_path_wd, file_path))
    
    try:
        # Checking whether target_file falls within absolute_path_wd and whether target_file is a valid file
        valid_target_file = os.path.commonpath([absolute_path_wd, target_file]) == absolute_path_wd
        valid_file = os.path.isfile(target_file)
        
        if valid_target_file is False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not valid_file:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        if args:
            command.extend(args)
    
        # Creating a subprocess to run the command
        result = subprocess.run(
            command,
            cwd=absolute_path_wd,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        parts = []
        if not result.stdout and not result.stderr:
            parts.append("No output produced")
        else:
            parts.append(f"STDOUT: {result.stdout}")
            parts.append(f"STDERR: {result.stderr}")
        
        if result.returncode != 0:
            parts.append(f"Process exited with code {result.returncode}")
        
        output = "\n".join(parts)
        return output
            
    except Exception as e:
        return f"Error: executing Python file: {e}"