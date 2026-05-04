from pyscript import document

def addStudent(event):
    name = document.getElementById("name").value

    if name == "":
        return

    li = document.createElement("li")
    li.textContent = "Hi! I am " + name

    document.getElementById("list").appendChild(li)

    document.getElementById("name").value = ""
