import flet as ft
from flet import TextField, Text, ElevatedButton, Column, Switch, Row, Dropdown, dropdown


def reverse_cipher(text):
    return text[::-1]

def caesar_cipher(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def rot13(text):
    return caesar_cipher(text, shift=13)


encryption_methods = {
    "Reverse Cipher": reverse_cipher,
    "Caesar Cipher": caesar_cipher,
    "ROT13": rot13,
}

def main(page: ft.Page):
    page.title = "Encryption Machine"

    
    encryption_dropdown = Dropdown(label="Select encryption method:",
                                   options=[dropdown.Option(text=method) for method in encryption_methods.keys()],
                                   value="Reverse Cipher",  
                                   on_change=lambda e: update_output())

    
    input_text = TextField(label="Enter your message:", multiline=True, autofocus=True)
    encrypt_switch = Switch(label="Encrypt", value=True, on_change=lambda e: update_output())
    output_text = Text(value="")
    copy_confirmation = Text(value="")

  
    def update_output():
        method = encryption_methods[encryption_dropdown.value]
        if encrypt_switch.value:
            output_text.value = method(input_text.value)
        else:
            output_text.value = "Decryption displayed directly: " + input_text.value
        page.update()


    def copy_to_clipboard(e):
        ft.clipboard.write_text(output_text.value)
        copy_confirmation.value = "Message copied to clipboard!"
        page.update()

    copy_button = ElevatedButton(text="Copy to Clipboard", on_click=copy_to_clipboard)

    page.add(Column([
        input_text,
        encryption_dropdown,
        encrypt_switch,
        output_text,
        Row([copy_button]),
        copy_confirmation
    ], spacing=10))

    update_output()

if __name__ == "__main__":
    ft.app(target=main)

















