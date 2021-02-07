from pytube import YouTube
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

         #Create a combo box
        my_combo = qtw.QComboBox(self)
        my_combo.addItem("360p", "360p")
        my_combo.addItem("480p", "480p")
        my_combo.addItem("720p", "720p")
        self.layout().addWidget(my_combo)

        #Create a button
        my_button = qtw.QPushButton("Download",
        clicked = lambda: press_it())
        self.layout().addWidget(my_button)

       
        

        self.show()

        def press_it():

            #Keep data
            url = my_entry.text()
            quality = my_combo.currentText()

            #clear entry
            my_entry.setText('')

            #Do pytube stuff
            print(url)
            print(quality)
            yt = YouTube(url)
            print(yt.title)
            #yt.streams.first().download('./Downloads')
            """
            versions = yt.streams.filter(progressive=True)
            for version in versions:
                print(version.resolution)
            """

app = qtw.QApplication([])
mw = MainWindow()

#Run the app

app.exec_()



