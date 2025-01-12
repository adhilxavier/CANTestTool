from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,\
                            QLabel, QComboBox, QStackedWidget, QGroupBox,\
                            QHBoxLayout, QTextEdit, QVBoxLayout

from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtGui import QFont, QColor


def WidgetSetStyle(widget, r, g, b):
        # Define colors using QColor
    color_start = QColor(255, 255, 255)  # White
    color_end = QColor( r,g,b)    # Light Gray

    # Convert colors to hex strings
    start_color_hex = color_start.name()
    end_color_hex = color_end.name()
        # Check widget type using isinstance
    if isinstance(widget, QPushButton):
        print("Passed widget is QpushButton")
        widget_style = f"""
        QPushButton {{
            border: 2px solid gray;
            border-radius: 10px;
            margin-top: 15px;
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 {start_color_hex}, stop: 1 {end_color_hex}
            );
        }}
        QPushButton::title {{
            subcontrol-origin: margin;
            subcontrol-position: top center;
            padding: 0 3px;
            color: black;
        }}
        """
    elif isinstance(widget, QComboBox):
        print("Passed widget is QComboBox")

    elif isinstance(widget, QGroupBox):
        print("Passed widget is QGroupBox")
        widget_style = f"""
        QGroupBox {{
            border: 2px solid gray;
            border-radius: 10px;
            margin-top: 10px;
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 {start_color_hex}, stop: 1 {end_color_hex}
            );
        }}
        QGroupBox::title {{
            subcontrol-origin: margin;
            subcontrol-position: top center;
            padding: 0 3px;
            color: black;
        }}
        """
    else:
        print("Unknown widget type")

    widget.setStyleSheet(widget_style)

