from flask import Flask, render_template, request
import RPi.GPIO as GPIO

# GPIO-Setup
GPIO.setmode(GPIO.BCM)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

# Flask-App erstellen
app = Flask(__name__)

# Startseite mit Button
@app.route("/")
def index():
    return '''
    <h1>LED Steuerung</h1>
    <form action="/toggle" method="post">
        <button type="submit">LED umschalten</button>
    </form>
    '''

# LED umschalten
@app.route("/toggle", methods=["POST"])
def toggle_led():
    GPIO.output(LED_PIN, not GPIO.input(LED_PIN))
    status = "AN" if GPIO.input(LED_PIN) else "AUS"
    return f'''
    <h1>LED ist jetzt {status}</h1>
    <a href="/">Zurück</a>
    '''

# App starten
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000)
    except KeyboardInterrupt:
        GPIO.cleanup()
