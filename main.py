from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout
)
from PyQt5.QtCore import Qt, QTimer
import sys
from gacha import automate_process

class BlueBlackUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ok = True
        self.setWindowTitle("Best Gacha Bot")
        self.resize(300, 200)

        # Set blue-black theme
        self.setStyleSheet("""
            QWidget {
                background-color: #1a1a2e;
                color: #eaeaea;
            }
            QPushButton {
                background-color: #0f3460;
                color: #eaeaea;
                border: 2px solid #16213e;
                border-radius: 8px;
                font-size: 16px;
                padding: 8px;
            }
            QPushButton:disabled {
                background-color: #3a3a5c;
                color: #9e9e9e;
            }
            QPushButton:hover {
                background-color: #16213e;
            }
            QLineEdit {
                background-color: #16213e;
                color: #eaeaea;
                border: 2px solid #0f3460;
                border-radius: 8px;
                padding: 5px;
                font-size: 14px;
            }
            QLabel {
                font-size: 16px;
            }
        """)

        # Layouts
        layout = QVBoxLayout()
        input_layout = QHBoxLayout()

        # Widgets
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.stop_button.setDisabled(True)  # Initially disabled

        # Connect buttons
        self.start_button.clicked.connect(self.start_clicked)
        self.stop_button.clicked.connect(self.stop_clicked)

        # Add widgets to layouts

        

        layout.addLayout(input_layout)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)

    def start_clicked(self):
        self.ok = True
        self.start_button.setDisabled(True)
        self.stop_button.setDisabled(False)
        automate_process()

    def stop_clicked(self):
        self.start_button.setDisabled(False)
        self.stop_button.setDisabled(True)
        print("Stopped")
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BlueBlackUI()
    window.show()
    sys.exit(app.exec_())
