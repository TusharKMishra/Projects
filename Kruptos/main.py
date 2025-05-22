import Assets.local_storage
import Assets.user_interface
import Assets.basic_encryption

def main():
    key = input("Enter your encryption key: ")
    storage_manager = Assets.local_storage.StorageManager('passwords.json', key)
    ui = Assets.user_interface.UserInterface(storage_manager)

    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            ui.add_password()
        elif choice == '2':
            ui.get_password()
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
