import hashlib

def generate_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

# Testing the hash generation function
if __name__ == "__main__":
    test_file = "path/to/your/test/photo.jpg"  # Replace with actual file path
    print(f"Hash for {test_file}: {generate_hash(test_file)}")
