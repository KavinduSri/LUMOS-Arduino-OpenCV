// LED pins
int green[] = {2, 3, 4, 5};
int blue[]  = {6, 7, 8, 9};
int red[]   = {10, 11, 12, 13};

int gN = 4, bN = 4, rN = 4;

void setup() {
  Serial.begin(9600);

  for (int i = 0; i < gN; i++) pinMode(green[i], OUTPUT);
  for (int i = 0; i < bN; i++) pinMode(blue[i], OUTPUT);
  for (int i = 0; i < rN; i++) pinMode(red[i], OUTPUT);
}

void loop() {
  if (Serial.available()) {
    int d = Serial.parseInt();   // distance from Python

    // Adjust distance ranges if needed
    int gLevel = constrain(map(d, 20, 80, 0, gN), 0, gN);
    int bLevel = constrain(map(d, 80, 140, 0, bN), 0, bN);
    int rLevel = constrain(map(d, 140, 220, 0, rN), 0, rN);

    // Green LEDs
    for (int i = 0; i < gN; i++)
      digitalWrite(green[i], i < gLevel ? HIGH : LOW);

    // Blue LEDs
    for (int i = 0; i < bN; i++)
      digitalWrite(blue[i], i < bLevel ? HIGH : LOW);

    // Red LEDs
    for (int i = 0; i < rN; i++)
      digitalWrite(red[i], i < rLevel ? HIGH : LOW);
  }
}
