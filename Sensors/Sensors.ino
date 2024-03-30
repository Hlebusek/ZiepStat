#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#define ssid "your_network_ssid"
#define password "your_network_password"
#define Sensitivity 900 // atkariba no telpas kura tiek uzstadits sensors, jamaina jutiba
#define photoresistorPin A0;  // fotorezistora pieslēgšanas pin
#define LedPin D1;        // Gaismas diodes pieslēgšanas pin

#define serverUrl "http://127.0.0.1:8000/commit?action=pods"; // "http://127.0.0.1:8000/commit?action=ziepes"

void setup() {

  Serial.begin(9600);

  pinMode(photoresistorPin, INPUT);
  pinMode(LedPin, OUTPUT);

  // pieslegsanas pie wifi 
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("WiFi connected!");
  digitalWrite(LedPin, HIGH);
}

void loop() {
  // nolasam fotorezistora rādītājus
  int lightLevel = analogRead(photoresistorPin);

  // ja radītāji ir par mazu, tad starp diodi un fotorezistoru noteikti atrodas objekts, piem. pirksts
  if (lightLevel < Sensitivity) { 
    Serial.println("Object detected!");

    // izslēdzam gaismas diodi sensora nostrādāšanas indikācijai
    digitalWrite(LedPin, LOW);

    // Nosūtam serverim ziņojumu par sensora nostrādāšanu
    HTTPClient http;
    http.begin(serverUrl);
    int httpResponseCode = http.GET();
    if (httpResponseCode > 0) {
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
    } else {
      Serial.println("Error sending request");
    }
    http.end();

    delay(15000); // apstādinam kodu uz 15 sekundem lai izslegtu gadijumu ka viens cilveks nosuta vairakas zinas serverim
    digitalWrite(LedPin, LOW);
  } 

  delay(500); // intervāls 0,5s starp rādijumu lasīšanam
}
