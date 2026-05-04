from pyscript import display
from js import document
import numpy as np
import matplotlib.pyplot as plt

months = ['Aug','Sept','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May']

def generate_graph(month_index):
    plt.clf()

    days = np.arange(1, 31)  # 30 days
    daily_absences = np.random.randint(0, 2, size=30)  # 0 or 1 absence per day
    total_absences = np.cumsum(daily_absences)  # running total

    plt.plot(days, total_absences)
    plt.title(f"Grade 10 Attendance - {months[month_index]}")
    plt.xlabel("Days")
    plt.ylabel("Total Absences")

    display(plt, target="output", append=False)

def add_data(event):
    month_index = int(document.getElementById("month").value)
    generate_graph(month_index)

# show default graph (August)
generate_graph(0)
