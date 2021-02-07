import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #Set a title
        self.setWindowTitle("YouTube Downloader")

        #Set a layout
        self.setLayout(qtw.QVBoxLayout())
        #Create a label
        my_label = qtw.QLabel("Welcome to free to use YouTube Downloader")
        #Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)
        
        #Set the url entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("Paste youtube url here")
        self.layout().addWidget(my_entry)

        #Create a button
        my_button = qtw.QPushButton("Press me !",
        clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            url = my_entry.text()
            #clear entry
            my_entry.setText('')
            print(url)

app = qtw.QApplication([])
mw = MainWindow()

#Run the app

app.exec_()