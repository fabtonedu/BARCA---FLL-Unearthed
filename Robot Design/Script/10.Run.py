from pybricks.hubs import InventorHub
from pybricks.robotics import DriveBase

from motor_config import MotorConfig

hub = InventorHub()


def _create_drivebase(motor_config: MotorConfig) -> DriveBase:
    drive_base = DriveBase(
        motor_config.left_motor,
        motor_config.right_motor,
        wheel_diameter=60.6,
        axle_track=240,
    )
    drive_base.settings(700, 700, 150, 100)
    drive_base.use_gyro(True)
    return drive_base


def _opening(drive_base: DriveBase, motor_config: MotorConfig):
    motor_config.b_motor.run_time(700, 750, wait=False)

    drive_base.straight(100)
    drive_base.turn(-20)
    drive_base.straight(450)
    drive_base.turn(-28.7)
    drive_base.straight(420)

    motor_config.b_motor.run_time(700, 300)


def _mid_section(drive_base: DriveBase):
    drive_base.straight(-100)
    drive_base.turn(-19)
    drive_base.straight(350)
    drive_base.turn(-37)
    drive_base.straight(345)
    drive_base.turn(-36)


def _final_actions(drive_base: DriveBase, motor_config: MotorConfig):
    motor_config.a_motor.run_time(-700, 1000)
    drive_base.straight(135)
    motor_config.b_motor.run_time(-700, 600)
    drive_base.straight(-170)


def run__10_futas(motor_config: MotorConfig):
    drive_base = _create_drivebase(motor_config)

    _opening(drive_base, motor_config)
    _mid_section(drive_base)
    _final_actions(drive_base, motor_config)
