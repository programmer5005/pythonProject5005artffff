from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class DailyRoutineAssistantApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, World", halign="center")


DailyRoutineAssistantApp().run()
