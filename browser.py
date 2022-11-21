# Import the required libraries
import traceback
import webview
import time

class Browser:
    def __init__(self, title, url):
        self.window = webview.create_window(title, url, min_size=(450, 700), height=700, width=450, confirm_close=True)

    def get_window(self):
        return self.window

    def on_closed(self):
        print('pywebview window is closed')


    def on_closing(self):
        print('pywebview window is closing')


    def on_shown(self):
        print('pywebview window shown')


    def on_minimized(self):
        print('pywebview window minimized')


    def on_restored(self):
        print('pywebview window restored')


    def on_maximized(self):
        print('pywebview window maximized')


    def on_loaded(self):
        print('DOM is ready')

        # unsubscribe event listener
        #webview.windows[0].loaded -= on_loaded
        #webview.windows[0].load_url('https://rust-book.cs.brown.edu')
        print(self.window.get_current_url())

    def on_resized(self, width, height):
        print('pywebview window is resized. new dimensions are {width} x {height}'.format(width=width, height=height))


    def on_moved(self, x, y):
        print('pywebview window is moved. new coordinates are x: {x}, y: {y}'.format(x=x, y=y))



    def start(self):
        try:
            print("Window Loading.")
            self.window.events.closed += self.on_closed
            self.window.events.closing += self.on_closing
            self.window.events.shown += self.on_shown
            self.window.events.loaded += self.on_loaded
            self.window.events.minimized += self.on_minimized
            self.window.events.maximized += self.on_maximized
            self.window.events.restored += self.on_restored
            self.window.events.resized += self.on_resized
            self.window.events.moved += self.on_moved
            webview.start()
        except Exception as exp:
            traceback.print_exc()

if __name__ == '__main__':
    owindow = Browser("Aprendiendo Rust!", "https://rust-book.cs.brown.edu")
    owindow.start()