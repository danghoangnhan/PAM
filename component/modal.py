from PyQt6.QtWidgets import QPushButton, QDialog, QHBoxLayout,QLabel,QVBoxLayout

class ConfirmDialog(QDialog):
    def __init__(self,message, parent=None):
        super().__init__(parent)
        self.message = message
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Confirm")
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.message_label = QLabel(self.message, self)  # Label to display the message
        main_layout.addWidget(self.message_label)
        confirm_btn = QPushButton("Confirm", self)
        confirm_btn.clicked.connect(self.confirm)
        button_layout.addWidget(confirm_btn)

        cancel_btn = QPushButton("Cancel", self)
        cancel_btn.clicked.connect(self.cancel)
        button_layout.addWidget(cancel_btn)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def confirm(self):
        self.accept()

    def cancel(self):
        self.reject()