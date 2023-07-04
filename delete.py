import os

# Provide the directory path where the files are located
directory_path = '.'

# Iterate over all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.md') and filename != 'index.md':
        # Construct the file path
        file_path = os.path.join(directory_path, filename)
        
        # Delete the file
        os.remove(file_path)
