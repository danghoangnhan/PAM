from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog, QHBoxLayout, QLabel

class ConfirmDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Confirm")

        layout = QHBoxLayout()

        confirm_btn = QPushButton("Confirm", self)
        confirm_btn.clicked.connect(self.confirm)
        layout.addWidget(confirm_btn)

        cancel_btn = QPushButton("Cancel", self)
        cancel_btn.clicked.connect(self.cancel)
        layout.addWidget(cancel_btn)

        self.setLayout(layout)

    def confirm(self):
        self.accept()  # Closes the dialog and returns QDialog.Accepted

    def cancel(self):
        self.reject()  # Closes the dialog and returns QDialog.Rejected