"""
Specify patch "project & number & description" appears on main window and use as executable file name.
!!! patch number must be unique because of creating unique backup file names!!!
"""
PATCH_NUMBER = "patch1"
PATCH_PROJECT = "VW 416 GP"
PATCH_DESCRIPTION = f"USE THIS PATCH FOR ECUBACKEND 22.05.17 ONLY !!!\n\n" \
                    f"- Fixed DCL reference issue\n"

"""
Specify the relative path for files what should be stored to executable file and replaced later.
"""
PATCH_FILES = [
    "ecuserver/VAG/vagservice.py",
]
