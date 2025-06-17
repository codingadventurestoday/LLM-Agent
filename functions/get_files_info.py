import os 

def get_files_info(working_directory, directory=None):
    directory_items = os.listdir("calculator")

    print(f"is a directory: {os.path.isdir(directory)}")
    if directory not in directory_items:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'

    contents_of_directory = """"""
    
    items_strs = []

    for item in directory_items:
        item_info = f"""- {item}: file_size={os.path.getsize(item)} bytes, is_dir={os.path.isdir(item)}"""
        items_strs.append(item_info)

    contents_of_directory.join(items_strs)
    return contents_of_directory