import os
import json
import basic_encryption

class StorageManager:
    def __init__(self, file_path, key):
        self.file_path = file_path
        self.encryption_manager = basic_encryption.EncryptionManager(key)
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump({}, file)

    def save_password(self, identifier, password):
        encrypted_password = self.encryption_manager.encrypt(password)
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        data[identifier] = encrypted_password
        with open(self.file_path, 'w') as file:
            json.dump(data, file)

    def retrieve_password(self, identifier):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        encrypted_password = data.get(identifier)
        if encrypted_password:
            return self.encryption_manager.decrypt(encrypted_password)
        return None
