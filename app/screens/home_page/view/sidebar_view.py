from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget


class SidebarView(Widget):

    def __init__(self,**kwargs):
        super(SidebarView,self).__init__(**kwargs)
        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)  # RGBA (light blue)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos