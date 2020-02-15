import json
import os
import traceback

path = './Ymmp/'


def do():
    try:
        for file in os.listdir(path):
            with open(path + file, 'r', encoding='utf-8') as f:
                ymmp = json.loads(f.read())

            from datetime import time, timedelta

            current_frame = 0
            for item in ymmp['Timeline']['Items']:
                if item['VoiceLength'] == '00:00:00':
                    continue
                dt = time.fromisoformat(item['VoiceLength'][:-1])
                seconds = (dt.hour * 3600 + dt.minute * 60 + dt.second + (dt.microsecond / 1000000)) / item[
                    'PlaybackRate'] * 100
                frames = int(seconds / (1 / 30))

                item['Length'] = frames + 6
                item['Frame'] = current_frame
                current_frame += frames + 6 + 6

            with open('./CompleteYmmp/' + file, 'w', encoding='utf-8') as f:
                data = json.dumps(ymmp, ensure_ascii=False)
                f.write(data)
    except:
        traceback.print_exc()
        input('エラー')


if __name__ == '__main__':
    do()
