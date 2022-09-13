"""
Specify patch "project & number & description" appears on main window and use as executable file name.
!!! patch number must be unique because of creating unique backup file names!!!
"""
PATCH_NUMBER = "patch1"
PATCH_PROJECT = "LiXiang X01"
PATCH_DESCRIPTION = f"USE THIS PATCH FOR EcuBackend 22.08.23 ONLY !!!\n\n" \
                    f"- added services FanControl, MotorLeveler, SecurityAccess"

"""
Specify the relative path for files what should be stored to executable file and replaced later.
"""
PATCH_FILES = [
    "ecuserver/Ecu/LHCM/LHCM.py",
    "ecuserver/Ecu/LHCM/security_handler.py",
    "ecuserver/EcuServicesFuncs/LHCMServiceFunctions.py",
    "ecuserver/LiXiang/LiaX01/LiaX01Service.py",
    "ecuserver/CAN_Trace/ECU/LHCM_CanCyclic.csv"
]

"""
Specify the relative path for files what are new and it is not possible to backup. But they must be in PATCH_FILES !
"""
NEW_PATCH_FILES = [
    "ecuserver/Ecu/LHCM/security_handler.py",
]
