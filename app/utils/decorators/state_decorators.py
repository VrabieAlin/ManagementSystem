import functools
import json


def save_after():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            save_state(self)
            return result

        return wrapper

    return decorator


def save_state(self):
    with open(self.file_path, "w") as file:
        json.dump({
            "logged_in": self.logged_in,
            "user_name": self.user_name,
            "order_page_state": self.order_page_state}, file)

        self.state_changed.emit()