def SetupUI(view):
    # CAN Channel label and combo box
    group_box = QGroupBox("CAN Settings", view)
    # group_box.setStyleSheet("background-color: lightblue;")
    group_box.setGeometry(50, 50, 350, 680)  # Position and size of the group box

    font = QFont("Arial", 12, QFont.Bold)  # Font family, size, and bold
    group_box.setFont(font)
    # Apply a glossy background using QSS with QColor
    WidgetSetStyle(group_box, 204,204,204)

    # CAN Channel label and combo box
    view.ChannelLabel = QLabel(group_box)  # Parent is group_box
    view.ChannelLabel.setFont(QFont('Arial', 10, QFont.Bold))
    view.ChannelLabel.setText("Channel :")
    view.ChannelLabel.setStyleSheet("color: black;")
    view.ChannelLabel.move(10, 50)  # Position the label within the group box

    view.Chcombobox = QComboBox(group_box)  # Parent is group_box
    view.Chcombobox.setStyleSheet(
        "color: black; background-color: white;"
    )
    view.Chcombobox.setGeometry(180, 50, 100, 30)  # Position within the group box
    Channel_list = ["Channel 0", "Channel 1", "Channel 2"]
    view.Chcombobox.addItems(Channel_list)

    # Baudrate label and combo box
    view.BaudrateLabel = QLabel(group_box)  # Parent is group_box
    view.BaudrateLabel.setFont(QFont('Arial', 10, QFont.Bold))
    view.BaudrateLabel.setText("Baud rate:")
    view.BaudrateLabel.move(10, 100)  # Position the label within the group box
    view.BaudrateLabel.resize(view.BaudrateLabel.sizeHint())

    view.BRcombobox = QComboBox(group_box)  # Parent is group_box
    view.BRcombobox.setStyleSheet("color: black; background-color: white;")
    view.BRcombobox.setGeometry(180, 100, 100, 30)  # Position within the group box
    BR_List = ["500", "125"]
    view.BRcombobox.addItems(BR_List)

    # Bps label
    view.bpslabel = QLabel(group_box)  # Parent is group_box
    view.bpslabel.setText("kbps")
    view.bpslabel.resize(view.bpslabel.sizeHint())
    view.bpslabel.move(300, 110)  # Position within the group box

    #Buttons
    view.submit = QPushButton(group_box)
    view.submit.setText("SUBMIT")
    view.submit.move(180, 160)
    view.submit.setMinimumWidth(6 * 15)
    WidgetSetStyle(view.submit, 255, 255, 0)

    view.send = QPushButton(group_box)
    view.send.setText("SEND")
    view.send.move(110, 210)
    view.send.setMinimumWidth(6 * 15)
    WidgetSetStyle(view.send, 255, 0, 0)

    view.stop = QPushButton(group_box)
    view.stop.setText("STOP")
    view.stop.move(110, 250)
    view.stop.setMinimumWidth(6 * 15)
    WidgetSetStyle(view.stop, 255, 0, 0)
  
    # CAN Channel label and combo box
    Params_group_box = QGroupBox("Params Config", view)
    # group_box.setStyleSheet("background-color: lightblue;")
    Params_group_box.setGeometry(450, 50, 800, 680)  # Position and size of the group box
    font = QFont("Arial", 12, QFont.Bold)  # Font family, size, and bold
    Params_group_box.setFont(font)
    # Apply a glossy background using QSS with QColor
    WidgetSetStyle(Params_group_box, 204,204,204)

    # Create a QVBoxLayout for the entire GroupBox
    Params_group_box_layout = QVBoxLayout(Params_group_box)
    # Create a horizontal layout for the labels inside the group box
    settings_layout = QHBoxLayout(Params_group_box)
    # Create some labels that will act as buttons for navigation
    Settings1 = QLabel("Settings 1")
    Settings1.setStyleSheet("padding: 10px; background-color: lightgray; border-radius: 5px;")
    Settings1.setAlignment(Qt.AlignCenter)
    # Settings1.mousePressEvent = self.show_window1  # Connect the click event
    
    Settings2 = QLabel("Settings 2")
    Settings2.setStyleSheet("padding: 10px; background-color: lightgray; border-radius: 5px;")
    Settings2.setAlignment(Qt.AlignCenter)
    # Settings2.mousePressEvent = self.show_window2  # Connect the click event
    
    Settings3 = QLabel("Settings 3")
    Settings3.setStyleSheet("padding: 10px; background-color: lightgray; border-radius: 5px;")
    Settings3.setAlignment(Qt.AlignCenter)
    # Settings3.mousePressEvent = self.show_window3  # Connect the click event
    
    # Add labels to the settings_layout inside the group box
    settings_layout.addWidget(Settings1)
    settings_layout.addWidget(Settings2)
    settings_layout.addWidget(Settings3)
    
    # Add label layout to the group box layout
    Params_group_box_layout.addLayout(settings_layout)
    
    # Create a stacked widget to hold the content windows
    view.stacked_widget = QStackedWidget()
    
    # Create some windows to be displayed
    view.window1 = QLabel("This is the content for Settings 1")
    view.window2 = QLabel("This is the content for Settings 2")
    view.window3 = QLabel("This is the content for Settings 3")
    
    # Add windows to stacked_widget
    view.stacked_widget.addWidget(view.window1)
    view.stacked_widget.addWidget(view.window2)
    view.stacked_widget.addWidget(view.window3)
    
    # Add the stacked widget to the group box layout (content area)
    Params_group_box_layout.addWidget(view.stacked_widget)
    # Create the log box (QTextEdit)
    view.log_box = QTextEdit()
    view.log_box.setReadOnly(True)  # Make the log box read-only so the user can't modify it
    view.log_box.setStyleSheet("border: 1px solid gray; background-color: #f0f0f0; padding: 10px;")
    
    # Add the log box to the group box layout
    Params_group_box_layout.addWidget(view.log_box)
    

# View
class CANTestAppUIView(QMainWindow):
    def __init__(self):
        super().__init__()
        # Define colors using QColor
        bg_color_start = QColor(255, 255, 255)  # White
        bg_color_end = QColor(224, 255, 255)    # Light Gray

        # Convert colors to hex strings
        start_bg_color_hex = bg_color_start.name()
        end_bg_color_hex = bg_color_end.name()
        self.setWindowTitle("CAN TestTool")
        self.resize(1280, 768)  # Set the window size
            # Apply a glossy background using QSS with QColor
        self.setStyleSheet(f"""
            QMainWindow {{
                border: 2px solid gray;
                border-radius: 10px;
                margin-top: 10px;
                background: qlineargradient(
                    spread: pad, x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 {start_bg_color_hex}, stop: 1 {end_bg_color_hex}
                );
            }}
            QMainWindow::title {{
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 3px;
                color: black;
            }}
        """)
        # self.setStyleSheet("background-color: lightyellow;") 
        SetupUI(self)
