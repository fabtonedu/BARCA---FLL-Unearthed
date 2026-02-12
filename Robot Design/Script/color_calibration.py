from pybricks.pupdevices import ColorSensor, ForceSensor
from pybricks.parameters import Port, Button, Color
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
# Initialize the force sensor
force_sensor = ForceSensor(Port.A)

# Initialize the color sensor.
sensor = ColorSensor(Port.E)

hub = PrimeHub()

COLOR_NAMES = ["1","2","3","4","5","6","7","8","9","0"]

FINAL_COLOR_CONFIG = "\nCOLOR_RANGES = {\n"
HUE_CORRECTION_RANGE = 2
SATURATION_CORRECTION_RANGE = 15
VALUE_CORRECTION_RANGE = 30

# egy számból csinál egy +- intervallumot
def generate_range_tuple_from_reading(value: int, correction_range: int):
    return (value - correction_range, value + correction_range)


for color_name in COLOR_NAMES:
    print(f"Waiting for press for {color_name}...")

    # --- Wait for press ---
    while not force_sensor.pressed(force=2):
        wait(10)

    # --- Optional: debounce / read value ---
    hsv_value = sensor.hsv()
    print(f'"{color_name}" pressed, HSV reading: {hsv_value}')

    run_number = color_name if color_name != "0" else "10"

    FINAL_COLOR_CONFIG += (f'\t"{color_name}" : ' +
        f'ColorTrigger(' +
        f'{generate_range_tuple_from_reading(hsv_value.h, HUE_CORRECTION_RANGE)}, ' +
        f'{generate_range_tuple_from_reading(hsv_value.s, SATURATION_CORRECTION_RANGE)}, ' +
        f'{generate_range_tuple_from_reading(hsv_value.v, VALUE_CORRECTION_RANGE)}, ' +
        f'action = run__{run_number}_futas), \n')


    # --- Wait for release before next iteration ---
    while force_sensor.pressed(force=2):
        wait(10)

FINAL_COLOR_CONFIG += "}"
# kiírjuk a teljes színekhez rendelt futásokat
print(FINAL_COLOR_CONFIG)
