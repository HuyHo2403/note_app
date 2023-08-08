from PyQt5 import QtGui

def set_style(app):
    QtGui.QFontDatabase.addApplicationFont(".VnBook-Antiqua")
    font = QtGui.QFont(".VnBook-Antiqua")
    font.setPointSize(10)
    app.setFont(font)
    

    app.setStyleSheet(
        """QWidget {
            color: #bbbfc3;
            background-color : #282b30;}
            """
        """QPushButton {
            background-color : #424549;
            border-radius : 10px;
            padding : 4px;
            padding-bottom : 7px;
            max-width : 3em;
            min-width : 3em;}
            """
        """QListWidget {
            border-radius : 10px;
            margin-bottom : 10px;
            padding-left : 5px;
            border : 2px solid #5b5b5b;}
            """
        """QLineEdit {
            margin-bottom : 10px;
            border-radius : 10px
            padding-left : 7px;
            padding-bottom : 4px;
            border : 2px solid #5b5b5b;}
            """
        """QLineEdit {
            border-radius : 10px;
            border : 2px solid #5b5b5b;}
            """
    )
