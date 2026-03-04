import sys
from PyQt6.QtWidgets import QApplication, QCheckBox, QLabel, QListWidget, QListWidgetItem, QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt6 Investigation")
layout = QVBoxLayout()
label = QLabel("Hello, PyQt6!")
layout.addWidget(label)
button = QPushButton("Quit")
button.clicked.connect(app.quit)
layout.addWidget(button)
window.setLayout(layout)
window.show()
sys.exit(app.exec())


