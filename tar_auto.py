import tarfile
from pathlib import Path
def extract_and_delete_tar(tar_dir):
    # Loop through all .tar files in the current directory
    for tar_file in tar_dir.glob("*.tar"):
        # Open and extract the tar file
        with tarfile.open(tar_file, 'r') as tar:
            tar.extractall(path=tar_dir)
        
        # Delete the .tar file after extraction
        tar_file.unlink()
        print(f"Extracted and deleted {tar_file}")
    # Recursively check subdirectories
    for sub_dir in tar_dir.iterdir():
        if sub_dir.is_dir():
            extract_and_delete_tar(sub_dir)
    extract_and_delete_tar(tar_dir)
# Example usage: pass the root directory to start extraction
root_dir = Path("/put/path/here")
extract_and_delete_tar(root_dir)