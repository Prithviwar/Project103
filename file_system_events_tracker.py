import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = 'C:/Users/warri/Documents/Document_Files'

class FileEventHandler(FileSystemEventHandler):
    def onCreated(self,event):
        print({event.src_path}, " created")
    def onModified(self,event):
        print({event.src_path}, " modified")
    def onMoved(self,event):
        print({event.src_path}, " moved")
    def onDeleted(self,event):
        print({event.src_path}, " deleted")

    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, from_dir, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(2)
            print("running...")
    except KeyboardInterrupt:
        print("stopped!")
        observer.stop()
    
