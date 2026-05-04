from pyscript import document

def addStudent(event):
    name = document.getElementById("name").value.strip()

    if name == "":
        return

    list_el = document.getElementById("list")

    existing_names = [
        li.textContent.replace("Hi! I am ", "").strip().lower()
        for li in list_el.children
    ]

    # Prevent duplicates
    if name.lower() in existing_names:
        document.getElementById("name").value = ""
        return

    li = document.createElement("li")
    li.textContent = "Hi! I am " + name

    list_el.appendChild(li)

    # Clear input
    document.getElementById("name").value = ""
