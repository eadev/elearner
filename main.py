import webbrowser
from tkinter import *
from tray import Tray
from browser import Browser
import webview
import time
import threading

def browser_load(owindow):
    time.sleep(10)
    owindow.start()

def tray_load(window):
    time.sleep(1)
    # CREAMOS EL SYSTEMTRAY
    otray = Tray(window)
    otray.start()

if __name__ == '__main__':

    # CARGAMOS EL WINDOW
    owindow = Browser("Aprendiendo Rust!", "https://rust-book.cs.brown.edu/")
    window = owindow.get_window()

    # CREAMOS EL HILO PARA CAMBIAR LA URL
    ttray = threading.Thread(target=tray_load(window))
    ttray.start()
    # CREAMOS UN HILO PARA EL BROWSER
    tbrowser = threading.Thread(target=browser_load(owindow))
    tbrowser.start()




