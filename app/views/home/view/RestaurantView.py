from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout

class ColoredWidget(Widget):
    def __init__(self, **kwargs):
        super(ColoredWidget, self).__init__(**kwargs)
        with self.canvas.before:
            # Setează culoarea
            Color(0.2, 0.6, 0.8, 1)  # RGBA (albastru deschis)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

class RestaurantView(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Creează un widget colorat și adaugă-l în layout
        colored_widget = ColoredWidget(size_hint=(1, 0.5))
        layout.add_widget(colored_widget)

        # Adaugă și alte widget-uri dacă este necesar
        label = Label(text="This is a label", font_size='24sp', size_hint=(1, 0.5))
        layout.add_widget(label)

        return layout