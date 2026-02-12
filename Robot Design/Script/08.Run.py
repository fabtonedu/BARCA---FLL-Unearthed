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
    drive_base.settings(700, 700, 250, 500)
    drive_base.use_gyro(True)
    return drive_base


def _approach_and_first_action(drive_base: DriveBase, motor_config: MotorConfig):
    drive_base.straight(260)
    drive_base.settings(700, 700, 250, 500)

    drive_base.turn(90)
    drive_base.settings(700, 700, 250, 250)

    drive_base.straight(435)

    motor_config.b_motor.run_time(-600, 1400)


def _micro_adjust_and_continue(drive_base: DriveBase, motor_config: MotorConfig):
    drive_base.turn(-19)
    wait(150)
    drive_base.turn(20)

    motor_config.b_motor.run_time(600, 1200)

    drive_base.straight(70)
    drive_base.turn(39)
    drive_base.straight(50)

    motor_config.b_motor.run_time(-1000, 1100)

    drive_base.straight(60)

    motor_config.a_motor.run_time(1000, 1000)
    motor_config.b_motor.run_time(1000, 1200)


def _curve_and_return(drive_base: DriveBase):
    drive_base.curve(-420, 80)
    drive_base.straight(-320)


def run__8_futas(motor_config: MotorConfig):
    drive_base = _create_drivebase(motor_config)

    _approach_and_first_action(drive_base, motor_config)
    _micro_adjust_and_continue(drive_base, motor_config)
    _curve_and_return(drive_base)
