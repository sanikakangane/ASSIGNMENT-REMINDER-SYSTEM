# Assignment Reminder System

print("Assignment Reminder System.")
print("Type 'done' when you have submitted your assignment.")

while True:
    answer = input("Have you submitted your assignment?: ")

    if answer.lower() == "done":
        print("Great!!! Your assignment has been submitted.")
        print("Reminder system stopped.")
        break
    else:
        print("Still waiting...")
