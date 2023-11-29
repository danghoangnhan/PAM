from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize

class SquareButton(QPushButton):
    def __init__(self, icon, parent=None):
        super().__init__(icon, "", parent)

    def sizeHint(self):
        size = super(SquareButton, self).sizeHint()
        dimension = max(size.width(), size.height())
        return QSize(dimension, dimension)
