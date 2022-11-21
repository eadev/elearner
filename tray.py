from pystray import Icon as icon, Menu as menu, MenuItem as item
import pystray
from PIL import Image, ImageDraw
import webview

class Tray:
    def __init__(self, window_url):
        print("Constructor")
        self.window_url = window_url

    def on_clicked(self, icon, url):
        print(f"Haz presionado {icon} {url}.")
        title = "Aprendiendo Rust"
        self.window_url.load_url(url)

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
