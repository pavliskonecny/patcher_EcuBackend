"""
Specify patch "project & number & description" appears on main window and use as executable file name.
"""
#!!! patch number must be unique because of creating unique backup file names!!!
PATCH_NUMBER = "patch1"
PATCH_PROJECT = "Audi Q6"
PATCH_DESCRIPTION = "added direct fan control + signal animations"

"""
Specify the absolute path for files what should be stored to executable file and replaced later.
"""
PATCH_FILES = [
    "C:\\Data\\DEV\\src\\Ecu.Server\\z_test_patcher\\one.jpg",
    "C:\\Data\\DEV\\src\\Ecu.Server\\z_test_patcher\\two.jpg",
]
