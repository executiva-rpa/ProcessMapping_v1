import ctypes, win32gui, win32ui
from PIL import Image, ImageGrab


def get_cursor():
    hcursor = win32gui.GetCursorInfo()[1]
    hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap(hdc, 36, 36)
    hdc = hdc.CreateCompatibleDC()
    hdc.SelectObject(hbmp)
    hdc.DrawIcon((0, 0), hcursor)

    bmpinfo = hbmp.GetInfo()
    bmpstr = hbmp.GetBitmapBits(True)
    cursor = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1).convert(
        "RGBA")

    win32gui.DestroyIcon(hcursor)
    win32gui.DeleteObject(hbmp.GetHandle())
    hdc.DeleteDC()

    pixdata = cursor.load()

    width, height = cursor.size
    for y in range(height):
        for x in range(width):

            if pixdata[x, y] == (0, 0, 0, 255):
                pixdata[x, y] = (0, 0, 0, 0)

    hotspot = win32gui.GetIconInfo(hcursor)[1:3]

    return (cursor, hotspot)


cursor, (hotspotx, hotspoty) = get_cursor()
cursor.save("cursor.png")

ratio = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100

img = ImageGrab.grab(bbox=None, include_layered_windows=True)

pos_win = win32gui.GetCursorPos()
pos = (round(pos_win[0] * ratio - hotspotx), round(pos_win[1] * ratio - hotspoty))

img.paste(cursor, pos, cursor)

img.save("screenshot.png")