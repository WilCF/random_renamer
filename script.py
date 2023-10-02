import os
import random
import string
import shutil

def random_filename(extension):
    """Generate a random filename with the format: A capital letter followed by a 2 digit number."""
    letter = random.choice(string.ascii_uppercase)
    number = str(random.randint(0, 99)).zfill(2)
    return f"{letter}{number}{extension}"

def rename_files_in_folder():
    """Rename files in the current folder to random names while keeping their original extensions."""
    existing_names = set()

    # Get the current directory (where the script is located)
    folder_path = os.path.dirname(os.path.abspath(__file__))

    # Create a new folder called 'new' inside the current directory
    new_folder_path = os.path.join(folder_path, 'new')
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    for filename in os.listdir(folder_path):
        # Skip if it's the 'new' directory itself or the script itself
        if filename == 'new' or filename == os.path.basename(__file__):
            continue

        # Extract the file extension
        name, extension = os.path.splitext(filename)

        # Generate a unique random filename
        new_name = random_filename(extension)
        while new_name in existing_names:
            new_name = random_filename(extension)

        existing_names.add(new_name)

        # Move and rename the file to the 'new' directory
        shutil.copy(os.path.join(folder_path, filename), os.path.join(new_folder_path, new_name))
        print(f"Copied and renamed {filename} to {new_name}")

if __name__ == "__main__":
    rename_files_in_folder()
