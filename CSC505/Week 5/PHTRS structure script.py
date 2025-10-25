# This UML is designed to show the flow for a User story of a citizen logging the occurence of a pothole into an online portal
# This portal will ask for and subesquently feed a database with contact infromation and key details about the pothole like location,
# size, specific damage caused, and $ estimate for that damage.  
# The database will queue according to district and repair priority waiting for the next available repair crew from that district
# to pick up the work order and complete the repair. Upon completion the repair crew will key completion details that will create a
# new entry into the Damage file that contains key information.

#Step 1 - Add contextual notes for design.

print("\n- program notes for Web-based Pothole Tracking and Repair System")
print("\n- Note 1: program makes multiple assumptions and is designed for early use prototyping")
print("\n- Note 2: program allows for two actors to input information (citizen and repair crew) that both feed into the repair system")

#Step 2 - Create the dictionary 'PHTRS_1' to store the different pages within the flow.

PHTRS_1 = {
    "1 PHTRS Display": ["Welcome to the Pothole Tracking and Repair Portal"],
    "2 Citizen Input": ["Please enter your contact information:> (cit name)> (home address)> (cit phone)"],
    "3 Public Works Dpt Repair Sys Database":["Citizen Entry created 'x' in database including (cit name) +(home address) +(cit phone)"],
    "4 PHTRS Display": ["I'm sorry (cit name) to hear about your experience. We're here to help."],
    "5 Citizen Input": ["Tell us more about the pothole please.> (pot address)> (size, scale 1-10)> (location, middle, curb, etc.)"],
    "6 Public Works Dpt Repair Sys Database": ["Pothole Entry Created 'y' associated with Citizen Entry 'x' from step 3 (pot address)",
                                               "+(size, scale 1-10) +(location, middle, curb, etc.)"],
    "7 PHTRS Display": ["We just have a few more questions (cit name). We'll get a crew to (pot address) to fix the pothole shortly."],
    "8 Citizen Input": ["What damage did you experience if any:> (type of damage)> ($ estimate of damage)"],
    "9 Public Works Dpt Repair Sys Database": ["Pothole entry 'y' is updated with (type of damage) +($ estimate of damage)"],
    "10 PHTRS Display": ["Thank you (cit name) for letting us know. We'll advise when the pothole at (pot address) is fixed."],
    "11 Public Works Dpt Repair Sys Database": ["Work Order 'z' is created with all attributes from 'y' then assigned repair priority 'q'",
                                                "based on (size, scale 1-10) and district (d) based on (pot address)"],
    "12 Public Works Dpt Repair Sys Database": ["Work Order 'z' is queued for Repair in Back End Work Portal System by priority (q)",
                                                "and district (d)"],
    "13 "


    "Display 2": ["Enter your name"],
    "User Input 2": ["User keys in name"],
    "Display 3": ["Please select your top 3 Personality Traits you have from the following list:"],
    "User Input 3": ["User keys integer (must be on list)"],
    "Display 4": ["Top 3 aggregated answers are displayed in descending order"]
    }

#Step 4 - Create the display function that prints the names and numbers of pages in the prototype
# in sequential order with each page number increasing with each step.

page_number = 1
for category, items in PHTRS_1.items():
    print(f"\n--- Page {page_number} ---")
    print(f"Page type: {category}")
    for item in items:
        print(item)
    page_number += 1

#Step 5 - Print total pages for design.
print("\n--- total pages in design ---")
print(page_number-1)