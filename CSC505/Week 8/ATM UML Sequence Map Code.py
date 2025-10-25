# This UML is designed to show the steps including Card Validation via Pin entry
# entry that includes a guard where a card is ejected and returned if a counter is tripped
# with too many bad entries. If successful, however, the card is accepted, and the user chooses to
# withdraw money. If the money is available, it is dispersed and if the account balance is $0
# the account is closed. All the states above loop back to Idle to reset for the next customer.

#Step 1 - Add contextual notes for design.

print("\n- program notes")
print("\n- Note 1: program has guards in steps 4 and 7 that if criteria is met ends the transaction")

#Step 2 - Create the dictionary 'ATM_Sequence_Map' to store the different pages within the flow.

ATM_Sequence_Map = {
    "State 1": ["IDLE Welcome Screen"],
    "Action 1": ["Card Inserted"],
    "State 2": ["CARD Validation"],
    "Event 1": ["Valid Card: Proceed to State 3"],
    "Guard 1": ["Invalid Card: Eject card and proceed to State 9"],
    "State 3": ["Pin Entry Screen"],
    "Action 2": ["Pin Entered"],
    "State 4": ["Pin Reviewed"],
    "Event 2": ["Valid Pin: Proceed to State 5"],
    "Event 3": ["Invalid Pin: Allow to loop up to 3x, proceed to Guard 2 on 4th bad pin entry"],
    "Guard 2": ["Invalid Pin: Limit reached, Eject card and proceed to State 9"],
    "State 5": ["Menu Screen"],
    "Action 3": ["Withdrawal option selected"],
    "State 6": ["Amount entry screen"],
    "Action 4": ["Withdraw amount entered"],
    "State 7": ["Amount Reviewed"],
    "Guard 3": ["If account balance is $0, eject card and close account then proceed to State 9"],
    "Event 4": ["If amount accepted, dispense money, receipt and proceed to State 8"],
    "State 8": ["Thank you screen"],
    "Event 5": ["Eject card and proceed to State 9"],
    "State 9": ["Ext Screen"],
    "Event 6": ["Return to State 1"]
    }

#Step 3 - The following code create the display function that prints the pages from the ATM UML
# in sequential order with each page number increasing with each step.

page_number = 1
for category, items in ATM_Sequence_Map.items():
    print(f"\n--- Page {page_number} ---")
    print(f"Page type: {category}")
    for item in items:
        print(item)
    page_number += 1