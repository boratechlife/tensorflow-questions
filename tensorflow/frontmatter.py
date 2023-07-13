import os
from datetime import date
from slugify import slugify

# Get the current directory
directory = '.'

# Get today's date
today = date.today()
publish_date = today.strftime("%d %b %Y")

def slug_to_text(slug):
    text = slugify(slug)
    text = text.replace('-', ' ')
    return text

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.md') and os.path.isfile(os.path.join(directory, filename)):
        # Get the file name without the extension
        title = slug_to_text(os.path.splitext(filename)[0])

        # Read the contents of the input file
        with open(filename, 'r') as file:
            content = file.read()

        # Construct the updated content with the front matter
        updated_content = f'''---
title: "{title}"
author: "stef"
date: "{publish_date}"
excerpt: "So, you’ve got your business website built, it’s got all the correct information on it to entice your ideal customer, its load times are optimized so they don’t swipe away, everything is ready to go… but what if they don’t show up?"
TOP: "Marketing"
thumbnail: "/post-images/whySEO.png"
thumbnailSource: "stef"
---

{content}'''

        # Write the updated content back to the file
        with open(filename, 'w') as file:
            file.write(updated_content)
