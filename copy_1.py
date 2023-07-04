import os
import shutil

# Provide the source directory path
source_directory = 'G:/Machine Learning/tensor fllow/tensor Main'

# Iterate over all files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith('.md'):
        # Construct the source and destination file paths
        source_path = os.path.join(source_directory, filename)
        destination_path = os.path.join('.', filename)  # Current directory as the destination
        
        # Copy the file to the destination directory
        shutil.copy2(source_path, destination_path)
