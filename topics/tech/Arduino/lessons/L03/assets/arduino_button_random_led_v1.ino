const int buttonPin = 7;
const int leds[6] = {13, 12, 11, 10, 9, 8};

int lastButtonState = LOW;

void setup() {
  pinMode(buttonPin, INPUT);

  for (int i = 0; i < 6; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], LOW);
  }

  randomSeed(analogRead(A0));
}

void turnOffAll() {
  for (int i = 0; i < 6; i++) {
    digitalWrite(leds[i], LOW);
  }
}

void loop() {
  int buttonState = digitalRead(buttonPin);

  // ловим момент нажатия
  if (buttonState == HIGH && lastButtonState == LOW) {
    turnOffAll();

    int index = random(0, 6);
    digitalWrite(leds[index], HIGH);
  }

  lastButtonState = buttonState;
}
