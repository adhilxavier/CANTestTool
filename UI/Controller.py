from PyQt5.QtWidgets import QApplication
from . import UI
from . import Model

# Controller
class CANTestAppUIController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_view(self, count):
        self.tmp = 0
      #   self.view.
      #   self.view.label.setText(str(count))

# Main Application
def run_ui():
   app = QApplication([])
   model = Model.CANTestAppUIModel()
   view = UI.CANTestAppUIView()
   controller = CANTestAppUIController(model, view)
   view.show()
   app.exec()