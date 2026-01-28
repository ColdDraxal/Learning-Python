# # # #Create a dictionary with at least 4 contacts
# # # (name → phone number)
# # # Ask the user to enter a name
# # # If the name exists:
# # # print the phone number
# # # If the name does not exist:
# # # print None
# # # (no fancy message needed — you’re okay with None)
# # contacts={"darpan":"9841111686",
# #           "firoj":"9869747076",
# #           "sahil":"9748703586",
# #           "makchud":"9749378099"}
# # name=input("Enter a name to get the phone number:").strip().lower()
# # number=contacts.get(name)
# # if number is None:
# #     print("the number doesn't exist in contacts.")
# #     new=input("would you like to add new number? (yes/no):")
# #     if new.strip().lower() == "yes":
# #         new_number=input("Enter the phone number:")
# #         contacts[name]=new_number
# #         print("Number added successfully.")
# #     else:
# #         print("Number doesn't exist.")

# # else:
# #      print("The number is:",number)


# Create a dictionary with at least 3 contacts
# store all names in lowercase
# Ask the user to enter a name
# make input case-insensitive
# remove extra spaces
# If the contact exists:
# print the phone number
# If the contact does not exist:
# ask: Would you like to add this contact? (yes/no)
# if yes:
# ask for phone number
# add it to the dictionary
# confirm it was added
# if no:
# print a message and exit
contacts={"darpan":"9841111686",
          "firoj":"9869747076",
          "sahil":"9748703586"}
name=input("Enter a name to get the phone number:").strip().lower()
number=contacts.get(name)
if number is None:
    print("This number doesn't exist")
    new=input("Would you like to add this contact? (yes/no):")
    if new.strip().lower()== "yes":
        new_number=input("Enter the phone number:")
        contacts[name]=new_number
        print("Your number is saved")
    else:
        print("number doesn't exist")
else:
    print("The number is :",number)
    