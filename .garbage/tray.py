from pystray import Icon as icon, Menu as menu, MenuItem as item
import pystray
from PIL import Image, ImageDraw
import webview
import time

class Tray:
    def __init__(self, window):
        self.window = window
        print("Iniciamos el tray.")

    def browser_load(self, owindow):
        time.sleep(1)
        owindow.start()

    def on_clicked(self, icon, url):
        print(f"Haz presionado {icon} {url}.")
        title = "Aprendiendo Rust"
        # CREAMOS UN HILO PARA EL BROWSER
        print("Window Loading.")
        #window = webview.create_window(title, url, min_size=(450, 700), height=700, width=450, confirm_close=True)
        #webview.start()

    def start(self):
        # LEEMOS EL ARCHIVO CON EL LISTADO DE SITIOS.
        asitios = open("sites.txt")
        imenus = []
        for line in asitios.readlines():
            imenus.append([line, self.on_clicked])

        # CREAMOS EL MENU CON SUS ITEMS
        menu = []
        for imenu in imenus:
            menu.append(item(imenu[0], imenu[1]))

        # SET THE APPLICATION ICON
        favicon = Image.open("favicon.png")
        icon('elearner', favicon, menu=menu).run()

if __name__ == '__main__':
    otray = Tray()
    otray.start()