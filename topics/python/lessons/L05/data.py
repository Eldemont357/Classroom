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