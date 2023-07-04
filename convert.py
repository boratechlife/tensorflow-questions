import os
import json
import re
from slugify import slugify

def slug_to_text(slug):
    text = slugify(slug)
    text = text.replace('-', ' ')
    return text

def read_filenames(directory):
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.md') and os.path.isfile(os.path.join(directory, filename)):
            filenames.append({
                'name': os.path.splitext(filename)[0],
                'slug': slugify(os.path.splitext(filename)[0])
            })
    return filenames

def write_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file)


def rename_files(directory, filenames):
    for filedata in filenames:
        original_filename = filedata['name']
        slug = filedata['slug']
        extension = '.md'
        original_path = os.path.join(directory, original_filename + extension)
        new_filename = slug + extension
        new_path = os.path.join(directory, new_filename)
        os.rename(original_path, new_path)

def edit_files(directory, filenames):
    for filedata in filenames:
        filename = filedata['slug']
        if filename != 'index':
            filepath = os.path.join(directory, filename + '.md')
            with open(filepath, 'r+') as file:
                content = file.read()
                title_line = f"# {slug_to_text(filedata['name'])}\n\n"
                file.seek(0, 0)
                file.write(title_line + content)

# Provide the directory path where the files are located
directory_path = '.'

# Provide the output file path for the JSON file
output_file_path = './output.json'

# Read filenames and slugs from the directory
file_data = read_filenames(directory_path)

# Rename each file to its corresponding slug name
rename_files(directory_path, file_data)

# Edit each file by adding the name as the title, except for index.md
edit_files(directory_path, file_data)

# Write filenames and slugs to the JSON file
write_to_json(file_data, output_file_path)
