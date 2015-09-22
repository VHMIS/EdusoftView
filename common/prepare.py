import os


def mount_data_macos():
    directory = "~/foldername"
    if not os.path.exists(directory): os.makedirs(directory)
    os.system("mount_smbfs //user.name:password@server/servershare ~/foldername")


def mount_data_linux():
    directory = "~foldername"
    if not os.path.exists(directory): os.makedirs(directory)
    os.system("smbmount \\server\sservershare ~/foldername -ousername=...,password=...")