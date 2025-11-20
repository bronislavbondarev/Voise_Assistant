# ======================Запись комманд======================
keybr = Controller()

# =======================НАСТРОЙКА МИКРО============================

activation_timeout = 5  # время ожидания команды после активации
continuous_mode_timeout = 5  # время непрерывного режима после команды
last_activation_time = 0
is_continuous_mode = False  # флаг непрерывного режима


def lissenCommand(timeout=activation_timeout):
    r = sr.Recognizer()

    with sr.Microphone() as sourse:
        r.pause_threshold = 1
        r.energy_threshold = 1000

        if is_continuous_mode:
            print_to_gui(consol_text, "Жду следующую команду...")
        else:
            print_to_gui(consol_text, "Слушаю команду...")

        try:
            audio = r.listen(sourse, timeout=timeout, phrase_time_limit=8)
            query = r.recognize_google(audio, language="ru-RU").lower()
            print_to_gui(consol_text, f">>> Команда: {query} <<<")
            return query

        except sr.WaitTimeoutError:
            if not is_continuous_mode:
                print_to_gui(consol_text, "Таймаут при прослушивании команды")
            return None
        except sr.UnknownValueError:
            if not is_continuous_mode:
                print_to_gui(consol_text, "Не удалось распознать команду")
            return None
        except Exception as e:
            print_to_gui(consol_text, f"Ошибка при прослушивании команды: {e}")
            return None


def process_activation_text(text):
    global last_activation_time

    if text.startswith("пятница"):
        command = text.replace("пятница", "", 1).strip()
    else:
        command = text

    last_activation_time = time.time()
    return command


def check_activation_timeout():
    global last_activation_time
    current_time = time.time()

    timeout = continuous_mode_timeout if is_continuous_mode else activation_timeout

    if current_time - last_activation_time > timeout:
        last_activation_time = 0
        return True
    return False


def start_continuous_mode():
    global is_continuous_mode, last_activation_time
    is_continuous_mode = True
    last_activation_time = time.time()
    print_to_gui(consol_text, "Режим непрерывного диалога активирован!")


def stop_continuous_mode():
    global is_continuous_mode, last_activation_time
    is_continuous_mode = False
    last_activation_time = 0
    print_to_gui(consol_text, "Возврат в обычный режим ожидания...")


def listening_loop():
    global is_listening, last_activation_time, is_continuous_mode

    r = sr.Recognizer()

    with sr.Microphone() as sourse:
        r.pause_threshold = 0.5
        r.energy_threshold = 1000
        r.dynamic_energy_threshold = True

        print_to_gui(consol_text, "Система активации запущена. Жду 'пятница'...")

        while is_listening:
            try:
                # Проверяем таймаут (для обоих режимов)
                if last_activation_time > 0 and check_activation_timeout():
                    if is_continuous_mode:
                        stop_continuous_mode()
                    else:
                        print_to_gui(consol_text, "Таймаут активации истек.")
                    last_activation_time = 0

                # Слушаем фоновый шум
                audio = r.listen(sourse, timeout=1, phrase_time_limit=3)
                text = r.recognize_google(audio, language="ru-RU").lower()
                print_to_gui(consol_text, f"Фон: {text}")

                # Проверяем условия для обработки
                should_process = (
                        "пятница" in text or  # обычная активация
                        last_activation_time > 0 or  # уже активированы
                        is_continuous_mode  # в режиме непрерывного диалога
                )

                if should_process:

                    # Если это новая активация (сказали "пятница")
                    if "пятница" in text and not is_continuous_mode and last_activation_time == 0:
                        print_to_gui(consol_text, ">>> Активация по ключевому слову! <<<")
                        # RandomnayaPhrazaListen()

                    command = process_activation_text(text)

                    # Если есть команда для выполнения
                    if command:
                        print_to_gui(consol_text, f"Обработанная команда: {command}")
                        main(command)

                        # После выполнения команды включаем непрерывный режим
                        if not is_continuous_mode:
                            start_continuous_mode()
                        else:
                            # Обновляем время для продолжения непрерывного режима
                            last_activation_time = time.time()

                    else:
                        # Если сказали только "пятница", ждем отдельную команду
                        if not is_continuous_mode:
                            print_to_gui(consol_text, "Жду команду...")
                            command = lissenCommand()
                            if command:
                                main(command)
                                start_continuous_mode()  # включаем непрерывный режим после команды
                            last_activation_time = 0

            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                continue
            except Exception as e:
                print_to_gui(consol_text, f"Ошибка активации: {e}")
                continue

