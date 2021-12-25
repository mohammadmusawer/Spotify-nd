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

def main():

    # Theme for the pop-up window
    gui.theme('GreenMono')

    # Buttons and text within the window
    layout = [ 
               [gui.Text('Track Name:')],
               [gui.InputText()],
               [gui.Text('Select File: ')],
               [gui.Input(), gui.FileBrowse()],
               [gui.Button('Done'), gui.Button('Cancel')]
             ]
    
    # Title of the window
    window = gui.Window('Spotify Fynd', layout)

    while True:
        event, values = window.read()

        if event == gui.WIN_CLOSED or event == 'Done' or event == 'Cancel':
            break

        print('Track name: ', values[0])
        print('Path to file: ', values[1])

    window.close()
           

if __name__ == "__main__":
    main()