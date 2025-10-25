# Implement the YourLastName class using Python, which will prompt the user to input
# the key elements of the diagram and return these objects in a well-formatted output.

class YourLastName:
    def __init__(self):
        self.phases = []

    def create_diagram(self):
        # Prompt the user to input phases and actions within each phase, 
        # then store them in the 'phases' list.
        
        num_phases = int(input("Enter the number of phases in the diagram: "))
        for i in range(num_phases):
            phase_name = input(f"Enter phase {i+1} name: ")
            actions = []
            num_actions = int(input(f"Enter the number of actions in phase {i+1}: "))
            for j in range(num_actions):
                action = input(f"Enter action {j+1} description: ")
                actions.append(action)
            self.phases.append((phase_name, actions))

    def display_diagram(self):
        
        # Present the diagram in a well-formatted output.
       
        for phase, actions in self.phases:
            print(f"\nPhase: {phase}")
            for action in actions:
                print(f" - {action}")
        
diagram = YourLastName()
diagram.create_diagram()
diagram.display_diagram()
