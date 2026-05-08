# Занятие 2. Создание графического интерфейса текстовой RPG на Python

---

## За текущее занятие должно быть понимание следующих элементов:

* графический интерфейс
* модульная структура проекта
* tkinter
* окно программы
* виджеты
* обработка событий
* разделение интерфейса и логики
* состояние игры
* инвентарь
* игровая карта
* панель информации
* защищённое текстовое поле
* архитектура проекта
* микро- и макроуровень программы

---

# Введение

На первом занятии была создана консольная текстовая игра.

Теперь задача состоит в том, чтобы перенести игровую логику в графическое окно и разделить проект на несколько файлов.

Это важный этап, потому что программа перестаёт быть одним длинным скриптом и начинает приобретать архитектуру.

В проекте появляются отдельные части:

* интерфейс;
* игровая логика;
* игровые данные;
* настройки внешнего вида;
* точка запуска.

Такой подход используется в реальных проектах, потому что он делает программу:

* понятнее;
* удобнее для изменения;
* пригодной для расширения;
* более устойчивой к ошибкам.

---

# Постановка задачи

Необходимо разработать графическую текстовую RPG.

Игра должна:

* запускаться из файла `main.py`;
* открывать графическое окно;
* выводить текст событий;
* принимать команды игрока;
* хранить состояние игры;
* показывать здоровье, золото, локацию и статус;
* отображать инвентарь;
* использовать отдельные файлы для логики, данных и настроек.

---

# Структура проекта

```text
PythonProject1/
│
├── main.py
├── ui.py
├── game_logic.py
├── data.py
├── settings.py
└── README.md
````

---

# Принципиальная схема проекта

```text
Пользователь
    │
    ▼
Поле ввода
    │
    ▼
ui.py
    │
    ▼
game_logic.py
    │
    ▼
data.py
```

---

# Схема интерфейса

```text
┌──────────────────────────────────────────────────────────────┐
│                        ВЕРХНЯЯ ПАНЕЛЬ                        │
│ Здоровье        Золото        Локация        Статус игры      │
└──────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────┬─────────────────┐
│                                            │                 │
│                                            │    INFO PANEL   │
│                                            │                 │
│              OUTPUT PANEL                  │    ИНВЕНТАРЬ    │
│                                            │                 │
│                                            │    факел        │
│                                            │    меч          │
│                                            │                 │
└────────────────────────────────────────────┴─────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                       НИЖНЯЯ ПАНЕЛЬ                          │
│                    поле ввода команды                        │
│                         кнопка                               │
└──────────────────────────────────────────────────────────────┘
```

---

# Главная идея занятия

```text
Интерфейс показывает игру.
Логика управляет игрой.
Данные описывают мир.
Настройки задают внешний вид.
```

---

# Архитектура проекта

```text
main.py
│
└── запуск программы


ui.py
│
├── создание окна
├── отображение интерфейса
├── обработка ввода
└── обновление интерфейса


game_logic.py
│
├── хранение состояния игры
├── обработка команд
├── изменение параметров
└── игровые правила


data.py
│
└── хранение карты мира


settings.py
│
├── цвета
├── размеры
└── шрифты
```

---



# Карта игрового мира

```text
              ┌──────────────┐
              │ Главный зал  │
              └──────┬───────┘
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
┌──────────────┐          ┌────────────────┐
│ Оружейная    │          │ Тёмный коридор │
│ меч          │          │ гоблин         │
└──────────────┘          └───────┬────────┘
                                  │
                                  ▼
                         ┌────────────────┐
                         │ Сокровищница   │
                         │ сундук         │
                         └────────────────┘
```

---

# ═══════════════════════════════════════════════════════════

# main.py

# ═══════════════════════════════════════════════════════════

## Назначение

Точка входа приложения.

Файл запускает графический интерфейс игры.

---

## Листинг

```
from ui import create_window

create_window()
```

---

## Структура запуска

```
main.py
    │
    ▼
create_window()
    │
    ▼
создание интерфейса
```

---

## Разбор

```
from ui import create_window

```

Импорт функции создания окна.

---

```
create_window()
```

Запуск интерфейса игры.

---

## Архитектурная роль

```
main.py
    ↓
точка запуска проекта
```

---

# ═══════════════════════════════════════════════════════════

# settings.py

# ═══════════════════════════════════════════════════════════

## Назначение

Файл хранит настройки интерфейса.

---

## Структура

```
settings.py
│
├── размеры окна
├── цвета
└── шрифты
```

---

## Листинг

```
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 750

