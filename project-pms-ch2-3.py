import random
import time

# Initialize variables
menuOptionMain = 0
menuOptionCreate = 0
startTime = 0
endTime = 0
elapseTime = 0.00
personCreationHour = 0
personCreationMin = 0
personSalary = 0.00
personCount = 0
personID = 0
personFirstName = "null"
personLastName = "null"
personStreetNo = 0
personStreetName = "null"
personCity = "null"
personState = "null"
personZip = 0
personPhone = 0
initial_ID = 2023001


#print program title and introductory messages
print("==========================================================")
print("Person Management System")
print("==========================================================")
print("Welcome to Person Management System (PMS)!)")
print("This program only has ch0, ch1, ch2, ch3-Selection Topics")
print("==========================================================\n")

# Print main menu options
print("Main Menu\n")
print("1 - [CREATE] Person")
print("2 - [READ] Persons")
print("3 - [UPDATE] Person")
print("4 - [DELETE] Person")
print("5 - [FIND] Person\n")

# Read user's input for the main menu option
menuOptionMain = int(input("Please input 1-5:  "))

print("\n")
print("==========================================================")
print("[user-input-auto-selection] =", menuOptionMain)
print("==========================================================\n")

# [Create] person
if menuOptionMain == 1:

    print("[Create] Person Option\n")
    print("1 - AUTO - CREATE PERSON FORM")
    print("2 - NORMAL - CREATE PERSON FORM\n")

    menuOptionCreate = int(input("Please input 1-2:  "))

    print("")
    print("==========================================================")
    print("[user-input-auto-selection] =", menuOptionCreate)
    print("==========================================================\n")

    # AUTO CREATE Person form
    if menuOptionCreate == 1:
        print("==========================================================")
        print("========AUTO========CREATE Menu - Form====================")
        print("==========================================================\n")
        
        # Calculate person creation time
        endTime = time.time()
        elapseTime = int((endTime - startTime) % 60)
        personCreationMin = int(((time.time() / 60) % 60))
        personCreationHour = int((((time.time() / 60) / 60) % 24))
        
        # Time Zone Central
        personCreationHour -= 5
        
        #AM or PM
        personCreationHour = personCreationHour + 12 if personCreationHour < 0 else personCreationHour

        startTime = time.time()
        personCount += 1
        personID = 2023001 + personCount + 1
        personFirstName = "null"
        personLastName = "null"
        personStreetNo = int((random.randint(111, 22999)))
        personStreetName = "null"
        personCity = "null"
        personState = "null"
        personZip = int(random.randint(77000, 77999))
        personPhone = int(random.randint(7131111111, 7139999999))
        personSalary = int(random.randint(25000, 250000))

        # Print person details
        print("Current Time: ", personCreationHour, ":", personCreationMin)
        print("Person Creation Time: ", elapseTime, "sec")
        print("Person Count: ", personCount)
        print("Person ID: ", personID)
        print("First Name: ", personFirstName)
        print("Last Name: ", personLastName)
        print("Street Number: ", personStreetNo)
        print("Street Name: ", personStreetName)
        print("City: ", personCity)
        print("State: ", personState)
        print("Zip Code: ", personZip)
        print("Phone number: ", personPhone)
        print("Salary: $", personSalary)
        print("\n")
        
        print("Row #", personCount + 1, " | ID = ", personID, " | First Name = ", personFirstName, " | Last Name: ", personLastName, " | Street Number: ", personStreetNo, " | Street Name: ", personStreetName, " | City: ", personCity, " | State: ", personState, " | Zip Code: ", personZip, " | Phone #: ", personPhone, " | Salary: $", personSalary, "]\n")

        
    elif menuOptionCreate == 2:

        print("==========================================================")
        print("======NORMAL========CREATE Menu - Form====================")
        print("==========================================================\n")
        
        # Calculate person creation time
        endTime = time.time()
        elapseTime = int((endTime - startTime) % 60)
        personCreationMin = int(((time.time() / 60) % 60))
        personCreationHour = int((((time.time() / 60) / 60) % 24))
        
        # Time Zone Central
        personCreationHour -= 5
        
        #AM or PM
        personCreationHour = personCreationHour + 12 if personCreationHour < 0 else personCreationHour
        
        startTime = time.time()
        personCount += 1
        personID = 2023001 + personCount + 1
        personFirstName = "null"
        personLastName = "null"
        personStreetNo = int(input("Enter Street Number [ADDRESS]: "))
        personStreetName = "null"
        personCity = "null"
        personState = "null"
        personZip = int(input("Enter Zip Code [ADDRESS]: "))
        personPhone = int(input("Enter Phone number [ADDRESS]: "))
        personSalary = int(input("Please enter your current Salary (ex. 25000 or 250000): $"))

        # Print person details
        print("")
        print("Current Time: ", personCreationHour, ":", personCreationMin)
        print("Person Creation Time: ", elapseTime, "sec")
        print("Person Count: ", personCount)
        print("Person ID: ", personID)
        print("First Name: ", personFirstName)
        print("Last Name: ", personLastName)
        print("Street Number: ", personStreetNo)
        print("Street Name: ", personStreetName)
        print("City: ", personCity)
        print("State: ", personState)
        print("Zip Code: ", personZip)
        print("Phone number: ", personPhone)
        print("Salary: $", personSalary)
        print("")

        print("==========================================================")
        print("============== PERSON ADD: ID# ", personID, " =================")
        print("==========================================================")

        print("")

        print("Row #", personCount + 1, " | ID = ", personID, " | First Name = ", personFirstName, " | Last Name: ", personLastName, " | Street Number: ", personStreetNo, " | Street Name: ", personStreetName, " | City: ", personCity, " | State: ", personState, " | Zip Code: ", personZip, " | Phone #: ", personPhone, " | Salary: $", personSalary, "]\n")

    
    else:
        print("============================================================")
        print("")
        print("ERROR!\n")
        print("Enter correct selection @ CREATE Menu")
        print("")

# To print error messages for Main Option selections for 2-5
elif menuOptionMain == 2:
    print("[READ] Person Menu Option is currently unavailable.  Please try again later.")
    print("Sorry for the inconvinience.\n") 

elif menuOptionMain == 3:
    print("[UPDATE] Person Menu Option is currently unavailable.  Please try again later.")
    print("Sorry for the inconvinience.\n") 

elif menuOptionMain == 4:
    print("[DELETE] Person Menu Option is currently unavailable.  Please try again later.")
    print("Sorry for the inconvinience.\n") 

elif menuOptionMain == 5:
    print("[FIND] Person Menu Option is currently unavailable.  Please try again later.")
    print("Sorry for the inconvinience.\n")   

else:
    print("ERROR!\n")
    print("Enter @ Main Menu")
    print("")


print("Program has ended.\n")