import shutil
import os

# Define source and destination directories
source_dir = 'staticfiles'
dest_dir = 'static'

# Ensure the destination directory exists
os.makedirs(dest_dir, exist_ok=True)

# Copy files
for root, dirs, files in os.walk(source_dir):
    for file in files:
        src_file = os.path.join(root, file)
        relative_path = os.path.relpath(src_file, source_dir)
        dest_file = os.path.join(dest_dir, relative_path)

        # Ensure subdirectories exist in the destination
        os.makedirs(os.path.dirname(dest_file), exist_ok=True)

        # Copy file
        shutil.copy2(src_file, dest_file)

print("Files successfully moved from 'staticfiles' to 'static'.")
