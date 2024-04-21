#ZIEPSTAT
### vienkārša programma, ziepju lietošanas pēc publiskās tualetes statistikas krāšanas un analīzes

## Nepieciešamā programmatūra
**Arduino IDE**

**Python3** ar norādītajām bibliotēkām

    **PyQt5** - grafiskās lietotāja saskarnes veidošanai
    
    **fastapi** - vienkārša API izveidei datubāzes ierakstu saņemšanai
    
    **uvicorn** - lokālā servera startēšanai

## Bibliotēku uzstādīšana
```pip install -r requirements```

## Programmas startēšana
```python app.py``` - analīzes programma

```uvicorn Server:server --reload``` - lokālā servera startēšanai

## Sensoru sagatavošana
Sensori sastāv no esp8266 moduļa (NodeMCU V3), gaismas diodes, fotorezistora, un diviem 68 omu rezistoriem sprieguma kontrolēšanai
Sensora shēma izskātās tā:

![image](https://github.com/Hlebusek/ZiepStat/assets/69074631/e52b36d6-bf67-4b16-a3ff-0b91e53db7dc)


failā Sensors/Sensors.ino 10. koda rindā jāveic izmaiņas atbilstoši programmēšanai izvēlētajam sensoram

ja sensors sūtīs statistiku par tualetes izmantošanu
```
#define serverUrl "http://127.0.0.1:8000/commit?action=pods";
``` 

ja sensors sūtīs statistiku par ziepju izmantošanu
```
#define serverUrl "http://127.0.0.1:8000/commit?action=ziepes";
```
pamācību par nodemcu moduļu programmēšanu var apskatīt te:
```https://www.instructables.com/Getting-Started-With-ESP8266LiLon-NodeMCU-V3Flashi/```

4. un 5. koda rindā jānorāda wifi SSID un parole
```
#define ssid "your_network_ssid"
#define password "your_network_password"
```

## Analīzes aplikācija

![image](https://github.com/Hlebusek/ZiepStat/assets/69074631/ab8e0355-0942-4709-b1ba-69ddef279426)

1 - rādītājs (ziepju izmantošanas skaits/tualetes apmeklējumu skaits)

2 - Apskatāmo datu sākuma un beigu datuma izvēle

3 - Procentu rādītājs (cik apmeklētāju procentuāli izmantoja ziepes)

atkarībā no procentuālās vērtibas programmā īstenota arī krāsas indikācija

![image](https://github.com/Hlebusek/ZiepStat/assets/69074631/d352094a-8095-4012-ad3e-61bfaed2c90c)
![image](https://github.com/Hlebusek/ZiepStat/assets/69074631/0c2584a8-e790-42e8-a4c2-c78b63dea33e)
![image](https://github.com/Hlebusek/ZiepStat/assets/69074631/c5256cb6-d5dd-478e-a98a-476b5b2ffd79)



