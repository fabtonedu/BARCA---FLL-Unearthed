from pybricks.hubs import InventorHub
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from motor_config import MotorConfig  # csak a type-hint miatt; a logikát nem bántja

hub = InventorHub()


def turn_90(motor_config: MotorConfig):
    # Meghagyva: ez egy külön gyros turn PD-vel (nincs hozzányúlva, csak formázás maradt ugyanaz)
    target = 90
    kp = 1.6
    kd = 1.2
    max_speed = 320
    min_speed = 70

    last_error = 0
    hub.imu.reset_heading(0)
    stable_count = 0

    while True:
        angle = hub.imu.heading()
        error = target - angle
        derivative = error - last_error
        last_error = error

        if abs(error) < 1.5:
            stable_count += 1
        else:
            stable_count = 0

        if stable_count >= 8:
            break

        turn = kp * error + kd * derivative

        if abs(error) > 5 and abs(turn) < min_speed:
            turn = min_speed if turn > 0 else -min_speed
        else:
            turn = max(-max_speed, min(max_speed, turn))

        motor_config.left_motor.run(turn)
        motor_config.right_motor.run(-turn)
        wait(100)


def _create_drivebase(motor_config: MotorConfig) -> DriveBase:
    drive_base = DriveBase(
        motor_config.left_motor,
        motor_config.right_motor,
        wheel_diameter=60.6,
        axle_track=240,
    )
    drive_base.settings(700, 700, 500, 120)
    drive_base.use_gyro(True)
    return drive_base


def _start_attachments(motor_config: MotorConfig):
    # Induláskor a két felső motor mozdul 
    motor_config.b_motor.run_time(1000, 1200, wait=False)
    motor_config.a_motor.run_time(1000, 100)


def _drive_out_to_mine(drive_base: DriveBase):
    hub.imu.reset_heading(0)
    drive_base.straight(892)
    wait(100)

    # finom forgás: itt “kézzel” forgattok heading alapján 
    drive_base.settings(60, 60, 120, 120)
    drive_base.stop()


def _turn_until_heading(motor_config: MotorConfig, target_heading: float):
    # Gyors, manuális fordulás headingre (
    while hub.imu.heading() < target_heading:
        motor_config.left_motor.run(200)
        motor_config.right_motor.run(-200)

    motor_config.left_motor.stop()
    motor_config.right_motor.stop()


def _mine_actions(drive_base: DriveBase, motor_config: MotorConfig):
    # kikapcsoljuk a gyroscope-ot, hogy ne korrigáljon az előremenetnél
    drive_base.use_gyro(False)

    # felvesszük a kincset a bányából, és áttoljuk a csillét 
    motor_config.a_motor.run_time(1000, 750, wait=False)
    motor_config.b_motor.run_time(-1000, 1200)

    drive_base.straight(100)

    motor_config.a_motor.run_time(-500, 390)
    motor_config.b_motor.run_time(1000, 800)
    wait(100)

    motor_config.b_motor.run_time(-1000, 800)
    drive_base.straight(-100)

    motor_config.a_motor.run_time(-1000, 800, wait=False)
    motor_config.b_motor.run_time(1000, 1200)


def _return_home_fast(drive_base: DriveBase):
    # kifordulunk, és teljes sebességgel visszajövünk a bázisra
    drive_base.settings(1000, 1000, 500, 500)
    drive_base.turn(-42)
    drive_base.straight(-880)


def run__1_futas(motor_config: MotorConfig):
    drive_base = _create_drivebase(motor_config)

    _start_attachments(motor_config)
    _drive_out_to_mine(drive_base)

    _turn_until_heading(motor_config, 83.5)

    _mine_actions(drive_base, motor_config)
    _return_home_fast(drive_base)
