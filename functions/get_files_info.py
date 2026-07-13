import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    absolute_path_wd = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(absolute_path_wd, directory))
    
    try:
        # Checking whether target_dir falls within absolute_path_wd and whether target_dir is an actual directory
        valid_target_dir = os.path.commonpath([absolute_path_wd, target_dir]) == absolute_path_wd
        valid_dir = os.path.isdir(target_dir)
        if valid_target_dir is False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if valid_dir is False:
            return f'Error: "{directory}" is not a directory'
        else:
            return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f"Error: {e}"
        

    