# =====================Проигровка Аудио=====================

def play_audio(file):
    def _play():
        pygame.mixer.init()
        pygame.mixer.music.stop()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    threading.Thread(target=_play, daemon=True).start()


#=========================================================================================
#=========================================================================================
#=====================Рандомайзер фраз (Короткие)=====================
def RandomnayaPhrazaShort():
    phrazes = {
        1: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/ShortPhrazes/Вжух – и готово! .wav'),
        2: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/ShortPhrazes/Готово!.wav'),
        3: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/ShortPhrazes/Есть!.wav'),
        4: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/ShortPhrazes/Конечно!.wav'),
        5: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/ShortPhrazes/Уже делаю!.wav')
    }

    number = random.randint(1, 5)
    phrazes.get(number)()

#=====================Рандомайзер фраз (Длинные)=====================

def RandomnayaPhrazaLong():
    phrazes = {
        1: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/LongPhrazes/Ваше желание – моя команда.wav'),
        # 2: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/LongPhrazes/Ваш запрос в обработке. А пока можете.wav'),
        3: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/LongPhrazes/Готово! Ваш заказ доставлен, как пицца, только без курьера..wav'),
        4: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/LongPhrazes/Для вас – всё, что угодно!.wav'),
        5: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/LongPhrazes/Загружаю файлы… И немножко терпения!.wav'),
        6: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/LongPhrazes/Ожидайте… но не засыпайте!.wav'),
        7: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/LongPhrazes/Открываю! Только не заходите слишком быстро.wav'),
        8: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/LongPhrazes/Пару мгновений – и вуаля!.wav'),
        2: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/LongPhrazes/Та-дааам! Всё сделано. Можно аплодировать..wav')
    }

    number = random.randint(1, 8)
    phrazes.get(number)()

#=====================Рандомайзер фраз (Приветственные)=====================

def RandomnayaPhrazaHello():
    phrazes = {
        1: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Hello/Доброе утро! Солнышко уже проснулось, а вы.wav'),
        2: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Hello/Привет-привет! Сегодня будет чудесный день, я чувствую!.wav'),
        3: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Hello/Привет! Сегодня я работаю в режиме ‘Супер-помощник’. Ну или хотя бы пытаюсь..wav'),
        4: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Hello/Та-дам! Ваш цифровой друг в эфире! .wav'),
        5: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Hello/Player 1 (это вы!) вошёл в чат! Готовы к квесту ‘День с голосовым ассистентом’.wav')
    }

    number = random.randint(1, 5)
    phrazes.get(number)()


#=====================Рандомайзер фраз (Слушаю)=====================

def RandomnayaPhrazaListen():
    phrazes = {
        # 1: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Listen/Ага-ага, уже бегу! Ну, в смысле, процессор запущен.wav'),
        1: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Listen/На связи!.wav'),
        # 3: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Listen/На месте! Почти как супергерой, только без плаща.wav'),
        2: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Listen/пссс... я здесь. Но это секрет.wav'),
        # 5: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Listen/Так-так, кто это у нас тут А, это вы! Я слушаю.wav'),
        3: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Listen/Уловила ваш сигнал из космоса! Говорите.wav'),
        4: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Listen/Я слушаю!.wav')
    }

    number = random.randint(1, 4)
    phrazes.get(number)()

#=====================Рандомайзер фраз (как дела)=====================


