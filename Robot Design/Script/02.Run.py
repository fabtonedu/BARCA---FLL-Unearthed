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
    drive_base.settings(900, 900, 500, 120)
    drive_base.use_gyro(True)
    return drive_base


def _approach_target(drive_base: DriveBase):
    drive_base.straight(705)
    drive_base.turn(-41)
    drive_base.straight(30)


def _do_missions_and_pickup(drive_base: DriveBase, motor_config: MotorConfig):
    # beallas az elem alap poziciojaba + 2 feladat megcsinalasa
    drive_base.straight(120, wait=False)
    motor_config.b_motor.run_time(-100, 1330)

    drive_base.straight(-39)

    # palyaelem felvevese
    motor_config.b_motor.run_time(speed=990, time=700)

    # hatra tolatas
    drive_base.straight(-105)


def _return_home(drive_base: DriveBase):
    drive_base.turn(50)
    drive_base.straight(-700)


def run__2_futas(motor_config: MotorConfig):
    drive_base = _create_drivebase(motor_config)

    _approach_target(drive_base)
    _do_missions_and_pickup(drive_base, motor_config)
    _return_home(drive_base)
