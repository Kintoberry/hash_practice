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