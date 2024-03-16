import os
import ctypes
import win32api
import win32con
import win32gui
import sys  # Add this line

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

print("Script started.")

if is_admin():
    print("Running with admin privileges.")
    
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Path to your .ico file
    icon_path = os.path.join(script_dir, "ASSETS", "Icons", "filetype.ico")

    # Path to your .ice files
    file_extension = ".ice"

    # Set the icon for the file type
    win32api.RegSetValue(
        win32con.HKEY_CLASSES_ROOT,
        file_extension,
        win32con.REG_SZ,
        "IceFile"
    )

    win32api.RegSetValue(
        win32con.HKEY_CLASSES_ROOT,
        "IceFile",
        win32con.REG_SZ,
        "ICE File"
    )

    win32api.RegSetValue(
        win32con.HKEY_CLASSES_ROOT,
        "IceFile\\DefaultIcon",
        win32con.REG_SZ,
        icon_path
    )

    # Refresh the shell icon cache
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, "Environment")

    print("Icon set successfully!")
else:
    print("Admin privileges not available. Script terminated.")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

print("Script finished.")
