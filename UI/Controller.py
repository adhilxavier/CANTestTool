from PyQt5.QtWidgets import QApplication
from . import UI
from . import Model

# Controller
class CANTestAppUIController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.submit.clicked.connect(self.SubmitSettings)
        self.view.send.clicked.connect(self.SendCANdata)
        self.view.stop.clicked.connect(self.StopCANpackets)
        self.view.Settings1.mousePressEvent = self.ShowWindow1
        self.view.Settings2.mousePressEvent = self.ShowWindow2
        self.view.Settings3.mousePressEvent = self.ShowWindow3

    def SubmitSettings(self):
        self.AppendLog("Settings updating")

    def SendCANdata(self):
        self.AppendLog("Send Data")

    def StopCANpackets(self):
        self.AppendLog("Stop Data")
    
    def ShowWindow1(self, event):
        self.view.stacked_widget.setCurrentWidget(self.view.text_box_widget[0])
        self.AppendLog("Settings 1 selected")

    def ShowWindow2(self, event):
        self.view.stacked_widget.setCurrentWidget(self.view.text_box_widget[1])
        self.AppendLog("Settings 2 selected")

    def ShowWindow3(self, event):
        self.view.stacked_widget.setCurrentWidget(self.view.text_box_widget[2])
        self.AppendLog("Settings 3 selected")
    
    def AppendLog(self, message):
        self.view.log_box.append(message)

# Main Application
def run_ui():
   app = QApplication([])
   model = Model.CANTestAppUIModel()
   view = UI.CANTestAppUIView()
   controller = CANTestAppUIController(model, view)
   view.show()
   app.exec()