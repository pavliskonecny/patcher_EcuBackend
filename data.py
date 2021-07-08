"""
Specify patch "project & number & description" appears on main window and use as executable file name. Example:

PATCH_PROJECT = "Audi Q6"
PATCH_NUMBER = "patch 1"
PATCH_DESCRIPTION = "measurement fix"
"""

#!!! patch number must be unique because of creating unique backup file names!!!
PATCH_NUMBER = "patch 1"
PATCH_PROJECT = "Audi Q6"
PATCH_DESCRIPTION = "measurement fix"

"""
Specify the absolute path for files what should be stored to executable file and replaced later. Example:

PATCH_FILES = [
    "C:\\Data\\DEV\\src\\Ecu.Server\\VAG\\VWIDBuzz\\VWIDBuzzTOP.py",
    "C:\\Data\\DEV\\src\\Ecu.Server\\VAG\\VWIDBuzz\\VWIDBuzzTOPService.py",
]
"""

PATCH_FILES = [
    "C:\\Users\\konepa1\\Desktop\\test_patcher\\one.jpg",
    "C:\\Users\\konepa1\\Desktop\\test_patcher\\two.jpg",
]