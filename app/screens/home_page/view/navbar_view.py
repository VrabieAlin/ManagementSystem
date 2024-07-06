from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout

from app.utils.widget_utils import WidgetUtils


class NavbarView(BoxLayout):
    def __init__(self,**kwargs):
        super(NavbarView,self).__init__(**kwargs)
        WidgetUtils.SetBG(self,bg_color=[0.6,0.2,0.8,1])