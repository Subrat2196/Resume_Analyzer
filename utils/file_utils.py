import os

# it is to save the analysis of your project
def save_text_to_file(text, output_path):
    """Save text to a file"""
    with open(output_path,'w',encoding='utf-8') as file:
        file.write(text)
    
# it will remove the already existing file if is present 
def remove_file(file_path):
    """Remove a file if it exists"""
    if os.path.exists(file_path):
        os.remove(file_path)
