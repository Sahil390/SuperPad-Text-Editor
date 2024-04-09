import openai
from PyQt5 import QtWidgets, QtGui

openai.api_key = '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'

class ChatWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Chatbot")
        self.setup_ui()

    def setup_ui(self):
        self.chatbox = QtWidgets.QTextEdit(self)
        self.chatbox.setReadOnly(True)
        self.chatbox.setFixedSize(1000, 400)  # Increase the size to 1000x400
        self.chatbox.setFontPointSize(12)  # Increase the font size to 12

        self.entry = QtWidgets.QLineEdit(self)
        self.entry.setFixedSize(1000, 50)  # Increase the width to 1000
        self.entry.setStyleSheet("padding-left: 10px; padding-right: 10px;")  # Add padding

        self.send_button = QtWidgets.QPushButton("Send", self)
        self.send_button.clicked.connect(self.send_message)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.chatbox)
        layout.addWidget(self.entry)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

    def send_message(self):
        message = self.entry.text()
        response = openai.Completion.create(engine="davinci-codex", prompt=message, max_tokens=60)
        self.chatbox.setReadOnly(False)
        self.chatbox.append(f"You: {message}")
        self.chatbox.append(f"Chatbot: {response.choices[0].text.strip()}")
        self.chatbox.setReadOnly(True)
        self.entry.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ChatWindow()
    window.show()
    app.exec()
