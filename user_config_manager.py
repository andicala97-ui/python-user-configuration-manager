Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def add_setting(settings, new_setting):
...     key, value = new_setting
...     key = key.lower()
...     value = value.lower()
... 
...     if key in settings:
...         return f"Setting '{key}' already exists! Cannot add a new setting with this name."
... 
...     if key not in settings:
...         settings[key] = value
...         return f"Setting '{key}' added with value '{value}' successfully!"
... 
... 
... def update_setting(settings, new_setting):
...     key, value = new_setting
...     key = key.lower()
...     value = value.lower()
... 
...     if key in settings:
...         settings[key] = value
...         return f"Setting '{key}' updated to '{value}' successfully!"
... 
...     if key not in settings:
...         return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
... 
... 
... def delete_setting(settings, key):
...     key = key.lower()
... 
...     if key in settings:
...         del settings[key]
...         return f"Setting '{key}' deleted successfully!"
... 
...     if key not in settings:
...         return 'Setting not found!'


def view_settings(settings):
    if not settings:
        return 'No settings available.'

    result = 'Current User Settings:'

    for key, value in settings.items():
        result += f'\n{key.capitalize()}: {value}'

    return result + '\n'


test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
