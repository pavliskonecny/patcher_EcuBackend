import os
import sys
import data
from shutil import copyfile, move, rmtree

_PATCH_FILES_FOLDER = "patch_files"
_ECU_SERVER_PATH = "C:\\Data\\mateo\\EcuBackend\\ecu-server\\server"


def get_patch_project() -> str:
    return data.PATCH_PROJECT


def get_patch_number() -> str:
    return data.PATCH_NUMBER


def get_patch_description() -> str:
    return data.PATCH_DESCRIPTION


def _gen_backup_file_name(file_path: str) -> str:
    """
    Generate backup file name like CreateServer.py -> CreateServer_VWIDBuzz_patch_1.py
    :param file_path: absolute file path
    :return: absolute file path with added "backup postfix" in file name
    """
    postfix = f"_{data.PATCH_PROJECT}_{data.PATCH_NUMBER}".replace(" ", "_")
    dot_index = None
    try:
        dot_index = file_path.index(".")
    except ValueError:
        pass
    if dot_index is not None:
        destination_path = file_path[:dot_index] + postfix + file_path[dot_index:]
    else:
        destination_path = file_path + postfix
    return destination_path


def check_destination_files() -> str:
    msg = ""
    for destination_path in data.PATCH_FILES:
        file_exist = os.path.isfile(destination_path)
        if not file_exist:
            raise Exception(f"File can not be replaced because it does not exist!\n{destination_path}")
        msg = msg + f"Required file exist... - {destination_path}\n"
    return msg.rstrip()


def backup_files() -> str:
    msg = ""
    for source_path in data.PATCH_FILES:
        destination_path = _gen_backup_file_name(source_path)
        # If backup file exist, then stop
        file_exist = os.path.isfile(destination_path)
        if file_exist:
            raise Exception(f"Patch is installed already because backup file exist already!\n"
                            f"For reinstalling patch you have to uninstall patch as first!\n{destination_path}")
        # Make backup of file
        msg = msg + f"Creating backup file... - {destination_path}\n"
        copyfile(source_path, destination_path)
        file_exist = os.path.isfile(destination_path)
        if not file_exist:
            raise Exception(f"File could not be backup! Permission denied probably\n{destination_path}")
    return msg.rstrip()


def replace_files() -> str:
    msg = ""
    folder_number = 0
    for destination_path in data.PATCH_FILES:
        file_name = os.path.basename(destination_path)
        actual_path = str(sys.path[1])
        # temp path of exe file contains this folder "lib-dynload". I don't know why...
        actual_path = actual_path.replace("\\lib-dynload", "")
        source_path = f"{actual_path}\\{_PATCH_FILES_FOLDER}\\{folder_number}\\{file_name}"
        if not os.path.isfile(source_path):
            raise Exception(f"Internal program error - source file does not exist!\n{source_path}")
        # replace file
        msg = msg + f"Replacing required file... - {destination_path}\n"
        copyfile(source_path, destination_path)  # destination folders have to exist as first!!!
        file_exist = os.path.isfile(destination_path)
        if not file_exist:
            raise Exception(f"File could not be created! Permission denied probably\n{destination_path}")
        folder_number += 1
    return msg.rstrip()


def restore_backup_files() -> str:
    msg = ""
    # Check exist of backup files
    for source_path in data.PATCH_FILES:
        destination_path = _gen_backup_file_name(source_path)
        file_exist = os.path.isfile(destination_path)
        if not file_exist:
            raise Exception(f"Patch can not be uninstalled because backup file doesn't exist!\n{destination_path}")

    # Restore backup files
    for source_path in data.PATCH_FILES:
        destination_path = _gen_backup_file_name(source_path)
        msg = msg + f"Restore required file ... - {destination_path}\n"
        move(destination_path, source_path)
        backup_exist = os.path.isfile(destination_path)
        orig_exist = os.path.isfile(source_path)
        if backup_exist or not orig_exist:
            raise Exception(f"File could not be restore! Permission denied probably\n{destination_path}")
    return msg.rstrip()


def copy_files_to_project():
    assert os.path.isdir(_PATCH_FILES_FOLDER), "Internal error - Project files folder doesnt found!"
    # remove "project files folder" because of cleaning
    rmtree(_PATCH_FILES_FOLDER)
    if os.path.isdir(_PATCH_FILES_FOLDER):
        raise Exception("Internal error - Project file folder can not be deleted. Could be permission denied")
    # create clear folder again
    os.mkdir(_PATCH_FILES_FOLDER)
    if not os.path.isdir(_PATCH_FILES_FOLDER):
        raise Exception("Internal error - Project file folder can not be created. Could be permission denied")
    # inside create folder 0-x according to count of required files
    folder_number = 0
    for source_path in data.PATCH_FILES:
        os.mkdir(f"{_PATCH_FILES_FOLDER}\\{folder_number}")
        file_name = os.path.basename(source_path)
        destination_path = f"{_PATCH_FILES_FOLDER}\\{folder_number}\\{file_name}"
        copyfile(source_path, destination_path)  # destination folders have to exist as first!!!
        file_exist = os.path.isfile(destination_path)
        if not file_exist:
            raise Exception(f"File can not be copied to \"project file folder!\" Could be permission denied\n"
                            f"{destination_path}")
        folder_number += 1


if __name__ == "__main__":
    copy_files_to_project()
