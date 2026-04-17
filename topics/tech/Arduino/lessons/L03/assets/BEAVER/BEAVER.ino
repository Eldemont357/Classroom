const int leds[4]    = {8, 9, 10, 11};
const int buttons[4] = {3, 4, 5, 6};

int current = -1;

void allOff() {
  for (int i = 0; i < 4; i++) digitalWrite(leds[i], LOW);
}

void spawn() {
  allOff();
  current = random(0, 4);
  digitalWrite(leds[current], HIGH);
}

void setup() {
  for (int i = 0; i < 4; i++) {
    pinMode(leds[i], OUTPUT);
    pinMode(buttons[i], INPUT);   // ВАЖНО: INPUT (у тебя внешние резисторы)
  }
  randomSeed(analogRead(A0));
  spawn();
}

void loop() {
  // ждём правильную кнопку
  if (digitalRead(buttons[current]) == HIGH) { // нажата = HIGH
    delay(120); // простой антидребезг
    // ждём отпускания, чтобы не перескакивало 10 раз
    while (digitalRead(buttons[current]) == HIGH) {}
    spawn();
  }
}
