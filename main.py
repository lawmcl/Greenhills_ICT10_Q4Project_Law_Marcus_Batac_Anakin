from pyscript import document

def addStudent(event):
    name = document.getElementById("name").value.strip()
    section = document.getElementById("section").value

    if name == "":
        return

    list_el = document.getElementById("list")

    existing_entries = [
        li.textContent.lower()
        for li in list_el.children
    ]

    new_entry = f"hi im {name} and im from {section}".lower()

    if new_entry in existing_entries:
        document.getElementById("name").value = ""
        return

    li = document.createElement("li")

    li.textContent = f"Hi Im {name} and im from {section}"

    list_el.appendChild(li)

    document.getElementById("name").value = ""
