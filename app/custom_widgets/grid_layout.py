from kivy.uix.boxlayout import BoxLayout


class GridLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(GridLayout,self).__init__(**kwargs)
        self.orientation='vertical'

    def add_row(self,widgets):
        if len(widgets) > 1:
            columns = BoxLayout(orientation='horizontal')
            for w in widgets:
                columns.add_widget(w)
            self.add_widget(columns)
        else:
            self.add_widget(widgets[0])