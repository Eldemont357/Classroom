const int buttonPin = 6;
const int leds[6] = {13, 12, 11, 10, 9, 8};

int lastButton = HIGH; // для INPUT_PULLUP: отпущена = HIGH

void setup() {
  pinMode(buttonPin, INPUT_PULLUP); // ВНУТРЕННЯЯ ПОДТЯЖКА

  for (int i = 0; i < 6; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], LOW);
  }

  randomSeed(analogRead(A0));
}

void turnOffAll() {
  for (int i = 0; i < 6; i++) digitalWrite(leds[i], LOW);
}

void loop() {
  int button = digitalRead(buttonPin);

  // нажатие: HIGH -> LOW
  if (button == LOW && lastButton == HIGH) {
    turnOffAll();
    int index = random(0, 6);
    digitalWrite(leds[index], HIGH);
  }

  lastButton = button;
}
