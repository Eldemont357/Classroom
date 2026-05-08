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