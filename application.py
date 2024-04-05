import flet as ft
import json
from datetime import datetime


DATA_FILE = 'classroom_data.json'

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            
            for classroom in data.values():
                for assignment in classroom["assignments"]:
                    assignment["due_date"] = datetime.strptime(assignment["due_date"], '%Y-%m-%d')
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  

def save_data(data):
    with open(DATA_FILE, 'w') as f:
       
        json.dump(data, f, indent=4, default=lambda x: x.strftime('%Y-%m-%d') if isinstance(x, datetime) else x)

classrooms = load_data()

def main(page: ft.Page):
    page.title = "Classroom Manager"
    show_classroom_management_ui(page)

def show_classroom_management_ui(page):
    page.update()
    page.controls.clear()
    classroom_name_input = ft.TextField(label="Classroom Name", width=300)
    add_classroom_btn = ft.ElevatedButton(text="Add Classroom", on_click=lambda e: add_classroom(page, classroom_name_input))
    
    for classroom_name in classrooms:
        page.add(ft.ElevatedButton(text=f"View {classroom_name} Details", on_click=lambda e, cn=classroom_name: show_classroom_details_ui(page, cn)))

    page.add(classroom_name_input, add_classroom_btn)

def add_classroom(page, classroom_name_input):
    classroom_name = classroom_name_input.value
    if classroom_name and classroom_name not in classrooms:
        classrooms[classroom_name] = {"students": [], "assignments": []}
        classroom_name_input.value = ""
        save_data(classrooms)  
    else:
        page.show_dialog(ft.AlertDialog(title="Error", content=ft.Text("Classroom already exists or name is invalid.")))
    show_classroom_management_ui(page)

def show_classroom_details_ui(page, classroom_name):
    page.controls.clear()
    
    student_name_input = ft.TextField(label="Student Name", width=300)
    add_student_btn = ft.ElevatedButton(text="Add Student", on_click=lambda e: add_student_to_classroom(page, classroom_name, student_name_input))

    assignment_name_input = ft.TextField(label="Assignment Name", width=300)
    due_date_input = ft.TextField(label="Due Date (YYYY-MM-DD)", width=300)
    add_assignment_btn = ft.ElevatedButton(text="Add Assignment", on_click=lambda e: add_assignment_to_classroom(page, classroom_name, assignment_name_input, due_date_input))
    
    
    students_title = ft.Text(value="Students:")
    assignments_title = ft.Text(value="Assignments:")
    students_list = [ft.Text(value=student) for student in classrooms[classroom_name]["students"]]
    assignments_list = [ft.Text(value=f"{assignment['name']} - Due: {assignment['due_date'].strftime('%Y-%m-%d')}") for assignment in classrooms[classroom_name]["assignments"]]

    back_btn = ft.ElevatedButton(text="Back", on_click=lambda e: show_classroom_management_ui(page))

    page.add(students_title, *students_list, assignments_title, *assignments_list, student_name_input, add_student_btn, assignment_name_input, due_date_input, add_assignment_btn, back_btn)
    page.update()

def add_student_to_classroom(page, classroom_name, student_name_input):
    student_name = student_name_input.value
    if student_name:
        classrooms[classroom_name]["students"].append(student_name)
        student_name_input.value = ""
        save_data(classrooms)  
    show_classroom_details_ui(page, classroom_name)

def add_assignment_to_classroom(page, classroom_name, assignment_name_input, due_date_input):
    assignment_name = assignment_name_input.value
    due_date_str = due_date_input.value
    try:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
        classrooms[classroom_name]["assignments"].append({"name": assignment_name, "due_date": due_date})
        assignment_name_input.value, due_date_input.value = "", ""
        save_data(classrooms)  
    except ValueError:
        page.show_dialog(ft.AlertDialog(title="Error", content=ft.Text("Invalid date format. Please use YYYY-MM-DD.")))
    show_classroom_details_ui(page, classroom_name)

if __name__ == "__main__":
    ft.app(target=main)






#https://api.flutter.dev/flutter/material/ElevatedButton-class.html
#https://flet.dev/docs/controls/datepicker/
#https://localizely.com/flat-json-file/?tab=react-intl






