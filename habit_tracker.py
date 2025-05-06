import tkinter as tk 
from datetime import datetime

# Initiates rules 
xp_per_level = 100
completed_today = []
today = datetime.now().strftime("%A, %B %d, %Y")

habits = {"Drink 1 Glass of Water": 10,
          "Read for 30 min": 20, 
          "Exercise": 20, 
          "Full Night Sleep": 30, 
          "Eat Healthy Meal": 15,
          "Meditate for 10 minutes": 20 
          }

xp = 0
level = 1
completed_habits = {}

# function to reset the day
def reset():
    # restarts at the start of theday 
    completed_today.clear()
    for habit in completed_habits.values():
        habit.set(False)
    status_label.config(text="New Day!")
    list_label.config(text="")

# function to calculate the xp from a habit 
def complete_habit():
    global xp, level 
    earned_xp = 0

    # habits that are checked are put into completed_habits 
    for habit, var in completed_habits.items():
        if var.get():
            #gets the correlated value from the habits dict and calc. adds it to completed_today 
            earned_xp += habits[habit]
            completed_today.append(habit)
            var.set(False)

    xp += earned_xp
    level = xp // xp_per_level + 1

    # Displays how much XP, Level, and How much XP was given 
    xp_label.config(text=f"XP: {xp}", font=("Arial", 12))
    level_label.config(text=f"Level: {level}", font=("Arial", 12))
    status_label.config(text=f"Nice Work! +{earned_xp} XP", font=("Arial", 12))
    # Calls function that shows all completed habits 
    show_completed_habits()

# shows completed habits that day. resets each day. 
def show_completed_habits():
    if completed_today:
        completed_texts = [f"{habit} (+{habits[habit]} XP)" for habit in completed_today]
        list_label.config(text="Completed: \n" + "\n".join(completed_texts), font=("Arial", 8))
    else:
        list_label.config(text="No Habits completed yet", font=("Arial", 8))

# GUI created through #tkinter
# creates the root info and the size of the app 
root = tk.Tk()
root.title("Habit Tracker")
root.geometry("300x500")

# header (title and date)
tk.Label(root, text="Daily Habits", font=("Arial", 12, "bold")).pack(pady=10)
tk.Label(root, text=f"Todays date: \n {today}", font=("Arial", 12)).pack(pady=10)

# shows the habit check mark icons with XP 
for habit in habits:
    var = tk.BooleanVar()
    completed_habits[habit] = var
    tk.Checkbutton(root, text=f"{habit} (+{habits[habit]} XP)", variable=var, font=("Arial", 10)).pack(anchor="w")

# buttons for reset and complete habits (calls the functions from above) 
tk.Button(root, text="Complete Habits", command=complete_habit).pack(pady=10)
tk.Button(root, text="Start a New Day!", command=reset).pack(pady=5)

# instantiates the labels from above to showcase information 
xp_label = tk.Label(root, text="XP: 0")
xp_label.pack()

level_label = tk.Label(root, text="Level: 1")
level_label.pack()

list_label = tk.Label(root, text="")
list_label.pack()

status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=10)

# runs the program 
root.mainloop()