BG_COLOR = "#0f172a"

PANEL_COLOR = "#020617"

TEXT_BG = "#111827"
TEXT_COLOR = "#00ff88"

ENTRY_BG = "#1e293b"
ENTRY_FG = "#ffffff"

BUTTON_BG = "#7c3aed"
BUTTON_ACTIVE = "#6d28d9"

FONT_MAIN = ("Consolas", 15)
FONT_PANEL = ("Consolas", 13)
FONT_TITLE = ("Consolas", 16)
```

---

## Разбор

```
WINDOW_WIDTH = 1100
```

Ширина окна.

---

```
BG_COLOR = "#0f172a"
```

Основной цвет интерфейса.

---

```
FONT_MAIN = ("Consolas", 15)
```

Основной шрифт приложения.

---

## Архитектурная роль

```
settings.py
    ↓
централизованное хранение настроек
```

---

# ═══════════════════════════════════════════════════════════

# data.py

# ═══════════════════════════════════════════════════════════

## Назначение

Файл содержит описание игрового мира.

---

## Структура игрового мира

```text id="uxo6ta"
rooms
│
├── hall
├── armory
├── corridor
└── treasury
```

---

## Структура комнаты

```text id="k08dba"
room
│
├── name
├── description
└── exits
```

---

## Листинг

```
rooms = {

    "hall": {
        "name": "Главный зал",

        "description":
        "Вы стоите в главном зале старого замка.",

        "exits": {
            "оружейная": "armory",
            "коридор": "corridor"
        }
    },

    "armory": {
        "name": "Оружейная",

        "description":
        "На полу лежит ржавый меч.",

        "exits": {
            "зал": "hall"
        }
    },

    "corridor": {
        "name": "Тёмный коридор",

        "description":
        "В темноте слышно рычание.",

        "exits": {
            "зал": "hall",
            "сокровищница": "treasury"
        }
    },

    "treasury": {
        "name": "Сокровищница",

        "description":
        "Перед вами огромный сундук с золотом.",

        "exits": {
            "коридор": "corridor"
        }
    }
}
```

---

## Разбор

```
"hall"
```

Внутренний идентификатор комнаты.

---

```
"name"
```

Название локации.

---

```
"description"
```

Описание комнаты.

---

```
"exits"
```

Список переходов.

---

## Логика перехода

```
идти оружейная
        │
        ▼
rooms[current_room]["exits"]
        │
        ▼
current_room = "armory"
```

---

## Карта мира

```
              ┌──────────────┐
              │ Главный зал  │
              └──────┬───────┘
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
┌──────────────┐          ┌────────────────┐
│ Оружейная    │          │ Тёмный коридор │
└──────────────┘          └───────┬────────┘
                                  │
                                  ▼
                         ┌────────────────┐
                         │ Сокровищница   │
                         └────────────────┘
```

---

## Архитектурная роль

```
data.py
    ↓
хранение игрового мира
```

---

# ═══════════════════════════════════════════════════════════

# game_logic.py

# ═══════════════════════════════════════════════════════════

## Назначение

Файл содержит игровую логику.

---

## Структура состояния игры

```
health
gold
inventory
current_room
game_over
goblin_alive
```

---

## Листинг состояния

```
from data import rooms


health = 100
gold = 0
inventory = ["факел"]

current_room = "hall"
game_over = False
goblin_alive = True


def get_status():
    return {
        "health": health,
        "gold": gold,
        "inventory": inventory,
        "room": rooms[current_room]["name"],
        "game_over": game_over
    }


