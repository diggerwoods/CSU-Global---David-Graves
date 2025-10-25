def print_use_case_diagram():
   # This script prints a simple use case diagram with multiple actors and systems and their interactions/functionality.
   # The first few 'print' lines follow the description and provide workflow notes

    print("\n--Workflow Notes--")
    print("If Status is updated by Repair Crew as '(1)Work In Progress' in Step 17, the system loops",
          "\nfrom Step 18 back to Step 16 until one of the other Status updates (2-4) is made, then it proceeds",
          "\nto Step 19.")

   # The following 'print' lines define the actors

    print("\nActors & Systems:")
    print("- Citizen")
    print("- Repair Crew")
    print("- 'PWDRSD' Public Works Department Repair System Database")
    print("- 'PHTRS' Pothole Tracking and Repair System Display")
    print("- 'WP' Work Portal System Display")

   # The following 'print' lines share a typical use case

    print("\nUse Case 1a:")
    print("- Citizen:")
    print(" Step 1 - Searches for and finds PHTRS system to report a pothole")
    print(" Step 2 - Enters: Name + Home Address + Phone number in PHTRS")
    print("- PWDRSD:")
    print(" Step 3 - Citizen Entry created 'x' in database with info from Step 2")
    print("- PHTRS:")
    print(" Step 4 - System prompts Citizen for more information")
    print("- Citizen:")
    print(" Step 5 - Enters: pothole address + size on a scale 1-10 + location as 'middle, curb, etc.'")
    print("- PWDRSD:")
    print(" Step 6 - Pothole Entry Created 'y' associated with Citizen Entry 'x' from step 3")
    print("- PHTRS:")
    print(" Step 7 - System prompts Citizen for more information")
    print("- Citizen:")
    print(" Step 8 - Enters: type of damage + $ estimate of damage")  
    print("- PWDRSD:")
    print(" Step 9 - Pothole Entry 'y' is updated with information from step 8")
    print("- PHTRS:")
    print(" Step 10 - System thanks citizen, and provides next steps follow up") 
    print("- PWDRSD:")
    print(" Step 11 - Work Order 'z' is created with all attributes from 'y' then",
          "\n   assigned repair priority based on size and district based on pothole address")
    print(" Step 12 - Work Order 'z' is queued for Repair in Work Portal System")
    print("\nUse Case 1b:")
    print("- WP:")
    print(" Step 13 - Welcome screen for Repair Crew that prompts login and Work Order selection")
    print("- Repair Crew")
    print(" Step 14 - Enters: repair crew id# + # of people on crew + equip assigned + Work order 'z')")
    print("- PWDRSD:")
    print(" Step 15 - Work Order 'z' is updated with new input from Step 14")
    print("- WP:")
    print(" Step 16 - Acknowledges work assigned and prompts Repair Crew for status update")
    print("- Repair Crew")
    print(" Step 17 - Enters: status update from list 1-4")
    print("- PWDRSD:")
    print(" Step 18 - Work Order 'z' is updated with status from Step 17 and email sent with update to Citizen.")
    print("- WP:")
    print(" Step 19 - Thanks Repair Crew for work completed and prompts for more information")
    print("- Repair Crew")
    print(" Step 20 - Enters: hrs applied to repair + amount of filler used")
    print("- PWDRSD:")
    print(" Step 21 - Work Order 'z' is updated with information from Step 20")
    print(" Step 22 - Cost of repair assigned to 'z' as: (hrs applied to repair) x (# of people on crew)",
          "\n   x (equip assigned) x (amount of filler used")
    print(" Step 23 - Damage file is created containing citizen information and type and $ estimate of damage")

# Description of the online program
print("**Description of program, actors, and use case for Web-based Pothole Tracking and Repair System**")
print("\nCitizens can log onto a website and report the location and severity of potholes. As potholes") 
print("are reported, they are logged within a 'public works department repair system' and are")
print("assigned an identifying number, stored by street address, size (on a scale of 1 to 10), location")
print("(middle, curb, etc.), district (determined from street address), and repair priority (determined")
print("from the size of the pothole).")
print("\nWork order data are associated with each pothole and include pothole location and size,")
print("repair crew identifying number, number of people on crew, equipment assigned, hours")
print("applied to repair, hole status (work in progress, repaired, temporary repair, not repaired),") 
print("amount of filler material used, and cost of repair (computed from hours applied, number of") 
print("people, material and equipment used).")
print("\nFinally, a damage file is created to hold information about reported damage due to the") 
print("pothole and includes the citizen's name, address, phone number, type of damage, and dollar") 
print("amount of damage. PHTRS is an online system; all queries are to be made interactively.") 

# Run the function to print the program description
print_use_case_diagram()