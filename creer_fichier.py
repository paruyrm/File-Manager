from toolbox import os

def create_file(directory, filename, content=None):
   
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_path = os.path.join(directory, filename)
    
    try:
        with open(file_path, 'w') as file:
            if content:
                file.write(content)
    except IOError as e:
        print(f"Error creating file: {e}")
        return None
    
    return file_path