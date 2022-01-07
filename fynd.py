import sys
import re
import os.path
import argparse
import PySimpleGUI as gui

# Function to get the count of the specified track name
def get_track_count(track_name, input_file):

    search_track_name = re.compile(r'(?<=trackName. : .)[^,\"]*')  
    track_count = 0

    with open(input_file, encoding='cp850') as stream_history_f1:
            
            while True:
                line_f1 = stream_history_f1.readline()

                # Break loop if EOF is reached
                if line_f1 == '':
                    break
                
                # If the name of the specified track is matched the increment the count
                for names in re.finditer(search_track_name, line_f1):
                    if names.group() == track_name:
                        track_count += 1

    return track_count

# Function to add new user input boxes if 'Add' is pressed
def new_layout():
    return [[gui.Input(), gui.FileBrowse()]]

def main():

    # Theme for the pop-up window
    gui.theme('GreenMono')

    # Layout to ask for file input
    column_layout = [
                      [gui.Input(), gui.FileBrowse()]
                    ]

    # Buttons and text within the window
    layout = [ 
               [gui.Text('Track Name:')],
               [gui.InputText()],
               [gui.Text('Select File(s): ')],
               [gui.Column(column_layout, key='column'), gui.Button('Add')],
               [gui.Button('Done'), gui.Button('Cancel')]
             ]

    # Title of the window
    window = gui.Window('SpotiFynd', layout)

    # Start window
    while True:
        event, values = window.read()

        # Close window if 'X' or 'Done' or 'Cancel' are clicked
        if event == gui.WIN_CLOSED or event == 'Cancel' or event == 'Done':
            break

        # If 'Add' button is pressed add more file inputs
        elif event == 'Add':
            window.extend_layout(window['column'],new_layout())

    window.close()

    # Tracked listened count
    count = get_track_count(str(values[0]), str(values[1]))

    # Pop-up window to display results
    gui.popup_no_buttons('\nYou have listened to '+ values[0] + ' ' + str(count) + ' times\n', location = (500, 500), title = 'Displaying Results', no_titlebar= False)



if __name__ == "__main__":
    main()
