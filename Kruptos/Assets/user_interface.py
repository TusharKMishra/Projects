#from storage import StorageManager
import local_storage

class UserInterface:
    def __init__(self, storage_manager):
        self.storage_manager = storage_manager

    def add_password(self):
        identifier = input("Enter the identifier for the password: ")
        password = input("Enter the password: ")
        self.storage_manager.save_password(identifier, password)
        print("Password saved successfully.")

    def get_password(self):
        identifier = input("Enter the identifier for the password: ")
        password = self.storage_manager.retrieve_password(identifier)
        if password:
            print(f"The password for {identifier} is: {password}")
        else:
            print("Password not found.")
