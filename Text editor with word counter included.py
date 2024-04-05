#heilliesantana
import flet as ft
from flet import TextField, Column, Row, ElevatedButton, Text

def main(page: ft.Page):
    def update_word_count(event=None):
        words = len(text_field.value.split())
        word_count.value = f"Word count: {words}"
        page.update()

    def create_file(e):
        text_field.value = ""
        feedback_text.value = "New file created."
        update_word_count()

    def open_file(e):
        file_name = filename_field.value.strip()
        if file_name:
            try:
                with open(file_name, "r", encoding="utf-8") as file:
                    text_field.value = file.read()
                update_word_count()
                feedback_text.value = "File opened successfully."
            except FileNotFoundError:
                feedback_text.value = "File not found."

    def save_file(e):
        file_name = filename_field.value.strip()
        if file_name:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(text_field.value)
            feedback_text.value = "File saved successfully."

    text_field = TextField(expand=True, multiline=True, autofocus=True, on_change=update_word_count)
    word_count = Text("Word count: 0")
    filename_field = TextField(label="File Name", width=300)
    feedback_text = Text(value="", color="green")

    create_btn = ElevatedButton(text="Create", on_click=create_file)
    open_btn = ElevatedButton(text="Open", on_click=open_file)
    save_btn = ElevatedButton(text="Save", on_click=save_file)

    controls_row = Row([create_btn, open_btn, save_btn, filename_field])
    feedback_row = Row([feedback_text], alignment="start")
    editor_column = Column([controls_row, feedback_row, text_field, word_count], expand=True)

    page.add(editor_column)

if __name__ == "__main__":
    ft.app(target=main)

