import json
import os

def load_metadata(directory):
    meta_path = os.path.join(directory, '.photometa')
    if os.path.exists(meta_path):
        with open(meta_path, 'r') as meta_file:
            return json.load(meta_file)
    return {"photos": {}}

def save_metadata(directory, metadata):
    meta_path = os.path.join(directory, '.photometa')
    with open(meta_path, 'w') as meta_file:
        json.dump(metadata, meta_file, indent=4)

def add_tag(directory, photo_hash, tag):
    metadata = load_metadata(directory)
    if photo_hash not in metadata['photos']:
        metadata['photos'][photo_hash] = []
    if tag not in metadata['photos'][photo_hash]:
        metadata['photos'][photo_hash].append(tag)
    save_metadata(directory, metadata)

def remove_tag(directory, photo_hash, tag):
    metadata = load_metadata(directory)
    if photo_hash in metadata['photos'] and tag in metadata['photos'][photo_hash]:
        metadata['photos'][photo_hash].remove(tag)
        if not metadata['photos'][photo_hash]:
            del metadata['photos'][photo_hash]
    save_metadata(directory, metadata)

# Testing the metadata functions
if __name__ == "__main__":
    test_directory = "testdata/images"  # Replace with actual directory path
    test_hash = "testhash123"
    test_tag = "sample_tag"

    add_tag(test_directory, test_hash, test_tag)
    print(f"Metadata after adding tag: {load_metadata(test_directory)}")

    remove_tag(test_directory, test_hash, test_tag)
    print(f"Metadata after removing tag: {load_metadata(test_directory)}")
