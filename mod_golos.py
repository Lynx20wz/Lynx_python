import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.playback import play


# from fuzzywuzzy import fuzz

program = {'VS_code': r'C:\Users\maks2\AppData\Local\Programs\Microsoft VS Code\Code.exe',
           'System_60': 'C:\\Users\\maks2\\Documents\\mods_HOI4\\System_60'}

opts = {
    'name': ('Ирбис', 'Барс', 'Ассистент'),
    'commands': {
        'mods': ("го кодить", "хойка и моды", "система 60"),
        'music': ('музыка', 'включи музыку')
    }
}

def as_list():
    play('pisk.mp3')

r = sr.Recognizer()
m =  sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)



# command = r.recognize_google(audio, language="ru-RU").lower()
# print(command)

command = input("Ввести: ")

command_list = ["го кодить", "хойка и моды", "система 60"]

# if command in command_list:
#     os.startfile(program['VS_code'])
#     os.startfile(program['System_60'])
if command in command_list:
    as_list()