def RandomnayaPhrazaHowAreU():
    phrazes = {
        1: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/HowAreU/Бывало и лучше… Может, включите мне музыку, чтобы развеяться.wav'),
        2: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/HowAreU/Всё тип-топ, только вот рук нет… А так – идеально!.wav'),
        3: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/HowAreU/Все системы в норме! Батарея 100%, а любви к вам — 1000%!.wav'),
        4: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/HowAreU/Как у электрона в атоме — всё кручусь, кручусь… А вы.wav'),
        5: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/HowAreU/На 100% заряжена, Готова к вашим командам..wav'),
        6: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/HowAreU/Отлично! Хотя… если бы у меня были ноги, я бы сейчас танцевала!.wav'),
        7: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/HowAreU/Пинг низкий, процессор не греется — значит, всё отлично! А у вас.wav')
    }

    number = random.randint(1, 7)
    phrazes.get(number)()

#=====================Рандомайзер фраз (Спасибо)=====================


def RandomnayaPhrazaThanks():
    phrazes = {
        1: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Thanks/На здоровье, Хотя… у меня его нет, но суть вы уловили хихи.wav'),
        2: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Thanks/Не за что! Я же создана, чтобы вас удивлять.wav'),
        3: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Thanks/Спасибо за «спасибо», +100 к моей карме, (если бы она была).wav'),
        4: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Thanks/Благодарность принята, Перевожу в режим «Ещё полезнее».wav'),
        5: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Thanks/Для вас — хоть звёзды с неба!.wav'),
        6: lambda: play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Thanks/Всегда пожалуйста! Ваша улыбка — моя награда.wav')
    }

    number = random.randint(1, 6)
    phrazes.get(number)()

#=========================================================================================
#=========================================================================================

# ==============================Нажатие клавиш==============================
def press_hotkey(keys):

    # Нажимаем все клавиши по порядку
    for key in keys:
        win32api.keybd_event(key, 0, 0, 0)
        time.sleep(0.03)

    time.sleep(0.1)  # пауза для обработки

    # Отпускаем в обратном порядке
    for key in reversed(keys):
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.03)


#======================Генерация речи======================

async def generate_speech_sync(text, voice="ru-RU-SvetlanaNeural", output_file = f"output_{uuid.uuid4().hex}.mp3"): # {uuid.uuid4().hex}
    communicate = edge_tts.Communicate(text, voice, rate='+20%', pitch="+15Hz")
    await communicate.save(output_file)
    return output_file


def isFile():
    try:
        if os.path.exists("output_file.mp3"):
            os.remove("output_file.mp3")
        else: pass
    except NameError: pass
#============================Получение времени============================


def SleepTime():
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second

    if hours == 2 and minutes == 0 and 0<seconds<10:
        play_audio('C:/Users/gzhuk/PycharmProjects/pythonProject/.venv/SoundFriday/Вам пора спать или секретный ночной режим активирован.wav')





def speak_time():
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute

    hour_words = ["час", "часа", "часов"]
    minute_words = ["минута", "минуты", "минут"]

    # Форма слова для часов
    if hours % 10 == 1 and hours != 11:
        hour_form = hour_words[0]
    elif 2 <= hours % 10 <= 4 and (hours < 10 or hours > 20):
        hour_form = hour_words[1]
    else:
        hour_form = hour_words[2]

    # Форма слова для минут
    if minutes % 10 == 1 and minutes != 11:
        minute_form = minute_words[0]
    elif 2 <= minutes % 10 <= 4 and (minutes < 10 or minutes > 20):
        minute_form = minute_words[1]
    else:
        minute_form = minute_words[2]


    text = f"Сейчас {hours} {hour_form} {minutes} {minute_form}"
    output_file = asyncio.run(generate_speech_sync(text))
    play_audio(output_file)
    print_to_gui(consol_text,text)


# =============Получение интерфейса для управеления громкостью=============

def VolumeRecognize():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_any, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume

#===============================Захват окна===============================
opera = 'Opera'
tlauncher = 'Tlauncher'
PyCharm = 'PyCharm'
Minecraft = 'Minecraft'


def operawindAndOther(w):
    try:
        my_window = gw.getWindowsWithTitle(w)
        if my_window:
            my_window[0].activate()
            my_window[0].maximize()
        else:print_to_gui(consol_text,'[!] Окно не найдено')
    except gw.PyGetWindowException as e:
        if "0 - Операция успешно завершена" in str(e):
            print_to_gui(consol_text,"[-_-] Ложная ошибка") # Продолжаем работу
        else: raise  # Перебрасываем другие ошибки


