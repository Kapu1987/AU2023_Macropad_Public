# MACROPAD Hotkeys example: Autodesk Maya for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Win Maya', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x005060, 'Esc',    [Keycode.ESCAPE]),
        (0x005060, 'Undo',   [Keycode.CONTROL, 'z']),   #Undo
        (0x005060, 'Redo',   [Keycode.CONTROL, 'Z']),   #Redo
        # 2nd row ----------
        (0x005060, 'Vrtx',   [Keycode.F9]),    # Vertex
        (0x005060, 'Edge',   [Keycode.F10]),   # Edge
        (0x005060, 'Face',   [Keycode.F11]),   # Face
        # 3rd row ----------
        (0x005060, 'RouQ',  '1'),   # Rough Q
        (0x005060, 'MedQ',  '2'),   # Medium Q
        (0x005060, 'SmooQ', '3'),   # Smooth Q
        # 4th row ----------
        (0x005060, 'Sel',   'q'),   # Select
        (0x005060, 'Move',  'w'),   # Move
        (0x005060, 'Enter',  [Keycode.ENTER]),   # Enter key
        # Encoder button ---
        (0x000000, '',       [Keycode.CONTROL, 's'])   # Save
    ]
}
