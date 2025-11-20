import os
from cProfile import label
from dataclasses import replace
from ensurepip import bootstrap
from time import sleep
from webbrowser import Opera
from xml.sax import parse

from Demos.RegCreateKeyTransacted import *
from PIL.ImageOps import expand
from pyautogui import press
from pynput.keyboard import *

import pygetwindow as gw
import pyautogui as pg
import speech_recognition as sr
import webbrowser
import sys
import time
import keyboard
import subprocess
import pygame
import threading
import random
import win32api
import win32con
from pywin.scintilla.formatter import Style
from selenium.webdriver.common.devtools.v135.fetch import continue_request
from sympy.polys.polyconfig import query
from win32comext.shell.demos.IShellLinkDataList import console_props
from win32con import VK_SHIFT, VK_F10
from win32timezone import *

import datetime
import pyttsx3

import psutil
import wmi
import GPUtil

import uuid
import asyncio
import edge_tts
import tempfile
import ctypes
import glob
from pathlib import Path
import sounddevice as sd

import torch
import sounddevice as sd
from omegaconf import OmegaConf
import torchaudio
from sympy.codegen.ast import break_
from googletrans import Translator

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as bs
from ttkbootstrap.constants import *
from ttkbootstrap.icons import Icon
from ttkbootstrap.style import Style
import re
#Импортируем массив со словесным представлением чисел и строку с этими числами
from Friday_data.py import words
from Friday_data.py import numbers

word_replacements = {
    "плюс": "+", "минус": "-",
    "умножить": "*", "х": "*", "разделить": "/",
    "равно": "=",
    "скобка открывается": "(", "скобка закрывается": ")",
    "точка": ".",
    "корень": "**0.5"
}

# ====================Создание окна для пятницы====================
# ====================Создание окна для пятницы====================
# ====================Создание окна для пятницы====================

is_listening = False
listening_thread = None

from Friday_window_setup.py import setupGUI

def run():
    wind = setupGUI()
    calculator_text.bind("<Return>", calculator)
    def on_closing():
        global is_listening
        is_listening = False
        wind.quit()
        wind.destroy()

    wind.protocol("WM_DELETE_WINDOW", on_closing)
    wind.mainloop()



from Friday_funcs.py import lissenCommand, process_activation_text, check_activation_timeout, start_continuous_mode, stop_continuous_mode, listening_loop, play_audio, _play, RandomnayaPhrazaShort, RandomnayaPhrazaHello,
RandomnayaPhrazaListen, RandomnayaPhrazaHowAreU, RandomnayaPhrazaThanks, press_hotkey, generate_speech_sync, isFile, SleepTime, speak_time, VolumeRecognize,
operawindAndOther, replace_words, CpuGpuInfo, gggg, giveCommandMine, calculator



# ===========================Главный функционал===========================
# ===========================Главный функционал===========================
# ===========================Главный функционал===========================
# ===========================Главный функционал===========================
keybr = Controller()

