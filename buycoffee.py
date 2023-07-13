import os

# Get the current directory
directory = './tensorflow/'

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.md') and filename != 'README.md' and os.path.isfile(os.path.join(directory, filename)):
        # Construct the file path
        file_path = os.path.join(directory, filename)

        # Read the contents of the input file
        with open(file_path, 'r') as file:
            content = file.read()

        # Append the JavaScript code at the bottom of the file
        updated_content = f"{content}\n<script>\n\nconst recaptchaScript = document.createElement('script');\nrecaptchaScript.setAttribute('src', 'https://storage.ko-fi.com/cdn/scripts/overlay-widget.js');\ndocument.head.appendChild(recaptchaScript);\n\nkofiWidgetOverlay.draw('boratechlife', {{\n  'type': 'floating-chat',\n  'floating-chat.donateButton.text': 'TIP ME',\n  'floating-chat.donateButton.background-color': '#5cb85c',\n  'floating-chat.donateButton.text-color': '#fff'\n}});\n\n</script>"

        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(updated_content)
