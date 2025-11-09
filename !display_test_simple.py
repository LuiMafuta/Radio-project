import tm1637
import time
import RPi.GPIO as GPIO

print("🧪 Test: Display wird initialisiert...")
GPIO.cleanup()

try:
    display = tm1637.TM1637(clk=24, dio=23)
    display.brightness(7)
    display.show("8888")
    print("✅ Display sollte jetzt 8888 zeigen")
    time.sleep(3)
    display.show("----")
    time.sleep(1)
    display.clear()
    print("✅ Test abgeschlossen")
except Exception as e:
    print("❌ Fehler beim Initialisieren:", e)