def process_command(command):
    global health
    global gold
    global current_room
    global game_over
    global goblin_alive

    result = []

    command = command.lower().strip()

    if game_over:
        result.append("Игра окончена.")
        return result

    if command == "помощь":
        result.append("Команды:")
        result.append("осмотреться")
        result.append("идти <место>")
        result.append("взять меч")
        result.append("атаковать")
        result.append("открыть сундук")
        result.append("статус")

    elif command == "осмотреться":
        room = rooms[current_room]

        result.append(room["name"])
        result.append(room["description"])

        exits = ", ".join(room["exits"].keys())
        result.append(f"Выходы: {exits}")

        if current_room == "armory" and "меч" not in inventory:
            result.append("На полу лежит меч.")

        if current_room == "corridor" and goblin_alive:
            result.append("Перед вами стоит гоблин.")

        if "факел" in inventory:
            result.append("Факел освещает помещение.")

    elif command.startswith("идти "):
        place = command.replace("идти ", "")

        exits = rooms[current_room]["exits"]

        if place in exits:
            current_room = exits[place]
            room = rooms[current_room]

            result.append("Вы пришли в локацию:")
            result.append(room["name"])

            if current_room == "corridor" and goblin_alive:
                result.append("Гоблин преграждает путь.")
        else:
            result.append("Туда нельзя пройти.")

    elif command == "взять меч":
        if current_room != "armory":
            result.append("Здесь нет меча.")
        elif "меч" in inventory:
            result.append("Меч уже у вас.")
        else:
            inventory.append("меч")
            result.append("Вы взяли меч.")

    elif command == "атаковать":
        if current_room != "corridor":
            result.append("Здесь нет врагов.")
        elif not goblin_alive:
            result.append("Гоблин уже побеждён.")
        else:
            if "меч" in inventory:
                goblin_alive = False
                gold += 30

                result.append("Вы атаковали гоблина мечом.")
                result.append("Гоблин побеждён.")
                result.append("Вы получили 30 золота.")
            else:
                health -= 35

                result.append("Вы попытались атаковать без оружия.")
                result.append("Гоблин ранил вас.")
                result.append(f"Здоровье: {health}")

                if health <= 0:
                    result.append("Вы погибли.")
                    game_over = True

    elif command == "открыть сундук":
        if current_room != "treasury":
            result.append("Здесь нет сундука.")
        elif goblin_alive:
            result.append("Сначала победите стража в коридоре.")
        else:
            gold += 100

            result.append("Вы открыли сундук.")
            result.append("Вы нашли сокровища.")
            result.append("ПОБЕДА!")

            game_over = True

    elif command == "статус":
        result.append(f"Здоровье: {health}")
        result.append(f"Золото: {gold}")
        result.append(f"Локация: {rooms[current_room]['name']}")

        if inventory:
            result.append("Инвентарь: " + ", ".join(inventory))
        else:
            result.append("Инвентарь пуст.")

    else:
        result.append("Неизвестная команда.")
        result.append("Введите: помощь")

    return result
```

---

## Разбор

```python id="ws9h5k"
health = 100
```

Текущее здоровье игрока.

---

```python id="14g1w7"
inventory = ["факел"]
```

Инвентарь игрока.

---

---

## ОБРАБОТКА КОМАНД

---

## Листинг

```python id="8g8k7k"
def process_command(command):
```

Главная функция обработки команд.

---

## Схема обработки

```text id="0cqarf"
Команда
   │
   ▼
process_command()
   │
   ▼
изменение состояния
```

---

## Очистка команды

```
command = command.lower().strip()
```

---

---

## ПЕРЕМЕЩЕНИЕ МЕЖДУ КОМНАТАМИ

---

## Листинг

```
elif command.startswith("идти "):
```

---

## Схема перемещения

```
идти коридор
      │
      ▼
смена current_room
```

---

## Получение переходов

```
exits = rooms[current_room]["exits"]
```

---

## Смена комнаты

```
current_room = exits[place]
```

---

---

## БОЕВАЯ СИСТЕМА

---

## Листинг

```
elif command == "атаковать":
```

---

## Схема боя

```
атаковать
    │
    ▼
есть меч?
```

---

## Победа

```
goblin_alive = False
gold += 30
```

---

## Получение урона

```
health -= 35
```

---

---

## ЗАВЕРШЕНИЕ ИГРЫ

---

## Листинг

```
if health <= 0:
```

---

## Схема завершения

```
health <= 0
      │
      ▼
game_over = True
```

---

## Архитектурная роль

```
game_logic.py
    ↓
управление состоянием игры
```

---

# ═══════════════════════════════════════════════════════════

# ui.py

# ═══════════════════════════════════════════════════════════

## Назначение

Файл отвечает за графический интерфейс.

---

## Структура интерфейса

```
window
│
├── info_panel
├── output
├── inventory_panel
└── bottom_panel
```

---
```
import tkinter as tk
import ctypes

from settings import *

from game_logic import (
    process_command,
    get_status
)

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


