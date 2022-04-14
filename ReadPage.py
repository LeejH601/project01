import pyperclip
import keyboard
import winsound


is_get = False
text = []


def play_ready_sound():
    winsound.Beep(440, 200)
    winsound.Beep(440, 200)


def play_end_sound():
    winsound.Beep(440, 200)
    winsound.Beep(440, 200)
    winsound.Beep(440, 200)


def report():
    global is_get, text
    winsound.Beep(400, 500)
    print("테스트")
    text = pyperclip.paste()
    if not text:
        winsound.Beep(440, 200)
    else:
        is_get = True


def Get_data_to_ClipBoard():
    global is_get, text
    keyboard.add_hotkey('ctrl+c', report)
    play_ready_sound()
    while not is_get:
        key = keyboard.read_hotkey(suppress=False)
    play_end_sound()
    keyboard.remove_hotkey(report)
    is_get = False
    return text


if __name__ == "__main__":
    t = Get_data_to_ClipBoard()
    f = open('data.txt', 'w')
    f.write(t)
    f.close()
