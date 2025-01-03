from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog, QLabel
import subprocess

performance_script = "powerprofilesctl set performance"
balanced_script = "powerprofilesctl set balanced"
power_save_script = "powerprofilesctl set power-saver"
power_mode = "powerprofilesctl get"

def performance_button_clicked():
    subprocess.run(performance_script, shell=True)

def balanced_button_clicked():
    subprocess.run(balanced_script, shell=True)
    get_mode_button_clicked()

def power_save_button_clicked():
    subprocess.run(power_save_script, shell=True)
    get_mode_button_clicked()

def get_mode() -> str:
    res = subprocess.run(power_mode, shell=True, capture_output=True, text=True)
    out = res.stdout
    return out

def get_mode_button_clicked():
    mode = get_mode()

    new_window = QDialog()
    get_mode_layout = QVBoxLayout()
    label = QLabel(f"Your mode is {mode}")
    ok_button = QPushButton("ОК")

    new_window.setWindowTitle("Your mode")
    new_window.resize(300, 100)
    ok_button.clicked.connect(new_window.close)
    get_mode_layout.addWidget(label)
    get_mode_layout.addWidget(ok_button)
    new_window.setLayout(get_mode_layout)

    new_window.exec_()


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
performance_button = QPushButton("Set performance mode")
balanced_button = QPushButton("Set balanced mode")
power_save_button = QPushButton("Set power saver mode")
get_power_mode_button = QPushButton("Get power mode")

window.resize(400, 300)
window.setWindowTitle("Power Mods")
window.setWindowIcon(QIcon("source/icon.jpg"))
performance_button.clicked.connect(performance_button_clicked)
balanced_button.clicked.connect(balanced_button_clicked)
power_save_button.clicked.connect(power_save_button_clicked)
get_power_mode_button.clicked.connect(get_mode_button_clicked)
layout.addWidget(performance_button)
layout.addWidget(balanced_button)
layout.addWidget(power_save_button)
layout.addWidget(get_power_mode_button)
window.setLayout(layout)

window.show()
app.exec()