def main(query):
    SleepTime()

    #=============================Напиши в тг=============================

    if 'напиши' in query:
        nameApp = query.split(' ')
        if 'пожалуйста' in query:
            nameApp.remove('пожалуйста')
        nameApp.remove('напиши')
        indx = len(nameApp) - 1
        tochonado = nameApp[indx]
        tochonado1 = tochonado[::-1]
        tochonado2 = tochonado1[1:]
        tochonado3 = tochonado2[::-1]
        os.startfile('C:/Users/gzhuk/AppData/Roaming/Telegram Desktop/Telegram.exe')
        RandomnayaPhrazaShort()
        time.sleep(2)
        keyboard.send('esc')
        time.sleep(0.2)
        press_hotkey([win32con.VK_CONTROL, ord('F')])
        keybr.type(tochonado3)
        time.sleep(1.6)
        press_hotkey([win32con.VK_RETURN])

    # ================================печать текста================================
    if any(x in query for x in ('пиши','запиши')):
        text = replace_words((query[5:]), word_replacements)
        keybr.type(text)


    # ================================дагностика системы================================
    if 'диагностик' in query and 'систем' in query:
        CpuGpuInfo()


    # ================================взятие предметов в майнкрафт================================
    if 'возьми' in query:
        giveCommandMine(query)


    # ================================Запуск работы скрипта================================
    if 'запуск' in query:
        operawindAndOther(PyCharm)
        press_hotkey([win32con.VK_SHIFT, win32con.VK_F10])


    # ================================завершение работы скрипта================================
    if 'завершение' in query:
        operawindAndOther(PyCharm)
        press_hotkey([win32con.VK_CONTROL, win32con.VK_F2])


    # ================================переключение окон================================
    if 'окно' in query:
        press_hotkey([win32con.VK_LWIN, win32con.VK_SHIFT, win32con.VK_RIGHT])


    #============================Поиск в приложениях============================
    if 'поиск' in query:
        press_hotkey([win32con.VK_CONTROL, ord('F')])
        time.sleep(0.2)
        keybr.type(query[6:])
        RandomnayaPhrazaShort()

    if "тут" in query:
        RandomnayaPhrazaListen()

    #============================Счёт============================
    if 'считай' in query:
        primer = query.split(' ')
        if "посчитай" in primer:
            primer.remove('посчитай')
        else: primer.remove('считай')
        if "пожалуйста" in primer:
            primer.remove("пожалуйста")

        primer = ''.join(primer)
        primer = replace_words(primer, word_replacements)
        try:
            result = eval(primer)
            print_to_gui(calculator_text, f"{primer}\n{result}", False)
            RandomnayaPhrazaShort()
        except:
            print_to_gui(calculator_text, f"\nОшибка вычисления")


    #============================Таймер============================
    if 'таймер' in query and 'отмен' in query:
        stop_timer()



    if 'таймер' in query:
        time_mas = {"минут": 60, "мин": 60, "часа": 3600, "час": 3600, "сек": 1, "секунд": 1}

        time_text = ""
        for i in query.split(' '):
            if i in words:
                time_text += str(words.index(i))
            elif i in nubmers:
                time_text += str(i)
            if i in time_mas:
                time_text += f"*{time_mas[i]} + "

        time_text = time_text[:-2]
        if time_text:
            start_timer(eval(time_text))


    #============================Таймер============================
    if 'отключение' in query:
        toggle()

    # ===================================Общение===================================
    elif 'привет' in query or 'добр' in query and any(x in query for x in ('утро','ночь', 'вечер', "день")):
        RandomnayaPhrazaHello()

    elif 'дела' in query and 'как' in query:
        RandomnayaPhrazaHowAreU()

    elif any(x in query for x in ('нормально' ,'хорошо','отлично','прекрасно')):
        play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Ну вот и отлично, хи-хик.wav')

    # elif 'пятница' in query and ('плохо' in query or 'так себе' in query or 'могло' in query or 'лучше' in query):
    #     play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/')

    elif any(x in query for x in('благодарю','молодец', 'спасибо')):
        RandomnayaPhrazaThanks()


    # =============================Поиск в интeрнeтe=============================
    elif 'найди' in query:

        operawindAndOther(opera)
        time.sleep(0.5)
        keyboard.press_and_release('ctrl+t')
        time.sleep(0.5)
        keyboard.press_and_release('ctrl+l')
        time.sleep(0.2)
        play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Ищу, секундочкуу.wav')
        keybr.type(query[5:])
        keyboard.send('enter')
        time.sleep(1.1)
        play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Оо, нашла, всё как и просили.wav')



    # elif 'пятница' in query and 'да ' in query:
    #     play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/отлично, можете апладировать хи-хи.wav')
    #
    # elif 'пятница' in query and 'нет' in query:
    #     play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/уупссс. Давайте ещё разок .wav')


    #=============================Открой приложение=============================

    elif 'открой' in query:
        nameApp = query.split(' ')
        if 'пожалуйста' in query:
            nameApp.remove('пожалуйста')
            if 'открой-ка' in query:
                nameApp.remove('открой-ка')
            if 'открой' in query:
                nameApp.remove('открой')
            else: pass
        indx = len(nameApp) - 1
        press_hotkey([win32con.VK_LWIN])  # Win down
        time.sleep(0.2)
        keybr.type(nameApp[indx])
        time.sleep(0.2)
        press_hotkey([win32con.VK_RETURN])   # Win up
        RandomnayaPhrazaShort()

    # ============================Py to exe (конвертация)=============================

    if 'конвертация' in query:
        operawindAndOther(PyCharm)
        press_hotkey([win32con.VK_MENU, win32con.VK_F12])
        time.sleep(1)
        keybr.type('auto-py-to-exe')
        time.sleep(1)
        press_hotkey([win32con.VK_RETURN])
        RandomnayaPhrazaLong()



    #=============================Удалние символов/слов/всего=============================


    if query == 'сотри' or query == 'удали':
        col = 1
        for i in query.split(' '):
            if i in words:
                col = int(words.index(i))
            elif i in nubmers:
                col = int(i)
        for x in range(col):
            press_hotkey([win32con.VK_BACK])



    if 'слов' in query and any(x in query for x in ('сотри','стерай' ,'удали')):
        col = 1
        for i in query.split(' '):
            if i in words:
                col = int(words.index(i))
            elif i in nubmers:
                col = int(i)
        for x in range(col):
            press_hotkey([win32con.VK_CONTROL, win32con.VK_BACK])



    if 'всё' in query and any(x in query for x in ('сотри','стирай' ,'удали')):
        press_hotkey([win32con.VK_CONTROL, ord('A'), win32con.VK_BACK])


    #============================Пдтверждение==================================

    if any(x in query for x in ('enter', 'подтверди', "верно")):
        press_hotkey([win32con.VK_RETURN])
        RandomnayaPhrazaShort()


    #============================Сохранение==================================

    if any(x in query for x in ('сохран', 'control s')):
        press_hotkey([win32con.VK_CONTROL, ord('S')])
        RandomnayaPhrazaShort()


    #============================Копирование и вставка==================================

    if any(x in query for x in ('копировать', 'control c', 'ctrl c')):
        press_hotkey([win32con.VK_CONTROL, ord('C')])
        RandomnayaPhrazaShort()



    if any(x in query for x in ('вставить', 'control v', 'ctrl v')):
        press_hotkey([win32con.VK_CONTROL, ord('V')])
        RandomnayaPhrazaShort()


    #============================Все окна==================================

    if 'окна' in query:
        press_hotkey([win32con.VK_LWIN, win32con.VK_TAB])
        RandomnayaPhrazaShort()

    #===========================Навигация стрелочками===========================

    if any(x in query for x in ('вправо', 'влево', "вверх", "вниз", "ниже", "выше", "лев", "прав")):
        myKey = Key.right
        col = 1
        direction_mapping = {
            'вправо': Key.right,'право': Key.right,
            'влево': Key.left,'лев': Key.left,
            'вверх':Key.up,'выше':Key.up,
            'вниз': Key.down,'ниже': Key.down
        }
        for i in query.split(' '):
            if i in 'вправовлевовверхвнизнижевышелевправо':
                myKey = direction_mapping.get(i)
            elif i in nubmers:
                col = int(i)
            elif i in words:
                col = int(words.index(i))

        for x in range(col):
            keybr.press(myKey)
            keybr.release(myKey)



    # =============================а через=============================

    if 'выключение через' in query:
        try:
            # Извлекаем последнее слово (предполагая, что это число)
            minutes = int(query.split(' ')[-1])
            seconds = minutes * 60
            os.system(f"shutdown /s /t {seconds}")
            print_to_gui(consol_text,f"⚠️⚠️⚠️Компьютер выключится через {minutes} минут⚠️⚠️⚠️")
        except (ValueError, IndexError):
            print_to_gui(consol_text,"⚠️Не удалось распознать время выключения")


    if 'отменить выключение' in query or 'отмени выключение' in query or 'отмена' in query:
        os.system("shutdown -a")
        RandomnayaPhrazaLong()


    # ============================Получение времени============================

    if (('который' in query  and  'час' in query) or 'сколько врем' in query):
        speak_time()




    # =================================Приколы=================================

    if 'напиши' in query and 'иль' in query:
        a = random.randint(1,3)

        os.startfile('C:/Users/gzhuk/AppData/Roaming/Telegram Desktop/Telegram.exe')
        RandomnayaPhrazaLong()
        time.sleep(2.5)
        keyboard.send('esc')
        time.sleep(0.1)
        keyboard.send('ctrl+f')
        time.sleep(0.5)
        keybr.type('илюша')
        time.sleep(0.1)
        keyboard.send('enter')
        time.sleep(1)
        if a == 1:
            time.sleep(0.1)
            keybr.type('Пошёл на х...')
        elif a == 2:
            time.sleep(0.1)
            keybr.type('Илья ЛОХ')
        elif a == 3:
            time.sleep(0.1)
            keybr.type('Илья красавчиГ')
        time.sleep(0.2)
        # keyboard.send('enter')




    # ====================Открытие ютуба=============================
    if "youtube" in query:
        webbrowser.open('https://www.youtube.com')
        RandomnayaPhrazaShort()

    # ====================Открытие диспетчера========================
    if "диспетчер" in query:
        keyboard.send("ctrl+shift+esc")
        RandomnayaPhrazaShort()

    # ====================Открытие Телеги============================
    if 'телега' in query:
        os.startfile('C:/Users/gzhuk/AppData/Roaming/Telegram Desktop/Telegram.exe')
        RandomnayaPhrazaShort()

    # ====================Открытие Загрузок============================
    if any(x in query for x in ('загрузки','проводник')):
        os.startfile('C:/Users/gzhuk/Downloads')
        RandomnayaPhrazaShort()


    # ====================Открытие Pycharm============================
    if 'пайчарм'in query or 'питон'in query:
        os.startfile('C:/Program Files/JetBrains/PyCharm Community Edition 2024.2.4/bin/pycharm64.exe')
        RandomnayaPhrazaShort()



    # ====================Сворачивание окон и разворачивание=====================
    if 'свернуть'in query or 'сверни'in query:
        keyboard.send('win+down')
        time.sleep(0.1)
        keyboard.send('win+down')
        RandomnayaPhrazaShort()

    if 'разверн' in query:
        keyboard.send('win+up')
        RandomnayaPhrazaShort()


    if 'обратно' in query:
        press_hotkey([win32con.VK_MENU, win32con.VK_TAB])
        time.sleep(0.1)
        press_hotkey([win32con.VK_LWIN, win32con.VK_UP])
        RandomnayaPhrazaShort()

    if query == 'закрой' or query == 'закрыть':
        keyboard.send('alt+f4')
        RandomnayaPhrazaShort()


    # ====================Выйти на рабочий стол и обратно=====================
    if 'рабочий' in query and 'стол'in query:
        press_hotkey([win32con.VK_LWIN, ord('D')])
        RandomnayaPhrazaShort()




    # ============================================================================================================
    # ============================================================================================================
    # ====================Открытие Музыки(YouTube)============================

    if 'музыка'in query or 'музыки'in query:
        webbrowser.open('https://www.youtube.com/watch?v=QGsevnbItdU&list=RDQGsevnbItdU&start_radio=1')
        play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Вжух – и звучит музыка! Громко или потише.wav')

    # ====================Перелистывание музыки(YouTube)===================

    if any(x in query for x in ('мотай', 'листа', "матай", "листай")):
        operawindAndOther(opera)
        time.sleep(0.5)
        myKey = Key.right
        direct = {
            'вперёд': Key.right, 'назад': Key.left
        }
        col = 1
        for i in query.split(' '):
            if i == 'вперёд' or i == 'назад':
                myKey = direct.get(i)
            if i in nubmers:
                col = int(i)
            if i in words:
                col = int(words.index(i))
        for x in range(col):
            keybr.press(myKey)
            keybr.release(myKey)
        RandomnayaPhrazaShort()


    if 'полный экран' in query:
        operawindAndOther(opera)
        time.sleep(0.5)
        press_hotkey([ord('F')])
        RandomnayaPhrazaShort()


    if 'вперёд'in query:
        operawindAndOther(opera)
        time.sleep(0.5)
        keyboard.send('shift+n')
        RandomnayaPhrazaShort()


    if 'назад'in query:
        operawindAndOther(opera)
        time.sleep(0.5)
        keybr.press(Key.shift)
        keybr.press('p')
        keybr.release(Key.shift)
        keybr.release('p')
        RandomnayaPhrazaShort()

    if any(x in query for x in ('стоп', 'хватит')):
        operawindAndOther(opera)
        time.sleep(0.6)
        keyboard.send('space')
        RandomnayaPhrazaShort()


    if any(x in query for x in('следующая', 'дальше')):
        operawindAndOther(opera)
        time.sleep(0.5)
        keyboard.send('ctrl+2')
        time.sleep(0.6)
        keyboard.send('shift+n')
        RandomnayaPhrazaShort()

    if any(x in query for x in('другая', 'предыдущая')):
        operawindAndOther(opera)
        time.sleep(0.5)
        keyboard.send('ctrl+2')
        time.sleep(0.6)
        press_hotkey([win32con.VK_SHIFT, ord('P')])
        RandomnayaPhrazaShort()

    if any(x in query for x in('пауза', 'play')):
        operawindAndOther(opera)
        time.sleep(0.6)
        keyboard.send('ctrl+2')
        time.sleep(0.2)
        keyboard.send('space')
        RandomnayaPhrazaShort()


    if any(x in query for x in('обнови', 'перезагрузить')):
        operawindAndOther(opera)
        time.sleep(0.6)
        keyboard.send('f5')
        RandomnayaPhrazaShort()



    # ====================Скачать музыку с ютуба=====================
    if any(x in query for x in('скачать', 'скачай')):
        operawindAndOther(opera)
        time.sleep(0.5)
        if 'муз' in query:
            keyboard.send('ctrl+2')
            time.sleep(0.2)

        press_hotkey([win32con.VK_CONTROL, ord('L')])
        time.sleep(0.2)
        press_hotkey([win32con.VK_CONTROL, ord('C')])
        time.sleep(0.5)

        os.startfile('C:/Users/gzhuk/AppData/Roaming/Telegram Desktop/Telegram.exe')
        RandomnayaPhrazaLong()
        time.sleep(4)

        press_hotkey([win32con.VK_LWIN, win32con.VK_UP])
        time.sleep(0.5)
        press_hotkey([win32con.VK_ESCAPE])
        time.sleep(0.2)

        press_hotkey([win32con.VK_CONTROL, ord('F')])
        time.sleep(0.2)
        keybr.type('скачать с')
        time.sleep(1)
        keyboard.send('enter')
        time.sleep(0.2)
        press_hotkey([win32con.VK_CONTROL, ord('V')])
        time.sleep(0.2)
        keyboard.send('enter')
    # ============================================================================================================
    # ============================================================================================================




    # ====================Запус майнкрафта====================
    if 'играть'in query:
        os.startfile('C:/Users/gzhuk/AppData/Roaming/.minecraft/TLauncher.exe')
        play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Играем! Только не забывайте моргать..wav')


    if 'войти в игру' in query:

        tl_wind = gw.getWindowsWithTitle('TLauncher')
        if tl_wind:
            win2 = tl_wind[0]
            win2.maximize()
            win2.activate()
            time.sleep(1)
            pg.click(681, 1043)
        else: print_to_gui(consol_text,'Окно не найдено')
        play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Погружение начинается….wav')




    # =====================Закрой вкладку=====================
    if any(x in query for x in('закрой', 'удали')) and 'вклад' in query:
        col = 1
        try:
            operawindAndOther(opera)
            time.sleep(0.5)
            for i in query.split(' '):
                if i in nubmers:
                    col = i
                if i in words:
                    col = int(words.index(i))
            for i in range(col):
                time.sleep(0.2)
                press_hotkey([win32con.VK_CONTROL, ord('W')])

            else:
                press_hotkey([win32con.VK_CONTROL, ord('W')])
            RandomnayaPhrazaShort()
        except ValueError as e:
            print_to_gui(consol_text,f'[!] {e}')



    # =====================открой вкладку <номeр>=====================
    if 'вкладка' in query:
        num = 1
        try:
            operawindAndOther(opera)
            time.sleep(0.5)
            if query[15:] == '' or query[15:] == ' ':
                keybr.press(Key.ctrl)
                keybr.press('1')
                keybr.release('1')
                keybr.release(Key.ctrl)
            for i in query.split(' '):
                if i in words:
                    num = int(words.index(i))
                if i in nubmers:
                    num = i
                keybr.press(Key.ctrl)
                keybr.press(f'{num}')
                keybr.release(f'{num}')
                keybr.release(Key.ctrl)
            RandomnayaPhrazaShort()
        except ValueError: print_to_gui(consol_text,f'[!] {e}')

    # =====================открой вкладку <номeр>=====================
    if 'верни' in query and 'вклад' in query:
        operawindAndOther(opera)
        time.sleep(0.5)
        keyboard.send(f'ctrl+shift+t')
        RandomnayaPhrazaShort()


    # ============================скриншот============================
    if ('скрин' or 'скриншот') in query:
        press_hotkey([win32con.VK_LWIN, win32con.VK_SHIFT, ord('S')])



    # =================Переключение на колонки===================
    if 'колонки'in query or 'колонкa'in query:
        subprocess.run(["powershell","Set-AudioDevice -Index (Get-AudioDevice -List | Where-Object Name -Like '*High Definition Audio Device*').Index"])
        RandomnayaPhrazaShort()


    if 'наушники'in query:
        subprocess.run(["powershell","Set-AudioDevice -Index (Get-AudioDevice -List | Where-Object Name -Like '*Динамики (USB Audio Device)*').Index"])
        RandomnayaPhrazaShort()


    # =================Показ иконок===================
    if any(x in query for x in('покажи','иконки', 'приложения', 'спрячь')):
        press_hotkey([win32con.VK_SHIFT, win32con.VK_F10])
        time.sleep(0.1)

        press_hotkey([win32con.VK_DOWN])
        press_hotkey([win32con.VK_RETURN])
        time.sleep(0.1)

        press_hotkey([win32con.VK_UP])
        press_hotkey([win32con.VK_RETURN])

    # ====================Упрвление яркостью====================
    if 'яркость' in query and any(x in query for x in('ноль','0', 'выключи')):
        win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)  # Win down
        win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)  # Win down
        keybr.press('1')
        keybr.release('1')
        win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)  # Win up
        win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)  # Win up
        RandomnayaPhrazaShort()


    if 'яркость' in query and any(x in query for x in('фулл','100', 'включи', 'сто', 'макс')):
        win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)  # Win down
        win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)  # Win down
        keybr.press('2')
        keybr.release('2')
        win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)  # Win up
        win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)  # Win up
        RandomnayaPhrazaShort()


    if 'мониторы' in query and any(x in query for x in('отключи','выруби', 'выключи', 'выкл')):
        win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)  # Win down
        win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)  # Win down
        keybr.press('3')
        keybr.release('3')
        win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)  # Win up
        win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)  # Win up
        RandomnayaPhrazaShort()



    # ====================Упрвление громкостью====================
    if 'тише' in query or query == 'убавь':
        for i in range(10):
            pg.press('volumedown')

    if 'громче' in query or query == 'прибавь':
        for i in range(10):
            pg.press('volumeup')

    if 'убавь на' in query:
        try:
            query = query.split(' ')
            for i in range(int(query[-1])):
                for x in range(5):
                    pg.press('volumedown')
        except ValueError: print_to_gui(consol_text,f'[!] {e}')

    if 'прибавь на' in query:
        try:
            query = query.split(' ')
            for i in range(int(query[-1])):
                for x in range(5):
                    pg.press('volumeup')
        except ValueError: print_to_gui(consol_text,f'[!] {e}')

    if 'полная громкость' in query:
        for i in range(10):
            pg.press('volumeup')

    if query == 'mute' or 'выключи звук' in query:
        for i in range(10):
            pg.press('volumedown')


    if any(x in query for x in('перезагруз', 'перезапуск')) and 'систем' in query:
        operawindAndOther(PyCharm)
        press_hotkey([win32con.VK_SHIFT, win32con.VK_F10])
        time.sleep(1)
        press_hotkey([win32con.VK_RETURN])
        RandomnayaPhrazaShort()

    elif "молчи" in query or "заткнись" in query:
        toggle()

if __name__ == "__main__":
    run()
