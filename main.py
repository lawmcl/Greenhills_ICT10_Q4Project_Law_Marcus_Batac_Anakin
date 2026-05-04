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

    new_entry = f"hi! i'm {name} from {section}".lower()

    if new_entry in existing_entries:
        document.getElementById("name").value = ""
        return

    li = document.createElement("li")
    li.textContent = f"Hi! I'm {name} from {section}"

    list_el.appendChild(li)

    document.getElementById("name").value = ""
