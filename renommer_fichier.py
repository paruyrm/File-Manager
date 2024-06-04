from toolbox import os

def rename_file(directory, old_filename, new_filename):
  
    try:
        old_file_path = os.path.join(directory, old_filename)
        new_file_path = os.path.join(directory, new_filename)
        
        os.rename(old_file_path, new_file_path)
        
        return new_file_path
    except OSError as e:
        print(f"Error renaming file: {e}")
        return None