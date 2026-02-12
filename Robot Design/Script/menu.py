#portok
#A-gomb
#B-bal fenti motor
#C-bal kerek motor
#D-jobb kerek motor
#E-szinerzekelo
#f-jobb fenti motor

from pybricks.pupdevices import ColorSensor, ForceSensor
from pybricks.parameters import Port, Button, Color, Direction, Icon
from pybricks.tools import wait, StopWatch
from COLOR_RANGES import COLOR_RANGES

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor

from color_trigger import ColorTrigger

from _1_futas import run__1_futas
from _2_futas  import run__2_futas
from _3_futas import run__3_futas
from _4_futas import run__4_futas
from _5_futas import run__5_futas
from _6_futas  import run__6_futas
from _7_futas import run__7_futas
from _8_futas import run__8_futas
from _9_futas import run__9_futas
from _10_futas import run__10_futas

# Motor konfiguráció
from motor_config import motor_config,MotorConfig
# importáljuk a segítő függvényeket
from util import play_bad,play_finish,play_good, in_range

# Initialize the force sensor
force_sensor = ForceSensor(Port.A)

# Initialize the color sensor.
sensor = ColorSensor(Port.E)
hub = PrimeHub()
hub.speaker.volume(100)
# inicalizáljuk az órát
stopwatch = StopWatch()

def init_motor_conf():
    motor_config= MotorConfig(
        left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE),
        right_motor = Motor(Port.D),
        a_motor = Motor(Port.B),
        b_motor = Motor(Port.F),
        )

def get_detected_color():
    while True:
        color = sensor.hsv()
        
        # a program végigveszi, és összehasonlítja a beolvasott színnel a COLOR_RANGES.py file-ban
        #  lévő értékekkel
        for name, trigger in COLOR_RANGES.items():
            if in_range(color=color, range=trigger):
                play_good(hub=hub)
                hub.display.char(name)
                print(f"GOT IT - running {name}")
                hub.system.set_stop_button(Button.CENTER)

                return name, trigger  # stop on first detected color

        print("NOT FOUND")
        return None, None

def stop_motor():
    motor_config.a_motor.stop()
    motor_config.b_motor.stop()
    motor_config.left_motor.stop()
    motor_config.right_motor.stop()

def close_motors():
    motor_config.a_motor.close()
    motor_config.b_motor.close()
    motor_config.left_motor.close()
    motor_config.right_motor.close()



change_time = stopwatch.time()
total_run = 0
total_change = 0
while True:
    press = force_sensor.pressed(force=2)
    if press:
        # ide tértek vissza a már megkapott értékek (futás szám, trigger objektum)
        run_number, color_trigger = get_detected_color()
        # elindítjuk a stoppert a futásra
        run_time = stopwatch.time()
        
        if run_number:
            # ha első futás indul, nem vesszük figyelembe a change_time változót
            if run_number == "1":
                change_time = stopwatch.time()
            # minden más esetben megnézzük, hogy mennyi idő telt el a tartozék
            # cserélésével    
            else:
                print(f"\nChange time before {run_number}: {(run_time-change_time)/1000}s\n")
                total_change += (run_time - change_time)
            # itt indul a program (a triggerhez rendelt futási program)
            color_trigger.run_action(motor_config)

            stop_motor()
            close_motors()
            play_finish(hub=hub)
            # újra indítjuk a csere stoppert
            change_time = stopwatch.time()
            # hozzáadjuk a total runhoz a mostani program idejét
            total_run += (change_time-run_time)
            # kiíratjuk, hogy mennyi volt az idő
            print(f"\nrun time for {run_number}: {(change_time-run_time)/1000}s\n")
            # utolsó program végén kiíratjuk, hogy mennyi volt az össz futás, az össz csere,
            # az átlagos csere, és a teljes idő
            if run_number == "0":
                print(f"\n\nTOTAL RUN: {total_run/1000}s")
                print(f"AVERAGE CHANGE: {total_change/9000}s")
                print(f"TOTAL CHANGE: {total_change/1000}s")
                print(f"TOTAL: {(total_run+total_change)/1000}s\n\n")
            # ha minden kész, újra inicalizáljuk a motor konfgurációt, a következő futáshoz
            init_motor_conf()
        else:
            # kiírja az X-et, ha a nyomásszenzor megnyomása esetén, nem ismeri 
            # fel a megfelelő színt
            play_bad(hub=hub)
            continue

    wait(200)