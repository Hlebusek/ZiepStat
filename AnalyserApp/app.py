from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window

class TimelineWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timestamps = []

    def add_timestamp(self, timestamp):
        self.timestamps.append(timestamp)
        self.draw_timeline()

    def draw_timeline(self):
        self.canvas.clear()

        with self.canvas:
            Color(0, 0, 1)  # Blue color
            for timestamp in self.timestamps:
                Rectangle(pos=(timestamp, 0), size=(10, 20))  # Adjust size as needed

class MainApp(App):
    def build(self):
        self.timeline_widget = TimelineWidget()
        self.timeline_widget.add_timestamp(100)  # Example timestamp
        self.timeline_widget.add_timestamp(200)  # Example timestamp
        self.timeline_widget.add_timestamp(300)  # Example timestamp
        self.timeline_widget.add_timestamp(400)  # Example timestamp
        return self.timeline_widget

if __name__ == '__main__':
    Window.size = (800, 600)
    MainApp().run()
