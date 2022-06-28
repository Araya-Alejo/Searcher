from cgi import print_arguments
import ctypes
import Searcher as searcher
# from pynput.keyboard import Key, Controller

CF_TEXT = 1

kernel32 = ctypes.windll.kernel32
kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
kernel32.GlobalLock.restype = ctypes.c_void_p
kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
user32 = ctypes.windll.user32
user32.GetClipboardData.restype = ctypes.c_void_p

# def Paste():
#     """ Paste in clipboard the selected area"""
#     # pass
#     keyboard = Controller()
#     keyboard.press('a')
#     keyboard.press(Key.enter)

def get_clipboard_text():
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            data_locked = kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            kernel32.GlobalUnlock(data_locked)
            print(get_clipboard_text)
            search = str(value)
            print(search)
            searcher.buscar_lo_seleccionado(search[2:-1])
            return value
    finally:
        user32.CloseClipboard()

print(get_clipboard_text())