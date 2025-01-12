from PyQt5.QtCore import pyqtSignal, QObject, Qt

# Model
class CANTestAppUIModel(QObject):
    counter_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._count = 0

    def increment(self):
        self._count += 1
        self.counter_changed.emit(self._count)