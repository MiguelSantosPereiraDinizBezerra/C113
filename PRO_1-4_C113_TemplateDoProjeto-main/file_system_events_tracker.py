import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/Kuttimma/Downloads"

# Classe Gerenciadora de Eventos
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
        print(event.src_path)
    def on_deleted(self, event):
        print(f"Opa, alguém excluiu uma pasta{event.src_path}")
    def on_modified(self, event):
        print("Olá [event.src_path] foi modificada")
    def on_moved(self, event):
        print("Olá, a {event.src_path} foi modificada")
# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileEventHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Inicie o Observer
observer.start()


#5_Escreva uma exceção para keyboardInterrupt
try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido")
observer.stop()





