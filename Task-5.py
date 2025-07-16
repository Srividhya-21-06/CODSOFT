Contacts = []
def adding_Contact():
    print("\n📇 Add New Contact")
    Name = input("Name: ")
    Phone_no = input("Phone Number: ")
    Email_id = input("Email: ")
    Address = input("Address: ")
    Contact = {
        "Name": Name,
        "Phone_no": Phone_no,
        "Email_id": Email_id,
        "Address": Address
    }
    Contacts.append(Contact)
    print("✅ Contact added successfully!")
def viewing_Contacts():
    if not Contacts:
        print("\n📭 No Contacts available.")
        return
    print("\n📋 Contact List:")
    for i, Contact in enumerate(Contacts, 1):
        print(f"\n{i}. {Contact['Name']} | 📞 {Contact['Phone_no']}")
        print(f"   ✉️ {Contact['Email_id']}")
        print(f"   🏠 {Contact['Address']}")
def searching_Contact():
    search = input("\n🔍 Search by Name or Phone: ").lower()
    found = False
    for Contact in Contacts:
        if search in Contact['Name'].lower() or search in Contact['Phone_no']:
            print(f"\n📍 Found Contact:")
            print(f"Name: {Contact['Name']}")
            print(f"Phone: {Contact['Phone_no']}")
            print(f"Email: {Contact['Email_id']}")
            print(f"Address: {Contact['Address']}")
            found = True
    if not found:
        print("❌ Contact not found.")
def updating_Contact():
    Name = input("\n✏️ Enter the name of the contact to update: ").lower()
    for Contact in Contacts:
        if Contact['Name'].lower() == Name:
            print("Leave blank to keep existing value.")
            Contact['Phone_no'] = input(f"New Phone_no ({Contact['Phone_no']}): ") or Contact['Phone_no']
            Contact['Email_id'] = input(f"New Email_id ({Contact['Email_id']}): ") or Contact['Email_id']
            Contact['Address'] = input(f"New Address ({Contact['Address']}): ") or Contact['Address']
            print("✅ Contact updated successfully.")
            return
    print("❌ Contact not found.")
def deleting_Contact():
    Name = input("\n🗑️ Enter the Name of the Contact to delete: ").lower()
    for i, Contact in enumerate(Contacts):
        if Contact['Name'].lower() == Name:
            del Contacts[i]
            print("🗑️ Contact deleted.")
            return
    print("❌ Contact not found.")
while True:
    print("\n📞 Contact Management System")
    print("1. To Add Contact")
    print("2. To View Contacts")
    print("3. To Search Contact")
    print("4. To Update Contact")
    print("5. To Delete Contact")
    print("6. To Exit")
    user_choice = input("Enter your choice (1-6): ")
    if user_choice == '1':
        adding_Contact()
    elif user_choice == '2':
        viewing_Contacts()
    elif user_choice == '3':
        searching_Contact()
    elif user_choice == '4':
        updating_Contact()
    elif user_choice == '5':
        deleting_Contact()
    elif user_choice == '6':
        print("👋 Exiting Contact Manager.Byeeee!")
        break
    else:
        print("❌ Invalid choice. Please enter only from 1–6.")
