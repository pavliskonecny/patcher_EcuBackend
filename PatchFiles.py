import os
import sys
import USER_DATA
from shutil import copyfile, move, rmtree


class PatchFiles:
    PATCH_FILES_FOLDER = "patch_files"
    _ECU_SERVER_INSTALL_PATH = "C:/Data/Python/venv/ecuserver/Lib/site-packages/"
    _ECU_SERVER_DEV_PATH = "C:/Data/DEV/src/Ecu.Server/"

    PATCH_PROJECT = USER_DATA.PATCH_PROJECT
    PATCH_NUMBER = USER_DATA.PATCH_NUMBER
    PATCH_DESCRIPTION = USER_DATA.PATCH_DESCRIPTION
    patch_files = None

    def __init__(self):
        """
        self.patch_project = USER_DATA.PATCH_PROJECT
        self.patch_number = USER_DATA.PATCH_NUMBER
        self.patch_description = USER_DATA.PATCH_DESCRIPTION
        """
        # Add absolut path to patch files
        self.patch_files = list()
        for rel_path in USER_DATA.PATCH_FILES:
            abs_path = self._ECU_SERVER_INSTALL_PATH + rel_path
            self.patch_files.append(abs_path)

    def _gen_backup_file_name(self, file_path: str) -> str:
        """
        Generate backup file name like CreateServer.py -> CreateServer_VWIDBuzz_patch1.py
        :param file_path: absolute file path
        :return: absolute file path with added "backup postfix" in file name
        """
        postfix = f"_{USER_DATA.PATCH_PROJECT}_{USER_DATA.PATCH_NUMBER}".replace(" ", "_")
        file_name, file_extension = os.path.splitext(file_path)
        destination_path = file_name + postfix + file_extension
        return destination_path

    def check_destination_files(self) -> str:
        msg = ""
        for destination_path in self.patch_files:
            file_exist = os.path.isfile(destination_path)
            if not file_exist:
                raise Exception(f"File can not be replaced because it does not exist!\n{destination_path}")
            msg = msg + f"Required patch file exist... - {destination_path}\n"
        return msg.rstrip()

    def backup_files(self) -> str:
        msg = ""
        for source_path in self.patch_files:
            destination_path = self._gen_backup_file_name(source_path)
            # If backup file exist, then stop
            file_exist = os.path.isfile(destination_path)
            if file_exist:
                raise Exception(f"Patch is installed already because backup file exist already!\n"
                                f"For reinstalling patch you have to uninstall patch as first!\n{destination_path}")
            # Make backup of file
            msg = msg + f"Creating backup patch file... - {destination_path}\n"
            copyfile(source_path, destination_path)
            file_exist = os.path.isfile(destination_path)
            if not file_exist:
                raise Exception(f"File could not be backup! Could be permission denied!\n{destination_path}")
        return msg.rstrip()

    def replace_files(self) -> str:
        msg = ""
        folder_number = 0
        for destination_path in self.patch_files:
            file_name = os.path.basename(destination_path)
            actual_path = str(sys.path[1])
            # temp path of exe file contains this folder "lib-dynload". I don't know why...
            actual_path = actual_path.replace("\\lib-dynload", "")
            source_path = f"{actual_path}\\{self.PATCH_FILES_FOLDER}\\{folder_number}\\{file_name}"
            if not os.path.isfile(source_path):
                raise Exception(f"Internal program error - source file does not exist!\n{source_path}")
            # replace file
            msg = msg + f"Replacing required patch file... - {destination_path}\n"
            copyfile(source_path, destination_path)  # destination folders have to exist as first!!!
            file_exist = os.path.isfile(destination_path)
            if not file_exist:
                raise Exception(f"File could not be created! Could be permission denied!\n{destination_path}")
            folder_number += 1
        return msg.rstrip()

    def restore_backup_files(self) -> str:
        msg = ""
        # Check exist of backup files
        for source_path in self.patch_files:
            destination_path = self._gen_backup_file_name(source_path)
            file_exist = os.path.isfile(destination_path)
            if not file_exist:
                raise Exception(
                    f"Patch can't be uninstalled because backup patch file doesn't exist!\n{destination_path}")

        # Restore backup files
        for source_path in self.patch_files:
            destination_path = self._gen_backup_file_name(source_path)
            msg = msg + f"Restore required patch file ... - {destination_path}\n"
            move(destination_path, source_path)
            backup_exist = os.path.isfile(destination_path)
            orig_exist = os.path.isfile(source_path)
            if backup_exist or not orig_exist:
                raise Exception(f"File could not be restore. Could be permission denied!\n{destination_path}")
        return msg.rstrip()

    @staticmethod
    def copy_files_to_project():
        # remove "patch files folder" because of cleaning
        if os.path.isdir(PatchFiles.PATCH_FILES_FOLDER):
            rmtree(PatchFiles.PATCH_FILES_FOLDER)
        if os.path.isdir(PatchFiles.PATCH_FILES_FOLDER):
            raise Exception("Internal error - Project file folder can not be deleted. Could be permission denied!")
        # create clear folder again
        os.mkdir(PatchFiles.PATCH_FILES_FOLDER)
        if not os.path.isdir(PatchFiles.PATCH_FILES_FOLDER):
            raise Exception("Internal error - Project file folder can not be created. Could be permission denied!")
        # inside create folder 0-x according to count of required files
        folder_number = 0
        for rel_path in USER_DATA.PATCH_FILES:
            source_path = PatchFiles._ECU_SERVER_DEV_PATH + rel_path
            os.mkdir(f"{PatchFiles.PATCH_FILES_FOLDER}\\{folder_number}")
            file_name = os.path.basename(source_path)
            destination_path = f"{PatchFiles.PATCH_FILES_FOLDER}\\{folder_number}\\{file_name}"
            copyfile(source_path, destination_path)  # destination folders have to exist as first!!!
            file_exist = os.path.isfile(destination_path)
            if not file_exist:
                raise Exception(f"File can not be copied to \"project file folder!\" Could be permission denied!\n"
                                f"{destination_path}")
            folder_number += 1


if __name__ == "__main__":
    PatchFiles.copy_files_to_project()
