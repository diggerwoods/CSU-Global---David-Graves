# Step 1: Write a program that creates a dictionary containing course numbers and the room numbers 
 # of the rooms where the courses meet. Course Number : Room Number

room_number = {'CSC101': '3004', 'CSC102': '4501', 'CSC103': '6755', 'NET110': '1244', 'COM241': '1411'}

# Step 2: The program should also create a dictionary containing course numbers and the names of the
 # instructors that teach each course. Course Number : Instructor

instructor = {'CSC101': 'Haynes', 'CSC102': 'Alvarado', 'CSC103': 'Rich', 'NET110': 'Burke', 'COM241': 'Lee'}

# Step 3: The program should also create a dictionary containing course numbers and the meeting times
 # of each course. Course Number : Meeting Time

meeting_time = {'CSC101': '8:00 a.m.', 'CSC102': '9:00 a.m.', 'CSC103': '10:00 a.m.', 'NET110': '11:00 a.m.', 'COM241': '1:00 p.m.'}

# Step 4: The program should let the user enter a course number and then display the course's room number, instructor, and meeting time.

course_number = input('Enter course number:')
if course_number in room_number:
    print(f"Room number: {room_number[course_number]}")
    print(f"Instructor: {instructor.get(course_number, 'Unknown')}")
    print(f"Meeting Time: {meeting_time.get(course_number, 'Unknown')}")
else:
    print("Course number not found.")
          