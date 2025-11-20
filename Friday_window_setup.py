# ==============Вывод текста в текстовых полях==============
def print_to_gui(text, message, enter = True):
    if enter: text.insert(tk.END, message + "\n")
    else: text.insert(tk.END, message)
    text.see(tk.END)


# ==============Кнопки калькулятора==============
def on_button_click(button_text):
    current_text = calculator_text.get("1.0", "end-1c")

    if button_text == '=':
        lines = current_text.split('\n')

        last_expression = ""
        for line in reversed(lines):
            line = line.strip()
            if line and not line.startswith('='):
                last_expression = line
                break

        if last_expression:
            try:
                result = eval(last_expression)
                calculator_text.insert("end", f"\n{result}")
                calculator_text.see("end")
            except:
                calculator_text.insert("end", "\nОшибка вычисления!\n")
                calculator_text.see("end")
        else:
            calculator_text.insert("end", "\nНет выражения для вычисления\n")
            calculator_text.see("end")

    elif button_text == 'C':
        calculator_text.delete("1.0", "end")
        print_to_gui(consol_text, "***Калькулятор очищен***")

    elif button_text == '←':
        if len(current_text) > 0:
            calculator_text.delete("end-2c", "end-1c")
    else:
        calculator_text.insert("end", button_text)


# ==============Запуст и остановка ПЯТНИЦЫ==============
def toggle():
    global is_listening, listening_thread

    if not is_listening:
        is_listening = True
        startButton.config(text='STOP')
        print_to_gui(consol_text,"🎤 Начинаю прослушивание...")

        listening_thread = threading.Thread(target=listening_loop, daemon=True)
        listening_thread.start()
    else:
        is_listening = False
        startButton.config(text='START')
        print_to_gui(consol_text,"⏹️ Прослушивание остановлено")


# ==============Работа таймера==============
def parse_command():
    global is_timer_running
    if is_timer_running:
        messagebox.showwarning("Внимание", "Таймер уже запущен!")
        return

    timer_text = timer_entry.get().strip().lower()

    if not timer_text:
        messagebox.showerror("Ошибка", "Установите таймер!")
        return

    numbers = re.findall(r'\d+', timer_text)

    if not numbers:
        messagebox.showerror("Ошибка", "Время не найдено!")
        return

    time_value = int(numbers[0])

    if any(x in timer_text for x in ("сек", "секунд")):
        total_seconds = time_value
    elif any(x in timer_text for x in ("мин", "минут")):
        total_seconds = time_value * 60
    elif any(x in timer_text for x in ("час", "часов")):
        total_seconds = time_value * 3600
    else:
        total_seconds = time_value

    start_timer(total_seconds)

    timer_entry.delete(0, tk.END)


def start_timer(seconds):
    global is_timer_running, remaining_time, end_time, timer_thread
    if seconds <= 0:
        messagebox.showerror("Ошибка", "Время должно быть больше 0!")
        return

    is_timer_running = True
    remaining_time = seconds
    end_time = time.time() + seconds

    timer_thread = threading.Thread(target=timer_worker, daemon=True)
    timer_thread.start()

    messagebox.showinfo("Таймер запущен", f"Таймер установлен на {seconds} секунд")


def stop_timer():
    global is_timer_running
    if not is_timer_running:
        messagebox.showwarning("Внимание", "Таймер не запущен!")
        return

    is_timer_running = False
    time_display.config(text="00:00:00")
    messagebox.showinfo("Таймер остановлен", "Таймер был остановлен")


