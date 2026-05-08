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