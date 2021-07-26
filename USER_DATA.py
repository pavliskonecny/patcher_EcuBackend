"""
Specify patch "project & number & description" appears on main window and use as executable file name.
"""
#!!! patch number must be unique because of creating unique backup file names!!!
PATCH_NUMBER = "patch2"
PATCH_PROJECT = "Audi Q6"
PATCH_DESCRIPTION = "added direct fan control + signal animations"

"""
Specify the relative path for files what should be stored to executable file and replaced later.
"""
PATCH_FILES = [
    "VAG/AudiQ6/AudiQ6Headlamp.py",
    "VAG/AudiQ6/AudiQ6MXBCCCService.py"
]
