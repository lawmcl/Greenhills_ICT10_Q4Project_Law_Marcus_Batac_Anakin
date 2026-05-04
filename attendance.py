from pyscript import document, display
import numpy as np
import matplotlib.pyplot as plt

months = np.array(['Aug','Sept','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May'])
attendance = np.array([0,0,0,0,0,0,0,0,0,0])

def draw_graph():
    plt.figure()
    plt.bar(months, attendance)
    plt.title("Grade 10 Attendance Tracker")
    plt.xlabel("Months")
    plt.ylabel("Number of Absences")

    display(plt, target="output", append=False)
    plt.close()

def add_data(event):
    month_index = int(document.getElementById("month").value)
    absences = document.getElementById("absences").value

    if absences == "":
        return

    attendance[month_index] = int(absences)

    draw_graph()
