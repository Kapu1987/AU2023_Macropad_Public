# MACROPAD Hotkeys example: Autodesk Revit

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Revit', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000064, 'Esc',    [Keycode.ESCAPE]),
        (0x000064, 'Undo',   [Keycode.CONTROL, 'z']),   #Undo
        (0x000064, 'Redo',   [Keycode.CONTROL, 'Z']),   #Redo
        # 2nd row ----------
        (0x000064, '2D',     '32'),   # 2D mode
        (0x000064, 'Fly',    '3f'),   # Fly Mode
        (0x000064, 'Obj',    '3o'),   # Obj Mode
        # 3rd row ----------
        (0x000064, 'PlCom',  'cm'),   # Place component
        (0x000064, 'AlDim',  'di'),   # Aligned Dimension
        (0x000064, 'Line',   'li'),   # Line
        # 4th row ----------
        (0x000064, 'Align',  'al'),   # Zoom
        (0x000064, 'Array',  'ar'),   # Redraw
        (0x000064, 'Enter',  [Keycode.ENTER]),   # Enter key
        # Encoder button ---
        (0x000000, '',       [Keycode.CONTROL, 's'])   # Save
    ]
}
