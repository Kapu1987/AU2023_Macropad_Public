# MACROPAD Hotkeys example: Autodesk Fusion 360 for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Win Fusion 360', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x5c1e00, 'Esc',       [Keycode.ESCAPE]),
        (0x5c1e00, 'Undo',      [Keycode.CONTROL, 'z']),   #Undo
        (0x5c1e00, 'Redo',      [Keycode.CONTROL, 'Z']),   #Redo
        # 2nd row ----------
        (0x5c1e00, 'Window',    '1'),   # Select by window
        (0x5c1e00, 'Lasso',     '2'),   # Select by Lasso
        (0x5c1e00, 'Paint',     '3'),   # Select by paint
        # 3rd row ----------
        (0x5c1e00, 'Psh-Pll',   'q'),   # Push Pull command
        (0x5c1e00, 'Extr',      'e'),   # Extrude command
        (0x5c1e00, 'Fllt',      'f'),   # Fillet command
        # 4th row ----------
        (0x5c1e00, 'Line',      'l'),   # Line command
        (0x5c1e00, 'Proj',      'p'),   # Project command
        (0x5c1e00, 'Shrtct',    's'),   # shortcuts pallet
        # Encoder button ---
        (0x000000, '',          [Keycode.CONTROL, 's'])   # Save
    ]
}
