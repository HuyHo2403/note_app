###Imports###
from PyQt5.QtWidgets import(
    QApplication, QWidget, QPushButton, QLabel, QListWidget,
    QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QMessageBox
)
import json
import stylesheet



###Constants###
WIDTH = 900
HEIGHT = 600


###Empty Dictionary### 
notes = {}


###Functions###
#*Read from json files
def json_read_notes():
    with open("notes_data.json", "r") as file:
        notes = json.load(file)
    lst_notes.addItems(notes)
    return notes

#*Write notes to Json
def json_write_notes():
    with open("notes_data.json", "w") as file:
        json.dump(notes, file, sort_keys=True, ensure_ascii=False, indent=4)
    

#*Show note
def show_note():
    key = lst_notes.selectedItems()[0].text()
    text_field_note.setText(notes[key]["text"])
    lst_tags.clear()
    lst_tags.addItems(notes[key]["tags"])

def add_note():
    note_name, ok = QInputDialog.getText(main_win, "Add Note", "Note Name")
    if note_name and ok != "":
        notes[note_name] = {"text": "", "tags" : []}
        lst_notes.addItem(note_name)
        lst_tags.addItems(notes[note_name]["tags"])
    else:
        warn_no_name()



def save_note():
    if lst_notes.selectedItems():
        note_name = lst_notes.selectedItems()[0].text()
        notes[note_name]["text"] = text_field_note.toPlainText()
        json_write_notes()
    else:
        warn_none_selected()

def delete_note():
    if lst_notes.selectedItems()[0].text():
        note_name = lst_notes.selectedItems()[0].text()
        del notes[note_name]
        lst_notes.clear()
        lst_tags.clear()
        text_field_note.clear()
        lst_notes.addItems(notes)
        json_write_notes()
    else:
        warn_none_selected()

def add_tag():
    if lst_notes.selectedItems():
        key = lst_notes.selectedItems()[0].text()
        tag = line_field_tag.text()
        if not tag in notes[key]["tags"]:
            notes[key]["tags"].append(tag)
            lst_tags.addItem(tag)
            line_field_tag.clear()
            json_write_notes()
    else:
        warn_none_selected()


def search_tag():
    tag = line_field_tag.text()
    if btn_search_tag.text() == "Search" and tag:
        filtered_notes = {}
        for note in notes:
            if tag in notes[note]["tags"]:
                filtered_notes[note] = notes[note]
        btn_search_tag.setText("Reset Search")
        lst_notes.clear()
        lst_tags.clear()
        lst_notes.addItems(filtered_notes)

    elif btn_search_tag.text() == "Reset Search":
        line_field_tag.clear()
        lst_notes.clear()
        lst_tags.clear()
        lst_notes.addItems(notes)
        btn_search_tag.setText("Search")



def delete_tag():
    if lst_tags.selectedItems():
        key = lst_notes.selectedItems()[0].text()
        tag = lst_tags.selectedItems()[0].text()
        notes[key]["tags"].remove(tag)
        lst_tags.clear()
        lst_tags.addItems(notes[key]["tags"])
        json_write_notes()
    else:
        warn_none_selected()



def warn_none_selected():
    warn = QMessageBox()
    warn.setWindowTitle("Error")
    warn.setText("No item selected")
    warn.exec_()


def warn_no_name():
    warn = QMessageBox()
    warn.setWindowTitle("Error")
    warn.setText("No name entered")
    warn.exec_()


###Application objects###
app = QApplication([])


#### Main Window Setup ###
main_win = QWidget()
main_win.setWindowTitle("Smart Notes")
main_win.resize(WIDTH, HEIGHT)


###GUI Objects###
#* Labels
label_note_lst = QLabel("Notes")
label_tag_lst = QLabel("Tags")


#* List Widgets
lst_notes = QListWidget()
lst_tags = QListWidget()

#* Button Widgets
btn_create_note = QPushButton("Create")
btn_delete_note = QPushButton("Delete")
btn_save_note = QPushButton("Save")

btn_add_tag = QPushButton("Add")
btn_search_tag = QPushButton("Search")
btn_delete_tag = QPushButton("Delete")

#* Text Entry Widgets
text_field_note = QTextEdit()
line_field_tag = QLineEdit()
line_field_tag.setPlaceholderText("Enter tag...")


###Layout Objects###
#*Main layout
layout_main = QHBoxLayout()

#*Column Layouts
layout_col_1 = QVBoxLayout()
layout_col_2 = QVBoxLayout()

#*Row layouts
layout_note_buttons = QHBoxLayout()
layout_tag_buttons = QHBoxLayout()

###Window Layout###
#*Add Buttons to Buttons Layouts
layout_note_buttons.addWidget(btn_create_note)
layout_note_buttons.addWidget(btn_save_note)
layout_note_buttons.addWidget(btn_delete_note)

layout_tag_buttons.addWidget(btn_add_tag)
layout_tag_buttons.addWidget(btn_search_tag)
layout_tag_buttons.addWidget(btn_delete_tag)

#*Add text to Edit Column 1
layout_col_1.addWidget(text_field_note)

#*Add Widgets and Button Layouts to column 2
layout_col_2.addWidget(label_note_lst)
layout_col_2.addWidget(lst_notes)
layout_col_2.addLayout(layout_note_buttons)
layout_col_2.addWidget(label_tag_lst)
layout_col_2.addWidget(lst_tags)
layout_col_2.addWidget(line_field_tag)
layout_col_2.addLayout(layout_tag_buttons)

#* Add column Layouts to Main Layouts
layout_main.addLayout(layout_col_1, stretch=2)
layout_main.addLayout(layout_col_2, stretch=1)

#*Add main layout to main window
main_win.setLayout(layout_main)



###Event Handlers###
lst_notes.itemClicked.connect(show_note)
btn_save_note.clicked.connect(save_note)
btn_create_note.clicked.connect(add_note)
btn_delete_note.clicked.connect(delete_note)

btn_add_tag.clicked.connect(add_tag)
btn_delete_tag.clicked.connect(delete_tag)
btn_search_tag.clicked.connect(search_tag)

### Set Styles###
stylesheet.set_style(app)



###Application Execution###
main_win.show()
notes = json_read_notes()
app.exec_()
