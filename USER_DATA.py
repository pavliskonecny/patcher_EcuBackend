"""
Specify patch "project & number & description" appears on main window and use as executable file name.
!!! patch number must be unique because of creating unique backup file names!!!
"""
PATCH_NUMBER = "patch1"
PATCH_PROJECT = "Lamborghini LB744"
PATCH_DESCRIPTION = f"USE THIS PATCH FOR EcuBackend 22.04.28 ONLY !!!\n\n" \
                    f"- added control of addHB via light distributions\n\n" \
                    f"- added reading of VW FAZIT String"

"""
Specify the relative path for files what should be stored to executable file and replaced later.
"""
PATCH_FILES = [
    "ecuserver/VAG/LamborghiniLB744/LamborghiniLB744.py",
    "ecuserver/VAG/LamborghiniLB744/LamborghiniLB744Service.py",
    "ecuserver/VAG/LamborghiniLB744/mxb_distribution_definition.py",
]
