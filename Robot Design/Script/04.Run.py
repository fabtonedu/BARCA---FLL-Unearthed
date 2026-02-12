from pybricks.hubs import InventorHub
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from motor_config import MotorConfig

hub = InventorHub()


def _create_drivebase(motor_config: MotorConfig) -> DriveBase:
    drive_base = DriveBase(
        motor_config.left_motor,
        motor_config.right_motor,
        wheel_diameter=60.6,
        axle_track=240,
    )
    drive_base.settings(800, 800, 500, 80)
    drive_base.use_gyro(True)
    return drive_base


def _approach_lochness(drive_base: DriveBase, motor_config: MotorConfig):
    motor_config.b_motor.run_time(1000, 780, wait=False)

    drive_base.straight(150)
    drive_base.turn(46.5)

    # menet közben picit agresszívebb turn accel (meghagyva)
    drive_base.settings(800, 800, 500, 120)


def _lochness_sequence(drive_base: DriveBase, motor_config: MotorConfig):
    # ráhajtunk a lochnessi szörnyre
    drive_base.straight(310, wait=False)
    motor_config.a_motor.run_time(250, 830)
    motor_config.b_motor.run_time(-1000, 780)
    wait(100)

    drive_base.straight(85)

    # felemeljük a lochnessi szörnyet
    motor_config.b_motor.run_time(400, 800)


def _flag_and_return(drive_base: DriveBase, motor_config: MotorConfig):
    drive_base.settings(1000, 1000, 500, 500)
    drive_base.straight(-20)

    # utolsó pillanatban visszatoljuk a zászlót
    motor_config.a_motor.run_time(500, 450)

    drive_base.straight(-500)


def run__4_futas(motor_config: MotorConfig):
    drive_base = _create_drivebase(motor_config)

    _approach_lochness(drive_base, motor_config)
    _lochness_sequence(drive_base, motor_config)
    _flag_and_return(drive_base, motor_config)
