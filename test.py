import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED_PIN = 12  # Replace with your GPIO pin if different
GPIO.setup(LED_PIN, GPIO.OUT)

print("Turning LED on...")
GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
time.sleep(2)

print("Turning LED off...")
GPIO.output(LED_PIN, GPIO.LOW)  # Turn LED off
GPIO.cleanup()
