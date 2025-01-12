from PyQt5.QtWidgets import QApplication
from . import UI
from . import Model

# Controller
class CANTestAppUIController:
    """
    Controller class for UI
    """
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
        """
        Submit button click event handler
        
        Parameters:
        self: instance of Controller class
        Returns:
        None
        """
        self.AppendLog("Settings updating")

    def SendCANdata(self):
        """
        Send button click event handler
        
        Parameters:
        self: instance of Controller class
        Returns:
        None
        """
        self.AppendLog("Send Data")

    def StopCANpackets(self):
        """
        Stop button click event handler
        
        Parameters:
        self: instance of Controller class
        Returns:
        None
        """
        self.AppendLog("Stop Data")
    
    def ShowWindow1(self, event):
        """
        Mouse press event for Settings1 label
        
        Parameters:
        self: instance of Controller class
        event :
        Returns:
        None
        """
        self.view.stacked_widget.setCurrentWidget(self.view.text_box_widget[0])
        self.AppendLog("Settings 1 selected")

    def ShowWindow2(self, event):
        """
        Mouse press event for Settings2 label
        
        Parameters:
        self: instance of Controller class
        event :
        Returns:
        None
        """
        self.view.stacked_widget.setCurrentWidget(self.view.text_box_widget[1])
        self.AppendLog("Settings 2 selected")

    def ShowWindow3(self, event):
        """
        Mouse press event for Settings3 label
        
        Parameters:
        self: instance of Controller class
        event :
        Returns:
        None
        """
        self.view.stacked_widget.setCurrentWidget(self.view.text_box_widget[2])
        self.AppendLog("Settings 3 selected")
    
    def AppendLog(self, message):
        """
        Message logging for TextEdit box
        
        Parameters:
        self: instance of Controller class
        message : log message 
        Returns:
        None
        """
        self.view.log_box.append(message)

# Main Application
def run_ui():
    """
    Run UI 
    
    Parameters:
    None
    Returns:
    None
    """
    app = QApplication([])
    model = Model.CANTestAppUIModel()
    view = UI.CANTestAppUIView()
    controller = CANTestAppUIController(model, view)
    view.show()
    app.exec()