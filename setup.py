import os
import sys
import files

# ******************************************************
# CHANGE THIS PARAMETERS AS NEEDED
main_py_file_name = 'main.py'

add_exe_file_name = True    # False will make exe file name the same like project name folder
exe_file_name = f"{files.get_patch_project()} {files.get_patch_number()}"

add_icon = True             # Add exe file icon
ico_name = "images\\MateoEcuServer.ico"

add_folder = True           # Include folder to exe file
add_folder_name = files.PATCH_FILES_FOLDER

gui_app = True              # False will take console app, True will take GUI app

one_file = True             # True means one exe file. False means folder with necessary files + exe file
# ******************************************************


def make_build():
    project_name = _get_project_name()
    project_folder = _get_project_folder()

    cmd = "pyinstaller --noconfirm --log-level=WARN --clean"

    if one_file:
        cmd += " --onefile"

    if gui_app:
        cmd += " --noconsole"

    if add_folder:
        cmd += " --add-data " + project_folder + "\\" + add_folder_name + ";" + add_folder_name

    cmd += " " + project_folder + "\\" + main_py_file_name
    cmd += " --name " + project_name
    cmd += " --specpath " + project_folder + "\\build\\"    # for spec file
    cmd += " --workpath " + project_folder + "\\build\\"    # for build file
    cmd += " --distpath " + project_folder + "\\dist\\"     # for distribution exe file

    if add_icon:
        cmd += " --icon " + project_folder + "\\" + ico_name  # --icon MyIcon.ico

    #cmd += " --exclude-module numpy"

    print("... required command is: " + cmd)
    os.system('cmd /c "' + cmd + '"')  # execute cmd


def _get_project_name():
    if add_exe_file_name:
        return "\"" + exe_file_name + "\""  # quotation marks are here because of possible spaces in the exe file name
    else:
        return os.path.basename(_get_project_folder())  # get project name


def _get_project_folder():
    # res = str(os.path.abspath(os.curdir))  #by this you will get current FILE folder, not PROJECT folder
    # res = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #by this you will get path without last folder
    res = sys.path[1]
    return res


def open_folder():
    dist_path = _get_project_folder() + "\\dist\\"
    cmd = "explorer " + dist_path  # explorer C:/Users/konepa1/PycharmProjects/test/dist

    os.system('cmd /c "' + cmd + '"')  # execute cmd


if __name__ == "__main__":
    print("Copy \"patch files\" to project folder ...")
    files.copy_files_to_project()
    print("Successful!")
    print("Start building ...")
    make_build()
    print("Successful!")
    open_folder()
