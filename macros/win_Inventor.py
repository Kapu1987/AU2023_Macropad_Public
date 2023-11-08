# MACROPAD Hotkeys example: Autodesk Inventor

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Inventor', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x5c3c00, 'Esc',      [Keycode.ESCAPE]),
        (0x5c3c00, 'Undo',     [Keycode.CONTROL, 'z']),   #Undo
        (0x5c3c00, 'Redo',     [Keycode.CONTROL, 'Z']),   #Redo
        # 2nd row ----------
        (0x5c3c00, 'WAxis',    '/'),   # Work Axis
        (0x5c3c00, 'WPlan',    ']'),   # Work Plane
        (0x5c3c00, 'WPoi',     '.'),   # Work Point
        # 3rd row ----------
        (0x5c3c00, '=',        '='),   # Equal
        (0x5c3c00, 'GndWP',    ';'),   # Ground Work point
        (0x5c3c00, 'Del',      [Keycode.DELETE]),   # Delete command
        # 4th row ----------
        (0x5c3c00, 'ZAll',     [Keycode.HOME]),   # Zoom All
        (0x5c3c00, 'ZSel',     [Keycode.END]),   # Zoom Selected
        (0x5c3c00, 'Enter',    [Keycode.ENTER]),   # Enter key
        # Encoder button ---
        (0x000000, '',         [Keycode.CONTROL, 's'])   # Save
    ]
}
