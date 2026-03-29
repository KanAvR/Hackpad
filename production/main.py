import board
import busio
import displayio
import terminalio
import neopixel
import adafruit_displayio_ssd1306
from adafruit_display_text import label

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, make_key
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

COL_PINS = (board.D0, board.D1, board.D2)
ROW_PINS = (board.D7, board.D8, board.D9)
ENC_A    = board.D6
ENC_B    = board.D10
RGB_PIN  = board.A3
I2C_SDA  = board.SDA
I2C_SCL  = board.SCL

pixel = neopixel.NeoPixel(RGB_PIN, 1, brightness=0.2, pixel_order=neopixel.GRBW)
pixel[0] = (0, 0, 30, 0)

displayio.release_displays()
_i2c      = busio.I2C(I2C_SCL, I2C_SDA)
_disp_bus = displayio.I2CDisplay(_i2c, device_address=0x3C)
_display  = adafruit_displayio_ssd1306.SSD1306(_disp_bus, width=128, height=32)

_root = displayio.Group()
_display.root_group = _root

_lbl_title = label.Label(terminalio.FONT, text="VOL", color=0xFFFFFF, x=2,  y=5)
_root.append(_lbl_title)

_lbl_pct = label.Label(terminalio.FONT, text=" 50%", color=0xFFFFFF, x=98, y=5)
_root.append(_lbl_pct)

_lbl_mute = label.Label(terminalio.FONT, text="   ", color=0xFFFFFF, x=2, y=26)
_root.append(_lbl_mute)

_BX, _BY, _BW, _BH = 2, 13, 124, 11

_bg_bmp = displayio.Bitmap(_BW, _BH, 2)
_bg_pal = displayio.Palette(2)
_bg_pal[0] = 0x000000
_bg_pal[1] = 0xFFFFFF
for px in range(_BW):
    _bg_bmp[px, 0] = 1
    _bg_bmp[px, _BH - 1] = 1
for py in range(_BH):
    _bg_bmp[0, py] = 1
    _bg_bmp[_BW - 1, py] = 1
_root.append(displayio.TileGrid(_bg_bmp, pixel_shader=_bg_pal, x=_BX, y=_BY))

_FILL_INNER_W = _BW - 2
_FILL_INNER_H = _BH - 2
_fill_pal    = displayio.Palette(1)
_fill_pal[0] = 0xFFFFFF
_fill_bmp  = displayio.Bitmap(61, _FILL_INNER_H, 1)
_fill_tile = displayio.TileGrid(_fill_bmp, pixel_shader=_fill_pal, x=_BX + 1, y=_BY + 1)
_root.append(_fill_tile)


def _update_oled(vol, muted):
    global _fill_tile, _root
    if muted:
        _lbl_pct.text   = "MUTE"
        _lbl_mute.text  = "[M]"
        _fill_pal[0]    = 0x000000
        new_w = 1
        pixel[0] = (30, 0, 0, 0)
    else:
        _lbl_pct.text   = f"{vol:3d}%"
        _lbl_mute.text  = "   "
        _fill_pal[0]    = 0xFFFFFF
        new_w = max(1, vol * _FILL_INNER_W // 100)
        pixel[0] = (0, 0, 30, 0)
    _root.remove(_fill_tile)
    _fill_bmp  = displayio.Bitmap(new_w, _FILL_INNER_H, 1)
    _fill_tile = displayio.TileGrid(_fill_bmp, pixel_shader=_fill_pal, x=_BX + 1, y=_BY + 1)
    _root.append(_fill_tile)


_vol   = 50
_muted = False
_update_oled(_vol, _muted)


def _vol_up_press(key, keyboard, *args):
    global _vol, _muted
    _muted = False
    _vol   = min(100, _vol + 5)
    _update_oled(_vol, _muted)
    keyboard.keys_pressed.add(KC.VOLU)
    keyboard.hid_pending = True

def _vol_up_release(key, keyboard, *args):
    keyboard.keys_pressed.discard(KC.VOLU)
    keyboard.hid_pending = True

def _vol_dn_press(key, keyboard, *args):
    global _vol, _muted
    _muted = False
    _vol   = max(0, _vol - 5)
    _update_oled(_vol, _muted)
    keyboard.keys_pressed.add(KC.VOLD)
    keyboard.hid_pending = True

def _vol_dn_release(key, keyboard, *args):
    keyboard.keys_pressed.discard(KC.VOLD)
    keyboard.hid_pending = True

def _mute_press(key, keyboard, *args):
    global _muted
    _muted = not _muted
    _update_oled(_vol, _muted)
    keyboard.keys_pressed.add(KC.MUTE)
    keyboard.hid_pending = True

def _mute_release(key, keyboard, *args):
    keyboard.keys_pressed.discard(KC.MUTE)
    keyboard.hid_pending = True


VOL_UP = make_key(names=('VOL_UP',), on_press=_vol_up_press, on_release=_vol_up_release)
VOL_DN = make_key(names=('VOL_DN',), on_press=_vol_dn_press, on_release=_vol_dn_release)
MUTE   = make_key(names=('MUTE',),   on_press=_mute_press,   on_release=_mute_release)


keyboard = KMKKeyboard()

keyboard.matrix = MatrixScanner(
    column_pins       = COL_PINS,
    row_pins          = ROW_PINS,
    diode_orientation = DiodeOrientation.COL2ROW,
)

keyboard.extensions.append(MediaKeys())

enc      = EncoderHandler()
enc.pins = ((ENC_A, ENC_B, None, False),)
enc.map  = [
    ((VOL_DN, VOL_UP, MUTE),),
]
keyboard.modules.append(enc)

S  = KC.LGUI
SS = lambda k: KC.LGUI(KC.LSFT(k))

keyboard.keymap = [
    [
        S(KC.N1),   S(KC.N2),  S(KC.N3),
        S(KC.N4),   S(KC.N5),  S(KC.N6),
        S(KC.Q),    S(KC.F),   SS(KC.S),
    ],
]

if __name__ == '__main__':
    keyboard.go()
