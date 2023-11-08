# MACROPAD Hotkeys example: Autodesk AutoCAD for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Win AutoCAD', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x641928, 'Esc',    [Keycode.ESCAPE]),
        (0x641928, 'Undo',   [Keycode.CONTROL, 'z']),   #Undo
        (0x641928, 'Redo',   [Keycode.CONTROL, 'Z']),   #Redo
        # 2nd row ----------
        (0x641928, 'Line',   'l'),   # Line
        (0x641928, 'Circ',   'c'),   # Circle
        (0x641928, 'Arc',    'a'),   # Arc
        # 3rd row ----------
        (0x641928, 'Strtch', 's'),   # Stretch
        (0x641928, 'Expld',  'x'),   # Explode
        (0x641928, 'Move',   'm'),   # Move
        # 4th row ----------
        (0x641928, 'Zoom',   'z'),   # Zoom
        (0x641928, 'Rdraw',  'r'),   # Redraw
        (0x641928, 'Enter',  [Keycode.ENTER]),   # Enter key
        # Encoder button ---
        (0x000000, '',       [Keycode.CONTROL, 's'])   # Save
    ]
}
