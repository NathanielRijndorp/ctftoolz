import zipfile
from pathlib import Path

def extract_and_delete_zip(zip_dir):
    # Loop through all .zip files in the current directory
    for zip_file in zip_dir.glob("*.zip"):
        # Open and extract the zip file
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(path=zip_dir)

        # Delete the .zip file after extraction
        zip_file.unlink()
        print(f"Extracted and deleted {zip_file}")
    
    # Recursively check subdirectories
    for sub_dir in zip_dir.iterdir():
        if sub_dir.is_dir():
            extract_and_delete_zip(sub_dir)

# Example usage: pass the root directory to start extraction
root_dir = Path("/put/path/here")
extract_and_delete_zip(root_dir)