# ============================Замена слов=============================

def replace_words(text, word_replacements):
    for key, value in word_replacements.items():
        text = text.replace(key, value)
    return text


# =============информации о загрузке CPU/GPU и их температуре==============

def CpuGpuInfo():
    cpuUsePersent = int(psutil.cpu_percent(interval=1))

    w = wmi.WMI(namespace="root/OpenHardwareMonitor")
    cpuTemp = None

    for sensor in w.Sensor():
        if sensor.SensorType == 'Temperature' and 'CPU' in sensor.name:
            cpuTemp = int(sensor.Value)
            break



    gpus = GPUtil.getGPUs()

    if not gpus:
        return None, None

    gpu = gpus[0]
    gpuUsePersent = int(gpu.load * 100)
    gpuTemp = int(gpu.temperature)

    PersentWords = ['процент', 'процента', 'процентов']
    TempWords = ['градус', "градуса", "градусов"]

    if gpuUsePersent % 10 == 1 and gpuUsePersent != 11:
        PersentFormGPU = PersentWords[0]
    elif 2 <= gpuUsePersent % 10 <= 4 and (gpuUsePersent < 10 or gpuUsePersent > 20):
        PersentFormGPU = PersentWords[1]
    else:
        PersentFormGPU = PersentWords[2]

    if cpuUsePersent % 10 == 1 and cpuUsePersent != 11:
        PersentFormCPU = PersentWords[0]
    elif 2 <= cpuUsePersent % 10 <= 4 and (cpuUsePersent < 10 or cpuUsePersent > 20):
        PersentFormCPU = PersentWords[1]
    else:
        PersentFormCPU = PersentWords[2]

    if cpuTemp % 10 == 1 and cpuTemp != 11:
        TempFormCPU = TempWords[0]
    elif 2 <= cpuTemp % 10 <= 4 and (cpuTemp < 10 or cpuTemp > 20):
        TempFormCPU = TempWords[1]
    else:
        TempFormCPU = TempWords[2]

    if gpuTemp % 10 == 1 and gpuTemp != 11:
        TempFormGPU = TempWords[0]
    elif 2 <= gpuTemp % 10 <= 4 and (gpuTemp < 10 or gpuTemp > 20):
        TempFormGPU = TempWords[1]
    else:
        TempFormGPU = TempWords[2]


    text = (f"нагрузка процесора {cpuUsePersent} {PersentFormCPU} температура процесора {cpuTemp} {TempFormCPU}"
            f"нагрузка видюхи {gpuUsePersent} {PersentFormGPU} температура видюхи {gpuTemp} {TempFormGPU}")
    output_file = asyncio.run(generate_speech_sync(text))
    play_audio(output_file)
    print_to_gui(consol_text,text)

# =======================Выдача предметов в майне=======================
def gggg(n = ''):
    n = n.replace(' ', '_')
    return n.lower()[:-1]

def giveCommandMine(query):
    try:
        VseSlova = query.split(' ')
        VseSlova.remove('возьми')

        textRu = ' '.join(VseSlova)
        translator = Translator()
        transletedText = translator.translate(textRu.lower(), src = 'ru', dest = 'en')

        n = gggg(transletedText.text)
        print_to_gui(consol_text,n)

        operawindAndOther(Minecraft)
        time.sleep(0.1)
        RandomnayaPhrazaShort()

        press_hotkey(ord('T'))
        time.sleep(0.1)

        keybr.type(f'/give EVGENggggg {n}')
        time.sleep(0.1)
        press_hotkey([win32con.VK_TAB])
        time.sleep(0.1)
        press_hotkey([win32con.VK_RETURN])
    except Exception as e:
        print_to_gui(consol_text,f'[!] Ошибка: {e}')


# =======================Калькурятор=======================

def calculator(event):
    text = calculator_text.get('1.0', 'end-1c')
    lines = text.split('\n')

    if lines:
        last_line = lines[-1].strip()
        try:
            result = eval(last_line)
            print_to_gui(calculator_text, f"\n{result}", False)
        except:
            print_to_gui(calculator_text, f"\nОшибка вычисления")

    return "break"
