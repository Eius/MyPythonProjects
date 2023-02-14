#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <EEPROM.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

int motoMinutes = 0;
int motorSensorPin = 3; // Pin so sensorom v motore
int counterSensorPin = 2; // Pin s elektromagnetickým poćtatdlom
int currentRotations = 0; // variable to store the count of rotations
int targetRotations = 2500; // number of rotations to reach before incrementing counter
int rpm = 0; // Current rotations per minute
unsigned long timeOfLastRotation = 0;
unsigned long timeOfCurrentRotation = 0;
unsigned long timeInterval = 0;


void countRotation() {
    currentRotations++;
    timeOfLastRotation = timeOfCurrentRotation;
    timeOfCurrentRotation = millis();
}

void setup() {
    pinMode(counterSensorPin, OUTPUT);
    pinMode(motorSensorPin, INPUT);
    lcd.init();
    lcd.backlight();
    attachInterrupt(digitalPinToInterrupt(motorSensorPin), countRotation, RISING);
    lcd.setCursor(0, 3);
    if (EEPROM.read(0) == 255) {
        EEPROM.put(0, motoMinutes);
    } 
    else {
        EEPROM.get(0, motoMinutes);
    }
    lcd.setCursor(0, 0);
    lcd.print(motoMinutes);
}

void loop() {
    lcd.clear();
    timeInterval = timeOfCurrentRotation - timeOfLastRotation;
    rpm = 60000/timeInterval;
    lcd.setCursor(0, 0);
    lcd.print("RPM: ");
    if (rpm <= 400){
        rpm = 0;
    }
    lcd.print(rpm);
    if (currentRotations >= targetRotations) {
        motoMinutes = motoMinutes + 1;
        currentRotations = 0;
    }
    lcd.setCursor(0, 1);
    lcd.print("Otacok spolu: ");
    lcd.print(currentRotations);
    lcd.setCursor(0, 2);
    lcd.print("Motohodiny: ");
    lcd.print(float(motoMinutes/60));
    // lcd.setCursor(0, 3);
    // lcd.print("Motominuty: ");
    // lcd.print(float(motoMinutes));
    
    if (rpm <= 0) {
        EEPROM.put(0, motoMinutes);
    }
    
    delay(1000);
}