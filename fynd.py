import sys
import re
import os.path
import argparse

def get_track_name():
    search_track_name = re.compile(r'(?<=trackName. : .)[^,\"]*')  
    
    with open("StreamingHistory0.json", encoding='cp850') as stream_history_f1:
        with open("StreamingHistory1.json", encoding='cp850') as stream_history_f2: 
           
            while True:
                line_f1 = stream_history_f1.readline()
                line_f2 = stream_history_f2.readline()

                if line_f1 == '':
                    break
                if line_f2 == '':
                    break
                
                for track in re.finditer(search_track_name, line_f1) and re.finditer(search_track_name, line_f2):
                    print('================================================')
                    print('Track name: ', track.group())


def main():
    get_track_name() 

    
if __name__ == "__main__":
    main()