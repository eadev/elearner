import webbrowser
from tkinter import *
from tray import Tray
from browser import Browser
import webview
import time
import threading
from multiprocessing import Process, Pipe


try:
  import tkinter as tk #python3
except ImportError:
  import Tkinter as tk #python2

def browser_load(browser):
    time.sleep(1)
    browser.start()

def tray_load(window):
    # CREAMOS EL SYSTEMTRAY
    otray = Tray(window)
    otray.start()

if __name__ == '__main__':
    # TUBERÍA PRINCIPAL
    parent_pipe, child_pipe = Pipe()

    # CARGAMOS EL WINDOW
    browser = Browser("Aprendiendo Rust!", "https://rust-book.cs.brown.edu/")
    window = browser.get_window()
    # CREAMOS EL HILO PARA CAMBIAR LA URL
    tray = threading.Thread(target=tray_load(window))
    tray.start()
    tray.join()
    # CREAMOS UN HILO PARA EL BROWSER
    tbrowser = threading.Thread(target=browser_load(browser))
    tbrowser.start()
    tbrowser.join()




