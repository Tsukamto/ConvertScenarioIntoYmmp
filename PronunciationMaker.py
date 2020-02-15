import pyperclip
import pyautogui
import time
import csv
import os


def do():
    input('セリフ欄にカーソルを合わせてエンターキーを押してください。')
    serif_x, serif_y = pyautogui.position()

    input('発音欄にカーソルを合わせてエンターキーを押してください。')
    pronunciation_x, pronunciation_y = pyautogui.position()

    input('変換ボタンにカーソルを合わせてエンターキーを押してください。')
    transform_button_x, transform_button_y = pyautogui.position()

    path = './ExtractData/'
    pronunciation_path = './PronunciationData/'

    for file in os.listdir(path):
        if 'extract' not in file:
            continue

        with open(path + file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            text_list = [{'character': row[0], 'serif': row[1]} for row in reader]

        print(file + 'を処理中です。カーソルを動かさないでください。強制終了したい場合はカーソルを左上に素早く持って行ってください。')

        try:
            for text in text_list:
                pyautogui.FAILSAFE = True
                serif = text['serif']
                pyautogui.moveTo(serif_x, serif_y, duration=0)
                pyautogui.click()
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('a')
                pyperclip.copy(serif)
                pyautogui.keyDown('v')
                pyautogui.keyUp('ctrl')
                pyautogui.keyUp('a')
                pyautogui.keyUp('v')

                pyautogui.moveTo(transform_button_x, transform_button_y, duration=0)
                pyautogui.click()
                count = 0
                while True:
                    pyautogui.moveTo(pronunciation_x, pronunciation_y, duration=0)
                    pyautogui.click()
                    pyautogui.keyDown('ctrl')
                    pyautogui.keyDown('a')
                    pyautogui.keyDown('c')
                    if pyperclip.paste() == serif and count <= 3:
                        time.sleep(0.5)
                        count += 1
                    else:
                        text['pronunciation'] = pyperclip.paste()
                        break
                pyautogui.keyUp('ctrl')
                pyautogui.keyUp('a')
                pyautogui.keyUp('c')

            with open(pronunciation_path + file.replace('_extract', '_pronunciation'), 'w', encoding='utf-8') as f:
                for index, text in enumerate(text_list):
                    f.writelines(text['character'] + ',' + text['serif'] + ',' + text['pronunciation'] + '\n')
        except:
            pyautogui.FAILSAFE = False
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('a')
            pyautogui.keyUp('c')
            pyautogui.keyUp('v')
            print('----------------------------------------------')
            print('終了しました。予期せぬ終了の場合、連絡してください。')
            print('----------------------------------------------')


if __name__ == '__main__':
    do()
