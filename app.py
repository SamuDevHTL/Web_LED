from flask import Flask, render_template, request, jsonify
import RPi.GPIO as GPIO
from datetime import datetime  # Import datetime to get the timestamp
import board
import busio
import adafruit_tsl2591

# GPIO Setup
GPIO.setmode(GPIO.BCM)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

# Initialize TSL2591 Sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2591.TSL2591(i2c)

# Flask App erstellen
app = Flask(__name__)

def get_light_intensity():
    """Read light intensity from the TSL2591 sensor."""
    return sensor.lux

def get_background_color(lux):
    """Determine background color based on light intensity."""
    if lux < 100:
        return "gray10"  # Very dim light
    elif lux < 200:
        return "gray20"
    elif lux < 300:
        return "gray30"
    elif lux < 400:
        return "gray40"
    elif lux < 500:
        return "gray50"
    elif lux < 600:
        return "gray60"
    elif lux < 700:
        return "gray70"
    elif lux < 800:
        return "gray80"
    elif lux < 900:
        return "gray90"
    else:
        return "gray100"  # Brightest light


# Route für die Startseite
@app.route("/")
def index():
    # Getting the current timestamp and light intensity when the page is loaded
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format the timestamp
    lux = get_light_intensity()  # Get the light intensity
    background_color = get_background_color(lux)  # Determine background color
    return render_template("index.html", timestamp=timestamp, lux=lux, background_color=background_color)

# Route zum Umschalten der LED
@app.route("/toggle", methods=["POST"])
def toggle_led():
    GPIO.output(LED_PIN, not GPIO.input(LED_PIN))  # LED umschalten
    status = "ON" if GPIO.input(LED_PIN) else "OFF"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current timestamp
    lux = get_light_intensity()  # Get the light intensity
    background_color = get_background_color(lux)  # Determine background color
    return render_template("index.html", status=status, timestamp=timestamp, lux=lux, background_color=background_color)

# New route for light intensity data
@app.route("/light", methods=["GET"])
def light_data():
    lux = get_light_intensity()
    background_color = get_background_color(lux)
    return jsonify({"lux": lux, "background_color": background_color})

# Flask-App starten
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()
