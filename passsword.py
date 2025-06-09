import sys
import random
import string
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout
#Build a password Generator GUI with python
class PasswordGeneratorApp(QWidget):
    def __init__(self):
         super().__init__()
         self.setWindowTitle('Password Generator')
         self.setup_ui() 
    def generate_password(self):
        password_length = int(self.input_box.text())
        print(password_length)
        description_text = self.description_box.text()
        print(description_text)
        empty = []
        for p in range(password_length):
            x = random.choice(string.ascii_letters)
            empty.append(x)
        password = ''.join(empty)
        self.password.setText(password)
        print(password)
    def save_password(self):
        password = self.password.text()
        description = self.description_box.text()
        with open('password.txt','a') as file:
            file.write(f'{description} : {password}\n')
    def setup_ui(self):
        layout = QVBoxLayout()
        label = QLabel('Enter a password length: ')
        self.input_box = QLineEdit()
        description = QLabel('Description (optional):')
        self.description_box = QLineEdit()
        button = QPushButton('Generate password')
        button.clicked.connect(self.generate_password)
        password_label = QLabel('Generated Password:')
        self.password = QLineEdit()
        save_btn = QPushButton('Save password')
        button.clicked.connect(self.save_password)
        layout.addWidget(label)
        layout.addWidget(self.input_box)
        layout.addWidget(description)
        layout.addWidget(self.description_box)
        layout.addWidget(button)
        layout.addWidget(password_label)
        layout.addWidget(self.password)
        layout.addWidget(save_btn)
        self.setLayout(layout)
event = QApplication(sys.argv)
password_generator = PasswordGeneratorApp()
password_generator.show()
event.exec()

