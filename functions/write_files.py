import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    absolute_path_wd = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(absolute_path_wd, file_path))
    
    try:
        # Checking whether target_file falls within absolute_path_wd and whether target_file points to an existing directory
        valid_target_file = os.path.commonpath([absolute_path_wd, target_file]) == absolute_path_wd
        valid_dir = os.path.isdir(target_file)
        if valid_target_file is False:
            print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
            return
        if valid_dir:
            print(f'Error: Cannot write to "{file_path}" as it is a directory')
            return
        
        # Making sure that all parent directories of file_path exist
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        
        # Writing the file
        with open(target_file, "w") as f:
            f.write(content)
        
        if os.path.exists(target_file):
            print(f"Created file: {target_file}")
      
            
            
            
    except Exception as e:
        return f"Error: {e}"
    
write_file("calculator", "pkg", "some content")