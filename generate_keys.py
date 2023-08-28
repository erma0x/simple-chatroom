from cryptography.fernet import Fernet

# Generate a new encryption key
key = Fernet.generate_key()

# Save the key to a file
with open('encryption_key.txt', 'wb') as file:
    file.write(key)
