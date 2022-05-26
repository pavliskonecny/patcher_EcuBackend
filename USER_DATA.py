"""
Specify patch "project & number & description" appears on main window and use as executable file name.
!!! patch number must be unique because of creating unique backup file names!!!
"""
PATCH_NUMBER = "patch1"
PATCH_PROJECT = "VW 416 PA2"
PATCH_DESCRIPTION = f"Fixed DCL reference issue for right side headlamps"

"""
Specify the relative path for files what should be stored to executable file and replaced later.
"""
PATCH_FILES = [
    "ecuserver/VAG/VW416PA2/VW416PA2BaseService.py",
    "ecuserver/Ecu/LLPMax/LLP_max.py",
]