def timer_worker():
    global is_timer_running, remaining_time, end_time
    while is_timer_running and remaining_time > 0:
        remaining_time = max(0, end_time-time.time())

        hours = int(remaining_time // 3600)
        minutes = int((remaining_time % 3600) // 60)
        seconds = int(remaining_time % 60)

        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        wind.after(0, lambda: update_display(time_str))
        time.sleep(1)

    if is_timer_running:
        is_timer_running = False
        wind.after(0, timer_finished)


def update_display(time_str):
    time_display.config(text=time_str)


def timer_finished():
    time_display.config(text="00:00:00")
    messagebox.showinfo("Таймер завершён", "Время вышло!")


def setupGUI():
    global startButton, consol_text, calculator_text, is_timer_running, remaining_time, end_time, timer_thread, timer_entry, time_display, wind, timer_entry

    wind = bs.Window(themename="flatly") #
    wind.title('Friday')
    wind.geometry('800x400')
    wind.minsize(800, 400)
    wind.maxsize(1200, 600)
    wind.iconbitmap("friday.ico")

    style = wind.style

    style.configure("StartButton.TButton",
                    padding=(20, 15),
                    font=('Arial', 20),
                    background='DarkCyan',
                    foreground='white')

    style.configure("CalculatorButton.TButton",
                    padding=(10, 10),
                    font=('Arial', 18),
                    background='DarkCyan',
                    foreground='white')

    style.configure("Start_timer_button.TButton",
                    font=('Arial', 15), background='dark turquoise')
    style.configure("Stop_timer_button.TButton",
                    font=('Arial', 15), background='dark cyan')

    # ========================================Главная панель==================================================
    mainWind = bs.PanedWindow(wind, orient=HORIZONTAL)
    mainWind.pack(fill=BOTH, expand=True)

    # ========================================Левый контейнер==================================================
    left_conteiner = bs.Frame(mainWind)
    left_conteiner.configure(width=1)
    left_conteiner.pack_propagate(True)
    mainWind.add(left_conteiner, weight=4)

    startButton = bs.Button(left_conteiner, text="START", command = toggle, style="StartButton.TButton", takefocus=0)
    startButton.pack(pady = 50)

    # ========================================Правый контейнер==================================================
    right_conteiner = bs.Frame(mainWind)
    right_conteiner.configure(width=1)
    right_conteiner.pack_propagate(True)
    mainWind.add(right_conteiner, weight=10)

    # Создание вкладок
    notebook = bs.Notebook(right_conteiner, bootstyle='success')
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # ----------Вкладка 1----------
    tab1 = bs.Frame(notebook)
    notebook.add(tab1, text="Консоль")

    main_frame = bs.Frame(tab1, bootstyle = "dark")
    main_frame.pack(fill=BOTH, expand=YES, padx=10, pady=10)

    # Текстовое поле
    text_frame = bs.Frame(main_frame)
    text_frame.pack(fill=BOTH, expand=YES)

    # Скроллбар на вкладке
    main_scrollbar = bs.Scrollbar(text_frame, bootstyle='success-round')
    main_scrollbar.pack(side=RIGHT, fill=Y, padx=10)

    # Текстовое widget на вкладке
    consol_text = tk.Text(text_frame,yscrollcommand=main_scrollbar.set,bg="green1",fg="white",font=("Arial", 12),height=20)
    consol_text.pack(fill=BOTH, expand=YES)

    main_scrollbar.config(command=consol_text.yview)

    # ----------Вкладка 2----------
    tab2 = bs.Frame(notebook)
    notebook.add(tab2, text="Калькулятор")

    calculator_main_field = bs.PanedWindow(tab2, orient=HORIZONTAL)
    calculator_main_field.pack(fill=BOTH, expand=True)

    # <<< Калькулятор левый контейнер <<<
    calculator_left_conteiner = bs.Frame(calculator_main_field)
    calculator_left_conteiner.configure(width=1)
    calculator_left_conteiner.pack_propagate(False)
    calculator_main_field.add(calculator_left_conteiner, weight=1)

    left_calculator_filed = bs.Frame(calculator_left_conteiner)
    left_calculator_filed.pack(fill=BOTH, expand=YES, padx=10, pady=10)

    calculator_left_text_field = bs.Frame(left_calculator_filed)
    calculator_left_text_field.pack(fill=BOTH, expand=YES)

    scrollbar_calculator_left_text = bs.Scrollbar(calculator_left_text_field, bootstyle='success-round')
    scrollbar_calculator_left_text.pack(side=RIGHT, fill=Y, padx=10)

    calculator_text = tk.Text(calculator_left_text_field,yscrollcommand=scrollbar_calculator_left_text.set,bg="white",fg="white",font=("Arial", 17),height=20)
    calculator_text.pack(fill=BOTH, expand=YES)

    scrollbar_calculator_left_text.config(command=calculator_text.yview)


    # >>> Калькулятор правый контейнер >>>
    calculator_right_conteiner = bs.Frame(calculator_main_field)
    calculator_right_conteiner.configure(width=1)
    calculator_right_conteiner.pack_propagate(False)
    calculator_main_field.add(calculator_right_conteiner, weight=1)


    grid_button_container = bs.Frame(calculator_right_conteiner)
    grid_button_container.pack(fill=BOTH, expand=YES, padx=30, pady=15)

    button_texts = [
        'C', '*', '/', '←',
        '7', '8', '9', '+',
        '4', '5', '6', '-',
        '1', '2', '3', '.',
        '(', '0', ')', '='
    ]

    for i in range(20):
        row = (i // 4) + 1
        col = i % 4

        btn = bs.Button(grid_button_container,text=button_texts[i],width=3, takefocus=0, style="CalculatorButton.TButton",command=lambda text=button_texts[i]: on_button_click(text))
        btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")


    for i in range(7):
        grid_button_container.grid_rowconfigure(i, weight=1)
    for i in range(5):
        grid_button_container.grid_columnconfigure(i, weight=1)

    calculator_text.focus_set()


    # ------------Вкладка 3------------
    tab3 = bs.Frame(notebook)
    notebook.add(tab3, text="Таймер")

    timer_main_field = bs.Frame(tab3)
    timer_main_field.pack(fill=BOTH, expand=YES, padx=10, pady=10)

    is_timer_running = False
    remaining_time = 0
    end_time = None
    timer_thread = None

    time_display = bs.Label(timer_main_field, text='00:00:00', font=("Courier New", 32, "bold"), bootstyle='success')
    time_display.pack(pady=35)

    input_field = bs.Label(timer_main_field)
    input_field.pack(pady=40)

    input_timer_label = bs.Label(input_field, text='Установите время: ', font=("Arial", 13))
    input_timer_label.pack(side=LEFT, padx=(0, 10))

    timer_entry = bs.Entry(input_field, font=("Arial", 13))
    timer_entry.pack(side=LEFT)
    timer_entry.bind('<Return>',lambda e: parse_command())

    button_timer_field = bs.Frame(timer_main_field)
    button_timer_field.pack(pady=5)

    start_timer_button = bs.Button(button_timer_field, text = 'start', command=lambda: parse_command(), style='Start_timer_button.TButton', takefocus=0)
    start_timer_button.pack(side=LEFT, padx=5)
    start_timer_button = bs.Button(button_timer_field, text = 'stop', command=stop_timer, style='Stop_timer_button.TButton', takefocus=0)
    start_timer_button.pack(side=LEFT, padx=5)



    # -----------------------------
    return wind
