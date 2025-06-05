import hashlib

def hash_file(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()
    
def run():
    file_path = input("Enter the file path to check integrity: ")
    try:
        hash_value = hash_file(file_path)
        print(f"SHA-256: {hash_value}")
    except FileNotFoundError:
        print("File not found.")