def create_window():

    window = tk.Tk()

    window.tk.call("tk", "scaling", 1.5)

    window.title("Текстовая RPG")

    window.geometry(
        f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
    )

    window.configure(bg=BG_COLOR)

    # -------------------
    # ВЕРХНЯЯ ПАНЕЛЬ
    # -------------------

    info_panel = tk.Frame(
        window,
        bg=PANEL_COLOR
    )

    info_panel.pack(
        fill="x",
        padx=20,
        pady=(20, 10)
    )

    for i in range(4):
        info_panel.columnconfigure(i, weight=1)

    health_label = tk.Label(
        info_panel,
        bg=PANEL_COLOR,
        fg="#22c55e",
        font=FONT_PANEL,
        anchor="center"
    )

    health_label.grid(
        row=0,
        column=0,
        sticky="ew",
        pady=10
    )

    gold_label = tk.Label(
        info_panel,
        bg=PANEL_COLOR,
        fg="#facc15",
        font=FONT_PANEL,
        anchor="center"
    )

    gold_label.grid(
        row=0,
        column=1,
        sticky="ew",
        pady=10
    )

    room_label = tk.Label(
        info_panel,
        bg=PANEL_COLOR,
        fg="#38bdf8",
        font=FONT_PANEL,
        anchor="center"
    )

    room_label.grid(
        row=0,
        column=2,
        sticky="ew",
        pady=10
    )

    state_label = tk.Label(
        info_panel,
        bg=PANEL_COLOR,
        fg="#c084fc",
        font=FONT_PANEL,
        anchor="center"
    )

    state_label.grid(
        row=0,
        column=3,
        sticky="ew",
        pady=10
    )

    # -------------------
    # ТЕКСТОВОЕ ПОЛЕ
    # -------------------

    output = tk.Text(
        window,
        bg=TEXT_BG,
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR,
        font=FONT_MAIN,
        wrap="word",
        bd=0,
        padx=15,
        pady=15,
        height=18,
        state="disabled"
    )

    output.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    output.tag_configure(
        "center",
        justify="center",
        spacing1=5,
        spacing3=5
    )

    # -------------------
    # ВСПЛЫВАЮЩИЙ ИНВЕНТАРЬ
    # -------------------

    inventory_panel = tk.Frame(
        window,
        bg="#111827",
        bd=2,
        relief="solid"
    )

    inventory_title = tk.Label(
        inventory_panel,
        text="🎒 ИНВЕНТАРЬ",
        bg="#111827",
        fg="#facc15",
        font=FONT_TITLE
    )

    inventory_title.pack(pady=10)

    inventory_text = tk.Text(
        inventory_panel,
        bg="#0f172a",
        fg="#ffffff",
        font=FONT_PANEL,
        bd=0,
        width=26,
        height=14,
        state="disabled"
    )

    inventory_text.pack(
        padx=10,
        pady=10,
        fill="both",
        expand=True
    )

    inventory_text.tag_configure(
        "center",
        justify="center"
    )

    inventory_panel.place_forget()

    # -------------------
    # НИЖНЯЯ ПАНЕЛЬ
    # -------------------

    bottom_panel = tk.Frame(
        window,
        bg=BG_COLOR
    )

    bottom_panel.pack(
        fill="x",
        padx=20,
        pady=(5, 20)
    )

    # -------------------
    # ПОЛЕ ВВОДА
    # -------------------

    entry = tk.Entry(
        bottom_panel,
        bg=ENTRY_BG,
        fg=ENTRY_FG,
        insertbackground=ENTRY_FG,
        font=FONT_MAIN,
        bd=0,
        justify="center"
    )

    entry.pack(
        fill="x",
        ipady=8,
        pady=(0, 10)
    )

    # -------------------
    # ФУНКЦИИ
    # -------------------

    def write(text=""):

        output.config(state="normal")

        output.insert(
            tk.END,
            text + "\n",
            "center"
        )

        output.see(tk.END)

        output.config(state="disabled")

    def update_ui():

        status = get_status()

        health_label.config(
            text=f"❤️ Здоровье: {status['health']}"
        )

        gold_label.config(
            text=f"💰 Золото: {status['gold']}"
        )

        room_label.config(
            text=f"📍 {status['room']}"
        )

        if status["game_over"]:

            state_label.config(
                text="☠ Игра окончена"
            )

        else:

            state_label.config(
                text="🟢 Игра идёт"
            )

    def update_inventory_panel():

        status = get_status()

        inventory_text.config(state="normal")

        inventory_text.delete("1.0", tk.END)

        if status["inventory"]:

            for item in status["inventory"]:

                icon = "📦"

                if item == "факел":
                    icon = "🔥"

                elif item == "меч":
                    icon = "⚔"

                inventory_text.insert(
                    tk.END,
                    f"{icon} {item}\n",
                    "center"
                )

        else:

            inventory_text.insert(
                tk.END,
                "Инвентарь пуст.",
                "center"
            )

        inventory_text.config(state="disabled")

    def show_inventory_panel(event=None):

        update_inventory_panel()

        inventory_panel.place(
            relx=1.0,
            rely=0.23,
            anchor="ne",
            width=280,
            height=300
        )

    def hide_inventory_panel(event=None):

        inventory_panel.place_forget()

    def handle_command(event=None):

        command = entry.get()

        entry.delete(0, tk.END)

        if command.strip() == "":
            return

        write("➜ " + command)

        result = process_command(command)

        for line in result:
            write(line)

        write()

        update_ui()
        update_inventory_panel()

    # -------------------
    # КНОПКА ВВОДА
    # -------------------

    button = tk.Button(
        bottom_panel,
        text="⚔ Ввести",
        command=handle_command,
        bg=BUTTON_BG,
        fg="white",
        activebackground=BUTTON_ACTIVE,
        activeforeground="white",
        font=FONT_PANEL,
        bd=0,
        padx=20,
        pady=8
    )

    button.pack()

    # -------------------
    # КНОПКА ИНВЕНТАРЯ
    # -------------------

    inventory_hover = tk.Label(
        window,
        text="🎒",
        bg=BUTTON_BG,
        fg="white",
        font=FONT_TITLE,
        padx=12,
        pady=6
    )

    inventory_hover.place(
        relx=1.0,
        rely=0.45,
        anchor="e"
    )

    inventory_hover.bind(
        "<Enter>",
        show_inventory_panel
    )

    inventory_panel.bind(
        "<Leave>",
        hide_inventory_panel
    )

    # -------------------
    # ENTER
    # -------------------

    entry.bind(
        "<Return>",
        handle_command
    )

    # -------------------
    # СТАРТ
    # -------------------

    write("===================================")
    write("⚔ ЗАМОК ТЕНЕЙ ⚔")
    write("===================================")

    write()

    write("Введите команду: помощь")

    write()

    update_ui()
    update_inventory_panel()

    entry.focus()

    window.mainloop()
