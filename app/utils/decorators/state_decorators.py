import functools
import json


def save_after():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            context = func(self, *args, **kwargs)
            save_state(self, context)
            return context

        return wrapper

    return decorator


def save_state(self, context):
    data = {}

    # Deschide fișierul JSON și citește datele existente
    try:
        with open(self.file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Fișierul {self.file_path} nu a fost găsit.")
    except json.JSONDecodeError:
        print(f"Fișierul {self.file_path} nu este un JSON valid.")

    with open(self.file_path, "w") as file:
        for field_name, field_value in context.items():
            data[field_name] = field_value
        json.dump(data, file, indent=4)

    self.state_changed.emit()