from kivy.uix.widget import Widget

from app.utils.utils import load_restaurant_view_image
from app.utils.widget_utils import WidgetUtils


class RestaurantView(Widget):
    def __init__(self, **kwargs):
        super(RestaurantView, self).__init__(**kwargs)
        WidgetUtils.SetBG(self, bg_color=[0.9, 0.9, 0.9, 1],source=load_restaurant_view_image())
