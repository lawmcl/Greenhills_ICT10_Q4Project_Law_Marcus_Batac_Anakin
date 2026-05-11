from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt


months = np.array(['Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May'])
attendance = np.array([0,0,0,0,0,0,0,0,0,0])

def draw_graph():
    
    plt.clf() 
    
    plt.figure(figsize=(8, 4))
    plt.plot(months, attendance, marker='o', linestyle='-', color='#7aa2ff')
    plt.title("Grade 10 Attendance Tracker")
    plt.xlabel("Months")
    plt.ylabel("Number of Absences")
    plt.grid(True, linestyle='--', alpha=0.6)

    # This updates the div with id="output"
    display(plt, target="output", append=False)
    plt.close()

def add_data(event):
 
    month_index = int(document.getElementById("month").value)
    

    absences_input = document.getElementById("absences")
    absences_value = absences_input.value


    if absences_value == "":
        return

 
    attendance[month_index] = int(absences_value)
    

    absences_input.value = ""


    draw_graph()


draw_graph()