```

---

## СОЗДАНИЕ ОКНА

---

## Листинг

```
window = tk.Tk()
```

---

## Размер окна

```
window.geometry(
    f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
)
```

---

## Цвет фона

```
window.configure(bg=BG_COLOR)
```

---

---

## ВЕРХНЯЯ ПАНЕЛЬ

---

## Структура

```text id="vjlwm0"
info_panel
│
├── health_label
├── gold_label
├── room_label
└── state_label
```

---

## Листинг

```python id="f6u2mc"
info_panel = tk.Frame(
    window,
    bg=PANEL_COLOR
)
```

---

---

## OUTPUT PANEL

---

## Назначение

Главное текстовое поле игры.

---

## Листинг

```python id="n6jlwm"
output = tk.Text(
    window,
    state="disabled"
)
```

---

## Защита текста

```python id="7w9w9o"
state="disabled"
```

---

---

## INVENTORY PANEL

---

## Структура

```text id="yo3tw7"
inventory_panel
│
├── inventory_title
└── inventory_text
```

---

## Схема работы

```text id="4jlwmq"
Наведение курсора
        │
        ▼
show_inventory_panel()
```

---

---

## ВВОД КОМАНД

---

## Листинг

```python id="j6lfnq"
entry = tk.Entry(
    bottom_panel
)
```

---

## Обработка команды

```python id="0jlwmf"
def handle_command(event=None):
```

---

## Схема обработки

```text id="fgjlwm"
entry.get()
    │
    ▼
process_command()
    │
    ▼
update_ui()
```

---

---

## ОБНОВЛЕНИЕ ИНТЕРФЕЙСА

---

## Получение состояния

```python id="p4lazs"
status = get_status()
```

---

## Схема обновления

```text id="n1jlwm"
get_status()
      │
      ▼
обновление интерфейса
```

---

## Архитектурная роль

```text id="jlwmh7"
ui.py
    ↓
отображение состояния игры
```

---

# ═══════════════════════════════════════════════════════════

# ЗАКЛЮЧЕНИЕ

# ═══════════════════════════════════════════════════════════

В ходе занятия разработана графическая текстовая RPG с модульной архитектурой.

В процессе разработки рассмотрены:

* разделение проекта на модули;
* структура игрового мира;
* хранение состояния игры;
* обработка пользовательских команд;
* взаимодействие интерфейса и логики;
* создание графического интерфейса на tkinter;
* архитектура приложения;
* обработка игровых событий;
* обновление интерфейса в реальном времени.



