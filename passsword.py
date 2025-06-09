import sys
import random
import string
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout,QMessageBox
#Build a password Generator GUI with python
class PasswordGeneratorApp(QWidget):
    def __init__(self):
         super().__init__()
         self.setWindowTitle('Password Generator')
         self.setup_ui() 
    def generate_password(self):
        length = (self.input_box.text())
        #logic to validate user input
        if length.isdigit():
            password_length = int(self.input_box.text())
            if password_length >=8 and password_length <=20:
                empty=[]
                for p in range(password_length):
                    x = random.choice(string.ascii_letters)
                    empty.append(x)
                    password = ''.join(empty)
                    self.password.setText(password)
            else:
                QMessageBox.warning(self,'Error!','Passwords must contain at least 8 to 20 characters!')
        else:
                QMessageBox.warning(self,'Error!','Enter a valid number')
        description_text = self.description_box.text()
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
        #connects the button to the Generate password function
        button.clicked.connect(self.generate_password)
        password_label = QLabel('Generated Password:')
        self.password = QLineEdit()
        save_btn = QPushButton('Save password')
        #connects the button to the Generate password function
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

