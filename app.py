from flask import Flask, render_template, request
import RPi.GPIO as GPIO
from datetime import datetime  # Import datetime to get the timestamp

# GPIO-Setup
GPIO.setmode(GPIO.BCM)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

# Flask-App erstellen
app = Flask(__name__)

# Route für die Startseite
@app.route("/")
def index():
    # Getting the current timestamp when the page is loaded
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format the timestamp
    return render_template("index.html", timestamp=timestamp)  # Pass the timestamp to the template

# Route zum Umschalten der LED
@app.route("/toggle", methods=["POST"])
def toggle_led():
    GPIO.output(LED_PIN, not GPIO.input(LED_PIN))  # LED umschalten
    status = "ON" if GPIO.input(LED_PIN) else "OFF"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current timestamp
    return render_template("index.html", status=status, timestamp=timestamp)  # Pass status and timestamp

# Flask-App starten
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()
