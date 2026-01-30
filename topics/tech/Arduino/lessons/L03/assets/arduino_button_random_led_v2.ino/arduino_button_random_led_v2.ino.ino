/ Пин, к которому подключена кнопка
const int buttonPin = 6;

// Массив пинов светодиодов (6 штук)
const int leds[6] = {13, 12, 11, 10, 9, 8};

// Предыдущее состояние кнопки
// При INPUT_PULLUP: отпущена = HIGH, нажата = LOW
int lastButton = HIGH;

void setup() {
  // Включаем внутреннюю подтяжку к питанию
  // Это избавляет от "плавающего" входа
  pinMode(buttonPin, INPUT_PULLUP);

  // Настраиваем все светодиоды как выходы
  // И сразу выключаем их
  for (int i = 0; i < 6; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], LOW);
  }

  // Инициализация генератора случайных чисел
  // analogRead(A0) даёт шум, достаточный для seed
  randomSeed(analogRead(A0));
}

// Функция выключает все светодиоды
void turnOffAll() {
  for (int i = 0; i < 6; i++) {
    digitalWrite(leds[i], LOW);
  }
}

void loop() {
  // Считываем текущее состояние кнопки
  int button = digitalRead(buttonPin);

  // Обработка события "нажатие кнопки"
  // Фиксируем переход из HIGH в LOW
  if (button == LOW && lastButton == HIGH) {
    // Гасим все светодиоды
    turnOffAll();

    // Выбираем случайный индекс светодиода (0–5)
    int index = random(0, 6);

    // Включаем выбранный светодиод
    digitalWrite(leds[index], HIGH);
  }

  // Сохраняем текущее состояние кнопки
  // для сравнения на следующем проходе loop()
  lastButton = button;
}