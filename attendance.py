from pyscript import display
import random
import matplotlib.pyplot as plt

months = ['Aug','Sept','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May']
days = ['Monday','Tuesday','Wednesday','Thursday','Friday']

def show_absence(event):
    month_index = int(document.getElementById("month").value)
    day_index = int(document.getElementById("day").value)

    absences = random.randint(0, 5)

    display("", target="output", append=False)

    display(
        f"{days[day_index]} of {months[month_index]}: {absences} absences",
        target="output",
        append=True
    )

    # show graph
    plt.clf()
    plt.bar([days[day_index]], [absences])
    plt.title(f"{days[day_index]} - {months[month_index]}")
    plt.ylabel("Absences")

    display(plt, target="output", append=True)
