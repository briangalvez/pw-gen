import sys, app
import pyperclip as pc
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class Window(QWidget): 

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(' ')
        self.setFixedSize(308, 190)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        group_box1 = QGroupBox('Strong Password Generator v1.2')
        main_layout.addWidget(group_box1)
        v_layout1 = QVBoxLayout()
        group_box1.setLayout(v_layout1)

        self.line_edit1 = QLineEdit()
        self.line_edit1.setObjectName('line_edit')
        self.line_edit1.setStyleSheet('#line_edit {color:black; background:white;}')
        v_layout1.addWidget(self.line_edit1)

        pw_length_list = ('8', '10', '12', '16', '20', '24', '30')
        self.pw_length_label = QLabel('Password length:')
        self.pw_length_combo_box = QComboBox()

        for item in pw_length_list:
            self.pw_length_combo_box.addItem(item)

        grid_layout1 = QGridLayout()
        v_layout1.addLayout(grid_layout1)
        grid_layout1.addWidget(self.pw_length_label, 0, 0)
        grid_layout1.addWidget(self.pw_length_combo_box, 0, 1)

        self.spl_char_label = QLabel('w/special character:')
        self.spl_char_checkbox = QCheckBox()

        grid_layout1.addWidget(self.spl_char_label, 0, 2)
        grid_layout1.addWidget(self.spl_char_checkbox, 0, 3)

        grid_layout2 = QGridLayout()
        v_layout1.addLayout(grid_layout2)
        self.copy_pw_btn = QPushButton('Copy Password')
        self.copy_pw_btn.clicked.connect(self.copy_to_clipboard)
        self.gen_pw_btn = QPushButton('Generate Password')
        self.gen_pw_btn.clicked.connect(self.generate_pw)

        grid_layout2.addWidget(self.copy_pw_btn, 0, 0)
        grid_layout2.addWidget(self.gen_pw_btn, 0, 1)

        self.save_pw_btn = QPushButton('Save Password as ".txt"')
        self.save_pw_btn.clicked.connect(self.save_pw)
        v_layout1.addWidget(self.save_pw_btn)

        self.line_edit1.setDisabled(True)
        self.copy_pw_btn.setDisabled(True)
        self.save_pw_btn.setDisabled(True)

    def generate_pw(self):
        self.copy_pw_btn.setDisabled(False)
        self.save_pw_btn.setDisabled(False)
        pw_length = int(self.pw_length_combo_box.currentText())
        special_char = self.spl_char_checkbox.isChecked()
        
        generated_pw = app.generate_pw(pw_length, special_char)
        self.line_edit1.setText(generated_pw)

    def copy_to_clipboard(self):
        gen_pw = self.line_edit1.text()

        pc.copy(gen_pw)
        pc.paste()

        msg_box = QMessageBox()
        msg_box.setWindowTitle('Message')
        msg_box.setText('Password copied to clipboard.')
        msg_box.exec()

    def save_pw(self):
        generated_pw = self.line_edit1.text()

        file_name = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text File (*.txt)')

        if file_name[0] != '':
            with open(file_name[0], 'w') as file:
                file.write(generated_pw)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    sys.exit(main())
