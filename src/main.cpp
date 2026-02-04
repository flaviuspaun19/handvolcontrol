#include <Arduino.h>
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
const int trigPin = 9;
const int echoPin = 10;

// Filter function to remove "ghost" readings
int getFilteredDistance() {
  long duration;
  int d;
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH, 30000); // 30ms timeout prevents hangs
  d = duration * 0.034 / 2;
  
  // Filter: Ignore impossible readings for indoor use
  if (d > 200 || d <= 0) return -1; 
  return d;
}

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  int currentDist = getFilteredDistance();

  if (currentDist != -1) {
    lcd.setCursor(0, 0);
    lcd.print("Dist: ");
    lcd.print(currentDist);
    lcd.print(" cm   ");

    lcd.setCursor(0, 1);
    // Added a "Deadzone" to make it more precise
    if (currentDist > 5 && currentDist < 15) {
      lcd.print("Action: VOL +  ");
      Serial.println("UP");
    } 
    else if (currentDist > 20 && currentDist < 35) {
      lcd.print("Action: VOL -  ");
      Serial.println("DOWN");
    } 
    else {
      lcd.print("Status: Idle   ");
    }
  }
  delay(150); // Balanced sampling rate
}