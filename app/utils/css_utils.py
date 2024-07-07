class CSSUtils:

    @classmethod
    def applyBackgroundColor(cls, color):
        return f"background-color: {color};"

    @classmethod
    def applyBorder(cls, pixel, type, color):
        return f"border: {pixel}px {type} {color};"