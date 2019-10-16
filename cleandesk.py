import time
import os
import json
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'jonas':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]

                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" +year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)

extensions_folders = {
#No name
    'noname' : "/Users/JL/Desktop/jonas/Other/Uncategorized",
#Audio
    '.aif' : "/Users/JL/Desktop/jonas/Media/Audio",
    '.cda' : "/Users/JL/Desktop/jonas/Media/Audio",
    '.mid' : "/Users/JL/Desktop/jonas/Media/Audio",
    '.midi' : "/Users/JL/Desktop/jonas/Media/Audio",
    '.mp3' : "/Users/JL/Desktop/jonas/Media/Audio",
    '.mpa' : "/Users/JL/Desktop/jonas/Media/Audio",
    '.ogg' : "/Users/JL/Desktop/jonas/Media/Audio",
    '.wav' : "/Users/JL/Desktop/jonas/Media/Audio",
    '.wma' : "/Users/JL/Desktop/jonas/Media/Audio",
    '.wpl' : "/Users/JL/Desktop/jonas/Media/Audio",
    '.m3u' : "/Users/JL/Desktop/jonas/Media/Audio",
#Text
    '.txt' : "/Users/JL/Desktop/jonas/Text/TextFiles",
    '.doc' : "/Users/JL/Desktop/jonas/Text/Microsoft/Word",
    '.docx' : "/Users/JL/Desktop/jonas/Text/Microsoft/Word",
    '.odt ' : "/Users/JL/Desktop/jonas/Text/TextFiles",
    '.pdf': "/Users/JL/Desktop/jonas/Text/PDF",
    '.rtf': "/Users/JL/Desktop/jonas/Text/TextFiles",
    '.tex': "/Users/JL/Desktop/jonas/Text/TextFiles",
    '.wks ': "/Users/JL/Desktop/jonas/Text/TextFiles",
    '.wps': "/Users/JL/Desktop/jonas/Text/TextFiles",
    '.wpd': "/Users/JL/Desktop/jonas/Text/TextFiles",
#Video
    '.3g2': "/Users/JL/Desktop/jonas/Media/Video",
    '.3gp': "/Users/JL/Desktop/jonas/Media/Video",
    '.avi': "/Users/JL/Desktop/jonas/Media/Video",
    '.flv': "/Users/JL/Desktop/jonas/Media/Video",
    '.h264': "/Users/JL/Desktop/jonas/Media/Video",
    '.m4v': "/Users/JL/Desktop/jonas/Media/Video",
    '.mkv': "/Users/JL/Desktop/jonas/Media/Video",
    '.mov': "/Users/JL/Desktop/jonas/Media/Video",
    '.mp4': "/Users/JL/Desktop/jonas/Media/Video",
    '.mpg': "/Users/JL/Desktop/jonas/Media/Video",
    '.mpeg': "/Users/JL/Desktop/jonas/Media/Video",
    '.rm': "/Users/JL/Desktop/jonas/Media/Video",
    '.swf': "/Users/JL/Desktop/jonas/Media/Video",
    '.vob': "/Users/JL/Desktop/jonas/Media/Video",
    '.wmv': "/Users/JL/Desktop/jonas/Media/Video",
#Images
    '.ai': "/Users/JL/Desktop/jonas/Media/Images",
    '.bmp': "/Users/JL/Desktop/jonas/Media/Images",
    '.gif': "/Users/JL/Desktop/jonas/Media/Images",
    '.ico': "/Users/JL/Desktop/jonas/Media/Images",
    '.jpg': "/Users/JL/Desktop/jonas/Media/Images",
    '.jpeg': "/Users/JL/Desktop/jonas/Media/Images",
    '.png': "/Users/JL/Desktop/jonas/Media/Images",
    '.ps': "/Users/JL/Desktop/jonas/Media/Images",
    '.psd': "/Users/JL/Desktop/jonas/Media/Images",
    '.svg': "/Users/JL/Desktop/jonas/Media/Images",
    '.tif': "/Users/JL/Desktop/jonas/Media/Images",
    '.tiff': "/Users/JL/Desktop/jonas/Media/Images",
    '.CR2': "/Users/JL/Desktop/jonas/Media/Images",
#Internet
    '.asp': "/Users/JL/Desktop/jonas/Other/Internet",
    '.aspx': "/Users/JL/Desktop/jonas/Other/Internet",
    '.cer': "/Users/JL/Desktop/jonas/Other/Internet",
    '.cfm': "/Users/JL/Desktop/jonas/Other/Internet",
    '.cgi': "/Users/JL/Desktop/jonas/Other/Internet",
    '.pl': "/Users/JL/Desktop/jonas/Other/Internet",
    '.css': "/Users/JL/Desktop/jonas/Other/Internet",
    '.htm': "/Users/JL/Desktop/jonas/Other/Internet",
    '.js': "/Users/JL/Desktop/jonas/Other/Internet",
    '.jsp': "/Users/JL/Desktop/jonas/Other/Internet",
    '.part': "/Users/JL/Desktop/jonas/Other/Internet",
    '.php': "/Users/JL/Desktop/jonas/Other/Internet",
    '.rss': "/Users/JL/Desktop/jonas/Other/Internet",
    '.xhtml': "/Users/JL/Desktop/jonas/Other/Internet",
#Compressed
    '.7z': "/Users/JL/Desktop/jonas/Other/Compressed",
    '.arj': "/Users/JL/Desktop/jonas/Other/Compressed",
    '.deb': "/Users/JL/Desktop/jonas/Other/Compressed",
    '.pkg': "/Users/JL/Desktop/jonas/Other/Compressed",
    '.rar': "/Users/JL/Desktop/jonas/Other/Compressed",
    '.rpm': "/Users/JL/Desktop/jonas/Other/Compressed",
    '.tar.gz': "/Users/JL/Desktop/jonas/Other/Compressed",
    '.z': "/Users/JL/Desktop/jonas/Other/Compressed",
    '.zip': "/Users/JL/Desktop/jonas/Other/Compressed",
#Disc
    '.bin': "/Users/JL/Desktop/jonas/Other/Disc",
    '.dmg': "/Users/JL/Desktop/jonas/Other/Disc",
    '.iso': "/Users/JL/Desktop/jonas/Other/Disc",
    '.toast': "/Users/JL/Desktop/jonas/Other/Disc",
    '.vcd': "/Users/JL/Desktop/jonas/Other/Disc",
#Data
    '.csv': "/Users/JL/Desktop/jonas/Programming/Database",
    '.dat': "/Users/JL/Desktop/jonas/Programming/Database",
    '.db': "/Users/JL/Desktop/jonas/Programming/Database",
    '.dbf': "/Users/JL/Desktop/jonas/Programming/Database",
    '.log': "/Users/JL/Desktop/jonas/Programming/Database",
    '.mdb': "/Users/JL/Desktop/jonas/Programming/Database",
    '.sav': "/Users/JL/Desktop/jonas/Programming/Database",
    '.sql': "/Users/JL/Desktop/jonas/Programming/Database",
    '.tar': "/Users/JL/Desktop/jonas/Programming/Database",
    '.xml': "/Users/JL/Desktop/jonas/Programming/Database",
    '.json': "/Users/JL/Desktop/jonas/Programming/Database",
#Executables
    '.apk': "/Users/JL/Desktop/jonas/Other/Executables",
    '.bat': "/Users/JL/Desktop/jonas/Other/Executables",
    '.com': "/Users/JL/Desktop/jonas/Other/Executables",
    '.exe': "/Users/JL/Desktop/jonas/Other/Executables",
    '.gadget': "/Users/JL/Desktop/jonas/Other/Executables",
    '.jar': "/Users/JL/Desktop/jonas/Other/Executables",
    '.wsf': "/Users/JL/Desktop/jonas/Other/Executables",
#Fonts
    '.fnt': "/Users/JL/Desktop/jonas/Other/Fonts",
    '.fon': "/Users/JL/Desktop/jonas/Other/Fonts",
    '.otf': "/Users/JL/Desktop/jonas/Other/Fonts",
    '.ttf': "/Users/JL/Desktop/jonas/Other/Fonts",
#Presentations
    '.key': "/Users/JL/Desktop/jonas/Text/Presentations",
    '.odp': "/Users/JL/Desktop/jonas/Text/Presentations",
    '.pps': "/Users/JL/Desktop/jonas/Text/Presentations",
    '.ppt': "/Users/JL/Desktop/jonas/Text/Presentations",
    '.pptx': "/Users/JL/Desktop/jonas/Text/Presentations",
#Programming
    '.c': "/Users/JL/Desktop/jonas/Programming/C&C++",
    '.class': "/Users/JL/Desktop/jonas/Programming/Java",
    '.dart': "/Users/JL/Desktop/jonas/Programming/Dart",
    '.py': "/Users/JL/Desktop/jonas/Programming/Python",
    '.sh': "/Users/JL/Desktop/jonas/Programming/Shell",
    '.swift': "/Users/JL/Desktop/jonas/Programming/Swift",
    '.html': "/Users/JL/Desktop/jonas/Programming/C&C++",
    '.h': "/Users/JL/Desktop/jonas/Programming/C&C++",
#Spreadsheets
    '.ods' : "/Users/JL/Desktop/jonas/Text/Microsoft/Excel",
    '.xlr' : "/Users/JL/Desktop/jonas/Text/Microsoft/Excel",
    '.xls' : "/Users/JL/Desktop/jonas/Text/Microsoft/Excel",
    '.xlsx' : "/Users/JL/Desktop/jonas/Text/Microsoft/Excel",
#System
    '.bak' : "/Users/JL/Desktop/jonas/Text/Other/System",
    '.cab' : "/Users/JL/Desktop/jonas/Text/Other/System",
    '.cfg' : "/Users/JL/Desktop/jonas/Text/Other/System",
    '.cpl' : "/Users/JL/Desktop/jonas/Text/Other/System",
    '.cur' : "/Users/JL/Desktop/jonas/Text/Other/System",
    '.dll' : "/Users/JL/Desktop/jonas/Text/Other/System",
    '.dmp' : "/Users/JL/Desktop/jonas/Text/Other/System",
    '.drv' : "/Users/JL/Desktop/jonas/Text/Other/System",
    '.icns' : "/Users/JL/Desktop/jonas/Text/Other/System",
    '.ico' : "/Users/JL/Desktop/jonas/Text/Other/System",
    '.ini' : "/Users/JL/Desktop/jonas/Text/Other/System",
    '.lnk' : "/Users/JL/Desktop/jonas/Text/Other/System",
    '.msi' : "/Users/JL/Desktop/jonas/Text/Other/System",
    '.sys' : "/Users/JL/Desktop/jonas/Text/Other/System",
    '.tmp' : "/Users/JL/Desktop/jonas/Text/Other/System",
}

folder_to_track = '/Users/JL/Desktop'
folder_destination = '/Users/JL/Desktop/jonas'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
