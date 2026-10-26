#This is the testing script that doesn't need kmk, 
# and can just be used independently to get output

# Basic setup, will need to consider:
# - the 3 mechanical buttons
# - the rotary encoder
# - the slide potentiometer
# - the RGB LED lights
# - capacitive touch input

print("Testing start")



import time
import board
import digitalio
import analogio
import rotaryio
import neopixel

# --------------------------------------------------
# Pin helper: board pin names vary between builds.
# --------------------------------------------------

def get_pin(*names):
    for name in names:
        if hasattr(board, name):
            return getattr(board, name)
    raise RuntimeError("Pin not found: " + ", ".join(names))


# --------------------------------------------------
# 1. Push buttons
# Schematic: buttons connect signal to GND.
# Therefore, use internal pull-ups.
# --------------------------------------------------

button_pins = {
    "SWITCH1": get_pin("RX", "IO44", "GPIO44"),
    "SWITCH2": get_pin("TX", "IO43", "GPIO43"),
    "SWITCH3": get_pin("IO6", "GPIO6", "GP6"),
}

buttons = {}

for name, pin in button_pins.items():
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    buttons[name] = btn


# --------------------------------------------------
# 2. Rotary encoder (A/B channels)
# --------------------------------------------------

encoder = rotaryio.IncrementalEncoder(
    get_pin("IO1", "GPIO1", "GP1"),
    get_pin("IO2", "GPIO2", "GP2"),
)

last_position = encoder.position


# --------------------------------------------------
# 3. Slide potentiometer
# SLIDE1 is the wiper / analog output.
# --------------------------------------------------

pot = analogio.AnalogIn(
    get_pin("IO3", "GPIO3", "GP3")
)


# --------------------------------------------------
# 4. SK6812 Mini-E addressable RGB LEDs
# --------------------------------------------------

pixels = neopixel.NeoPixel(
    get_pin("IO5", "GPIO5", "GP5"),
    3,
    brightness=0.15,
    auto_write=False,
)

# Startup test: red, green, blue, then off.
for color in [(255, 0, 0), (0, 255, 0), (0, 0, 255)]:
    pixels.fill(color)
    pixels.show()
    time.sleep(0.4)

pixels.fill((0, 0, 0))
pixels.show()


# --------------------------------------------------
# 5. Capacitive touch inputs
# ESP32-S3 touch-capable pins: GPIO7 through GPIO13.
# --------------------------------------------------

touch_pins = {
    "TOUCH1": ("IO13", "GPIO13", "GP13"),
    "TOUCH2": ("IO12", "GPIO12", "GP12"),
    "TOUCH3": ("IO11", "GPIO11", "GP11"),
    "TOUCH4": ("IO10", "GPIO10", "GP10"),
    "TOUCH5": ("IO9", "GPIO9", "GP9"),
    "TOUCH6": ("IO8", "GPIO8", "GP8"),
    "TOUCH7": ("IO7", "GPIO7", "GP7"),
}

touch_inputs = {}

try:
    import touchio

    for name, pin_names in touch_pins.items():
        try:
            touch_inputs[name] = touchio.TouchIn(
                get_pin(*pin_names)
            )
        except Exception as e:
            print(name, "unavailable:", repr(e))

except ImportError:
    print("touchio unavailable in this CircuitPython build.")


# --------------------------------------------------
# 6. Main test loop
# --------------------------------------------------

previous_buttons = {name: False for name in buttons}
previous_touches = {name: False for name in touch_inputs}

print("\nHardware test running.")
print("Press buttons, rotate encoder, move slider,")
print("touch electrodes, and watch the serial output.\n")

while True:
    # Push buttons
    for name, btn in buttons.items():
        pressed = not btn.value

        if pressed and not previous_buttons[name]:
            print(name, "PRESSED")

        previous_buttons[name] = pressed

    # Rotary encoder
    position = encoder.position

    if position != last_position:
        print("Encoder position:", position)
        last_position = position

    # Potentiometer: 0 to 65535
    print("Pot:", pot.value,
          "Voltage:", round(pot.value * 3.3 / 65535, 2), "V")

    # Capacitive touch: detect new touches
    for name, touch in touch_inputs.items():
        touched = touch.value

        if touched and not previous_touches[name]:
            print(name, "TOUCHED")

        previous_touches[name] = touched

    # Show encoder position on LEDs for a quick visual test.
    # A/B encoder direction should change the lit LED.
    led_index = position % 3
    pixels.fill((0, 0, 0))
    pixels[led_index] = (0, 40, 100)
    pixels.show()

    time.sleep(0.05)
