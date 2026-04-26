from pyscript import display
import numpy as np
import matplotlib.pyplot as plt

# data
months = np.array(['Aug','Sept','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May'])
attendance = np.array([0,0,0,0,0,0,0,0,0,0])

# draw graph
def sample_graph():
    plt.clf()
    plt.bar(months, attendance)
    plt.title("Grade 10 Attendance Tracker")
    plt.xlabel("Months")
    plt.ylabel("Number of Absences")
    display(plt, target="output", append=False)

# button function
def add_data(event):
    month_index = int(document.getElementById("month").value)
    absences = document.getElementById("absences").value

    if absences == "":
        return

    attendance[month_index] = int(absences)
    sample_graph()

# show graph at start
sample_graph()