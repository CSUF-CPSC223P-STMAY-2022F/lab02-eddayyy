# Author Name: Eduardo NUnez
# Author email: eduardonunez@csu.fullerton.edu
# File Purpose: 

def print_list(contact_list):
    ''' This functions prints out our contacts list. '''
    print("\n================== CONTACT LIST ==================\n", "Index   First Name            Last Name\n", "======  ====================  ====================")
    for contact in contact_list:
        print(f'{contact_list.index(contact)}\t {contact[0]}\t\t\t{contact[1]}')



def add_contact(contact_list):
    ''' This function allows the user to add a contact to contact_list.''' 
    x = input("\nEnter the first name: ")
    y = input("\nEnter the last name: ")
    contact_list.append([x,y])
    return contact_list


def modify_contact(contact_list):
    ''' This function allows the user to modify an element in contact_list.'''
    input_string = input("Enter the index number: ")
    i = int(input_string)
    if i < len(contact_list):
        contact_list.pop(i)
        x = input("Enter first name: ") 
        y = input("Enter last name: ")
        contact_list.insert(i, [x, y])
        # contact_list[modified_contact] = [x, y]
        return contact_list
    else:
        print("Invalid index number.")
        return contact_list

def delete_contact(contact_list):
    ''' This function allows the user to delete a contact from conact_list.'''
    input_string = input("Enter the index number: ")
    i = int(input_string)
    if i < len(contact_list):
        contact_list.pop(i)
        return contact_list
    else:
        print("Invalid index number.")
        return contact_list



def exit_program():
    print("You have chosen to exit the program. Good-Bye!")
    quit()


