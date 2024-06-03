from typing import Dict, Optional
import csv

def main_menu():
    """Main menu options"""
    print('''
          1. Add Contact
          2. View Contacts
          3. Search Contacts
          4. Delete Contact
          5. Exit
          ------------------------
          ''')
    try:
        user_input = int(input('What would you like to do?\n'))
        if user_input > 5 or user_input < 1:
            print("Invalid option. Please choose a valid option.")
            return main_menu()
        else:
            return user_input
    except ValueError:
        print('Invalid input. Please enter a number.')
        return main_menu()
    
# Connect to SQL database?
def data_structure() -> Dict[str, Dict[int, Optional[str]]]:
    """Initialize the contact book

    Returns:
        Dict[str, Dict[int, Optional[str]]]: Dictionary that will contain the contacts
    """
    
    return {}

def add_contacts(contacts: Dict[str, Dict[int, Optional[str]]]) -> None:
    """Adds contacts to the contact book

    Args:
        contacts (Dict[str, Dict[int, Optional[str]]]): Dictionary that have or will have the contacts
    """
    
    name = input('Enter name of contact:\n')
    
    while True:
        phone = input('Enter phone number of contact:\n')
        if phone.isdigit():
            phone = int(phone)
            break
        else:
            print('Invalid input. Please enter a valid phone number.')
            
    email = input('Enter email address of contact (optional):\n')
    address = input('Enter the address of contact (optional):\n')

    if name in contacts and any(contact == phone for contact in contacts[name].values()):
        print('Contact already exists.')
    else:
        contacts[name] = {'phone': phone,
                          'email': email,
                          'address': address}
        print('Contact added successfully!')

def view_contacts(contacts: Dict[str, Dict[int, Optional[str]]]):
    """Display a list of contacts"""
    
    if not contacts:
        print("No contacts saved yet.")
        return

    for name, details in contacts.items():
        if isinstance(details, str):
            print(f"** {name} **")
            print(f"Contact details: {details}")
        elif isinstance(details, dict):
            print(f"** {name} **")
            print(f"Phone: {details.get('phone')}")
            print(f"Email: {details.get('email')}")
            print(f"Address: {details.get('address')}")
        print("------------------------")

def search_contacts(contacts: Dict[str, Dict[int, Optional[str]]]):
    """Search for a specific contact by name"""
    
    search_param = input('Please enter the name you are searching for:\n').lower()
    for name, contact_info in contacts.items():
        if search_param in name.lower():
            print(f"Contact found: {name}")
            print(f"Phone: {contact_info.get('phone')}")
            print(f"Email: {contact_info.get('email')}")
            print(f"Address: {contact_info.get('address')}")
            print("------------------------")
            return
        
    print('Contact not found.')
    

def delete_contacts(contacts: Dict[str, Dict[int, Optional[str]]]):
    """Prompt the user if they want to delete a contact"""
    
    name = input('Enter the name of the contact you wish to delete:\n')
    if name in contacts:
        del contacts[name]
        print(f'Contact {name} has been deleted.')
    else:
        print('Contant not found.')
        


def exit_book(contacts: Dict[str, Dict[int, Optional[str]]]):
    """"Promt user if they want to save the contact book before exiting"""
    
    response = input('Do you want to save your contact book before exiting? (Y/N)\n')
    if response.upper() == 'Y':
        file_name = input('Please enter a file name (example, contact_book.csv)\n')
        save_contact(contacts, file_name)
    elif response.upper() == 'N':
        print('Thank you for using the contact book!')
    else:
        print('Invalid response. Please enter Y or N.')
        
def save_contact(contacts: Dict[str, Dict[int, Optional[str]]], file_name: str):
    with open(file_name, 'w', newline='') as csvfile:
        col_names = ['Name', 'Phone', 'Email', 'Address']
        writer = csv.DictWriter(csvfile, fieldnames=col_names)
        writer.writeheader()
        
        for name, details in contacts.items():
            writer.writerow({
                'Name': name,
                'Phone': details.get('phone'),
                'Email': details.get('email'),
                'Address': details.get('address')
            })
    
def main():
    contacts = data_structure()
    while True:
        user_input = main_menu()
        if user_input == 1:
            add_contacts(contacts)
        elif user_input == 2:
            view_contacts(contacts)
        elif user_input == 3:
            search_contacts(contacts)
        elif user_input == 4:
            delete_contacts(contacts)
        else:
            exit_book(contacts)
            break
        
if __name__ == '__main__':
    main()

    
    