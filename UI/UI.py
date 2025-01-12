from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,\
                            QLabel, QComboBox, QStackedWidget, QGroupBox,\
                            QHBoxLayout, QTextEdit, QVBoxLayout, QLineEdit, QWidget, QGridLayout

from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtGui import QFont, QColor

class TextBoxWidget(QWidget):
    """
    This a class for TextBox group widget.
    """
    def __init__(self, title):
        super().__init__()
        layout = QVBoxLayout()
        
        # Add a title label
        title_label = QLabel(title)
        title_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title_label)
        
        # Create a grid layout for text boxes and labels
        grid_layout = QGridLayout()
        page1_row1 = ["System state", "Target speed", "Feedback speed"]
        page1_row2 = ["Speed Command Source", "Target torque", "Feedback speed"]
        page1_label = [page1_row1, page1_row2]
        page2_row1 = ["System", "Target", "Feedback"]
        page2_row2 = ["Speed Command", "Torque", "Speed"]
        page2_label = [page2_row1, page2_row2]
        page3_row1 = ["Module state", "Running mode", "Module Temperatue"]
        page3_row2 = ["Resolver angle", "Bus current", "Bus voltage"]
        page3_label = [page3_row1, page3_row2]
        page_label = [page1_label, page2_label, page3_label]

        if title == "Page1":
          item = 0
        elif title == "Page2":
          item = 1
        elif title == "Page3":
          item = 2
        
        # Add labels and text boxes in 2 rows and 3 columns
        for row in range(2):
            for col in range(3):
                label = QLabel(page_label[item][row][col])
                text_box = QLineEdit()
                grid_layout.addWidget(label, row * 2, col)  # Place the label
                grid_layout.addWidget(text_box, row * 2 + 1, col)  # Place the textbox below the label

        # Adjust spacing
        grid_layout.setHorizontalSpacing(110)
        grid_layout.setVerticalSpacing(30)
        grid_layout.setContentsMargins(10, 10, 10, 10)  # Left, Top, Right, Bottom
        
        layout.addLayout(grid_layout)
        self.setLayout(layout)

def WidgetSetStyle(widget, r, g, b):
    """
    This function set style sheet for widgets.
    Currently supports only for button and Groupbox
    
    Parameters:
    widget (Qwidget): widget class.
    r (int): Red pixel level.
    g (int): Green pixel level.
    b (int): Blue pixel level.
    Returns:
    None
    """
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
        """
    else:
        print("Unknown widget type")

    widget.setStyleSheet(widget_style)

def SetupUI(view):
    """
    This function set style sheet for widgets.
    Currently supports only for button and Groupbox
    
    Parameters:
    view: UI view class.
    Returns:
    None
    """
    # CAN Channel label and combo box
    group_box = QGroupBox("CAN settings", view)
    group_box.setGeometry(50, 50, 350, 480)  # Position and size of the group box

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
    view.submit.setFixedSize(100, 50)
    view.submit.setText("SUBMIT")
    view.submit.move(180, 160)
    view.submit.setMinimumWidth(6 * 15)
    WidgetSetStyle(view.submit, 255, 255, 0)

    view.send = QPushButton(group_box)
    view.send.setFixedSize(100, 50)
    view.send.setText("SEND")
    view.send.move(110, 210)
    view.send.setMinimumWidth(6 * 15)
    WidgetSetStyle(view.send, 255, 0, 0)

    view.stop = QPushButton(group_box)
    view.stop.setFixedSize(100, 50)
    view.stop.setText("STOP")
    view.stop.move(110, 250)
    view.stop.setMinimumWidth(6 * 15)
    WidgetSetStyle(view.stop, 255, 0, 0)
  
    # CAN Channel label and combo box
    Params_group_box = QGroupBox("Parameter Settings", view)
    # group_box.setStyleSheet("background-color: lightblue;")
    Params_group_box.setGeometry(450, 50, 800, 480)  # Position and size of the group box
    font = QFont("Arial", 12, QFont.Bold)  # Font family, size, and bold
    Params_group_box.setFont(font)
    # Apply a glossy background using QSS with QColor
    WidgetSetStyle(Params_group_box, 204,204,204)

    view.Settings1 = QLabel(Params_group_box)
    view.Settings1.setText("Settings 1")
    view.Settings1.setStyleSheet("padding: 10px; background-color: lightgreen; border-radius: 5px;")
    view.Settings1.move(50, 50)
    
    view.Settings2 = QLabel(Params_group_box)
    view.Settings2.setText("Settings 2")
    view.Settings2.setStyleSheet("padding: 10px; background-color: lightgreen; border-radius: 5px;")
    view.Settings2.move(150, 50)
    
    view.Settings3 = QLabel(Params_group_box)
    view.Settings3.setText("Settings 3")
    view.Settings3.setStyleSheet("padding: 10px; background-color: lightgreen; border-radius: 5px;")
    view.Settings3.move(250, 50)

    view.Settings4 = QLabel(Params_group_box)
    view.Settings4.setText("Settings 4")
    view.Settings4.setStyleSheet("padding: 10px; background-color: lightgreen; border-radius: 5px;")
    view.Settings4.move(350, 50)
    
    view.Settings5 = QLabel(Params_group_box)
    view.Settings5.setText("Settings 5")
    view.Settings5.setStyleSheet("padding: 10px; background-color: lightgreen; border-radius: 5px;")
    view.Settings5.move(450, 50)

    view.Settings6 = QLabel(Params_group_box)
    view.Settings6.setText("Settings 6")
    view.Settings6.setStyleSheet("padding: 10px; background-color: lightgreen; border-radius: 5px;")
    view.Settings6.move(550, 50)

    view.Settings7 = QLabel(Params_group_box)
    view.Settings7.setText("Settings 7")
    view.Settings7.setStyleSheet("padding: 10px; background-color: lightgreen; border-radius: 5px;")
    view.Settings7.move(650, 50)
    # Create a stacked widget to hold the content windows
    view.stacked_widget = QStackedWidget(Params_group_box)
    view.text_box_widget = []

    for i in range(3):
      view.text_box_widget.append(TextBoxWidget(f"Page{i + 1}"))
      view.stacked_widget.addWidget(view.text_box_widget[i])
    view.stacked_widget.move(50, 200)
    
    # Add the stacked widget to the group box layout (content area)
    view.log_box = QTextEdit(view)
    view.log_box.setGeometry(50, 550, 1200, 180)
    view.log_box.setReadOnly(True)  # Make the log box read-only so the user can't modify it
    view.log_box.setStyleSheet("border: 1px solid gray; background-color: #ffffff; padding: 10px;")
    

# View
class CANTestAppUIView(QMainWindow):
    """
    This class is for the UI view
    """
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
        # self.resize(1920, 1080)
        # Apply a glossy background using QSS with QColor
        self.setStyleSheet(f"""
            QMainWindow {{
                border: 2px solid #4CAF50;;
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

        SetupUI(self)
