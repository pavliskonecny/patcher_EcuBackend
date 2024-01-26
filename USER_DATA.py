"""
Specify patch "project & number & description" appears on main window and use as executable file name.
!!! patch number must be unique because of creating unique backup file names!!!
"""
PATCH_NUMBER = "patchX"
PATCH_PROJECT = "AudiQ6"
PATCH_DESCRIPTION = f"USE THIS PATCH FOR EcuBackend 22.XX.XX ONLY !!!\n\n" \
                    f"test iTACu"

"""
Specify the relative path for files what should be stored to executable file and replaced later.
"""
PATCH_FILES = [
    "ecuserver/VAG/vagservice.py"
]

"""
Specify the relative path for files what are new and it is not possible to backup. But they must be in PATCH_FILES !
"""
NEW_PATCH_FILES = [
]
