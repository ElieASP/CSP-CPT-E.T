import time
import sys #find system of computer to adapt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel #dowload essentials of PYQT5
from PyQt5.QtCore import QDate



#ADD POMODORO/FEYNMAN TECHNIQUE AS A SUGGESTION

print("Welcome to the Schedule Planner!")
print("Enter your tasks, and we'll help you ace your exams")
print("ATTENTION, this schedule algorithm works best for last minute study sessions.")

# Initialize task list
tasks = []

# Get user input for tasks
while True:
    print("Add a new task:")
    name = input("Task name: ")
    priority = int(input("Priority (1 = High, 2 = Medium, 3 = Low): "))
    due_date = int(input("Days until due date: "))
    hours_needed = float(input("Total hours needed to complete: "))
    
    # Append the task as a dictionary
    tasks.append({
        "name": name,
        "priority": priority,
        "due_date": due_date,
        "hours_needed": hours_needed
    })
    
    add_more = input("Do you want to add another task? (yes/no): ")
    if add_more != "yes":
        break

# Get available hours per day
hours_per_day = float(input("\nHow many hours can you study per day? "))

#Number of pomodors
minutes_needed = hours_needed * 60 
amount_pomodoro = round(minutes_needed / 25,1)

# Calculate task importance
for task in tasks:
    # Higher priority and shorter due dates increase weight
    task["weight"] = (3 - task["priority"]) * 2 + (1 / max(task["due_date"], 1))


# Allocate study hours per day for each task
print("\nYour Daily Study Schedule:")
total_weight = sum(task["weight"] for task in tasks)

for task in tasks:
    daily_hours = (task["weight"] / total_weight) * hours_per_day
    days_to_study = task["hours_needed"] / daily_hours if daily_hours > 0 else "N/A"
    
    print(f"- Task: {task['name']}")
    print(f"  Priority: {task['priority']} (1 = High, 3 = Low)")
    print(f"  Due in: {task['due_date']} days")
    print(f"  Study Time: {daily_hours:.2f} hours/day")
    print(f"  Amount of pomodors: {amount_pomodoro}")
    print(f"  Estimated Days to Finish: {round(days_to_study, 1) if isinstance(days_to_study, float) else days_to_study}")
    
    # Add feasibility check
    if isinstance(days_to_study, float) and days_to_study > task["due_date"]:
        print("WARNING: Not enough time allocated to finish this task before the due date!")
    
    print()  # Blank line between tasks
print("We suggest you study with two different types of techniques depending on the subject and preference:"
"   1. Feynman Technique: select your concept, map your knowledge, teach it to a 12 year old, review and refine, test."
"   2. Pomodoro Technique: decide on the task, set the Pomodoro timer (typically 25 min), study for that time, take a 5-10 min break, after 4 rounds, take a 20 min break, restart the process")
print("Plan your study time with the techniques and structure your mind with the interface which popped up, good luck!")


time.sleep(15)
class CalendarApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Create calendar widget
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)

        # Create label to display selected date
        self.label = QLabel(self)
        self.label.setStyleSheet("font-size: 18px; margin-top: 10px;")

        layout.addWidget(self.calendar)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 Calendar')
        self.setGeometry(200, 200, 900, 600)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalendarApp()
    ex.show()
    sys.exit(app.exec_())


