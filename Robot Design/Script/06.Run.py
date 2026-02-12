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
    drive_base.settings(1000, 1000, 500, 200)
    drive_base.use_gyro(True)
    return drive_base


def _approach_crane(drive_base: DriveBase):
    drive_base.straight(73)
    drive_base.turn(90)
    drive_base.straight(973)

    # precízebb beállás a daruhoz
    drive_base.settings(300, 300, 300, 120)
    drive_base.turn(89.4)
    drive_base.straight(86)
    drive_base.turn(-6)


def _spin_crane(motor_config: MotorConfig, drive_base: DriveBase):
    # felpörgetjük a darut
    motor_config.b_motor.run_time(1000, 1800)
    wait(100)

    # vissza az eredeti headingre
    drive_base.turn(6)


def _exit_and_scale(drive_base: DriveBase):
    # kitolatunk a darutól
    drive_base.straight(-35)

    drive_base.settings(1000, 1000, 500, 500)
    drive_base.turn(33)

    # elindulunk hátrafele, és ráhajtunk a mérlegre
    drive_base.straight(-170)
    wait(100)

    drive_base.straight(70)


def _return_home(drive_base: DriveBase):
    drive_base.settings(1000, 1000, 500, 500)
    drive_base.turn(67)

    # behajtunk a bázisra
    drive_base.straight(-700)


def run__6_futas(motor_config: MotorConfig):
    drive_base = _create_drivebase(motor_config)

    _approach_crane(drive_base)
    _spin_crane(motor_config, drive_base)
    _exit_and_scale(drive_base)
    _return_home(drive_base)
