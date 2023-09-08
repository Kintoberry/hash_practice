import hashlib
import os

file_name = os.path.join(os.getcwd(), 'text_files', 'harrypotter.txt')
hasher = hashlib.new('sha256')

with open (file_name, 'rb') as file:
    while True:
        data = file.read(8192)
        if not data:
            break
        hasher.update(data)

print(hasher.hexdigest())
        

# # Function to calculate the hash of a file
# def calculate_file_hash(file_path, hash_algorithm='sha256'):
#     hasher = hashlib.new(hash_algorithm)
#     with open(file_path, 'rb') as file:
#         while True:
#             data = file.read(8192)  # Read the file in chunks
#             if not data:
#                 break
#             hasher.update(data)
#     return hasher.hexdigest()

# # Create a simple text file with content
# original_content = "This is the original content of the file."
# file_name = "sample.txt"

# with open(file_name, 'w') as file:
#     file.write(original_content)

# # Calculate the hash of the original file
# original_hash = calculate_file_hash(file_name)
# print(f"Original Hash: {original_hash}")

# # Modify the file's content slightly
# modified_content = "This is the slightly modified content of the file."
# with open(file_name, 'w') as file:
#     file.write(modified_content)

# # Calculate the hash of the modified file
# modified_hash = calculate_file_hash(file_name)
# print(f"Modified Hash: {modified_hash}")

# # Compare the hash values
# if original_hash == modified_hash:
#     print("The hash values are the same. Content is identical.")
# else:
#     print("The hash values are different. Content has changed.")
