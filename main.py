import os, sys


def chagneSep(paramPath: str) -> str:
    paramPath = paramPath.replace(os.sep, "/")
    return "{}".format(paramPath.strip('"').strip("'"))


####################### FILE OPERATIONS #######################################
def scan_hidden_file(paramPath: str) -> list:
    if sys.version_info.major >= 3 and sys.version_info.minor >= 4 and sys.version_info.micro >= 0:
        def isHiddenFileOrDir(ParamFilePath: str) -> bool:
            import stat
            """Only Works nt(Windows) Operating System  if file is hidden return "True" """
            return bool(os.stat(ParamFilePath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

        os.chdir(chagneSep(paramPath))
        file_list = []
        if os.name == "nt":
            for f in os.listdir(os.curdir):
                if not os.path.isdir(f) and not isHiddenFileOrDir(f):
                    split_extension = f.rsplit(".", 1)
                    if len(split_extension) == 1:
                        split_extension.append('sessile')
                    file_list.append(tuple(split_extension))

        else:
            for f in os.listdir(os.curdir):
                if not os.path.isdir(f) and not f.startswith("."):
                    split_extension = f.rsplit(".", 1)
                    if len(split_extension) == 1:
                        split_extension.append('sessile')
                    file_list.append(tuple(split_extension))
        return file_list
    else:
        waring = "Install Python 3.4.0 and higher".upper()
        print("*" * len(sys.version), waring.center(len(sys.version)),
              "Your Python Version Info".center(len(sys.version)), sys.version,
              "*" * len(sys.version), sep="\n")


def isFinished():
    note = "Transaction finished".upper()
    print()
    print("*" * len(note), note, "*" * len(note), sep="\n")
    print()


########################################## Group By Extentions ########################################
def control1(name: str, ex: str) -> None: # ex = extention of file, name = name of file
    from random import random
    if ex != "sessile":
        if not os.path.exists(os.path.join(ex, f"{name}.{ex}")):
            os.rename(f"{name}.{ex}", chagneSep(os.path.join(ex, f"{name}.{ex}")))
        else:
            os.rename(f"{name}.{ex}", chagneSep(os.path.join(ex, f"{str(random())[2:]}-{name}.{ex}")))
    else:
        if not os.path.exists(os.path.join(ex, name)):
            os.rename(name, chagneSep(os.path.join(ex, name)))
        else:
            os.rename(name, chagneSep(os.path.join(ex, f"{str(random())[2:]}-{name}")))


def groupByExtentions(folderPath: str) -> None:
    fileList = scan_hidden_file(folderPath)
    os.chdir(chagneSep(folderPath))
    for name, ex in fileList:
        if not os.path.exists(ex):
            os.mkdir(ex)
            control1(name=name, ex=ex)
        else:
            control1(name=name, ex=ex)
    isFinished()


########################################## Group By Create Date ########################################
def control2(name: str, ex: str, foldername: str) -> None: # ex = extention of file, name = name of file , foldername = File creation date
    from random import random
    if ex != "sessile":
        if not os.path.exists(os.path.join(foldername, f"{name}.{ex}")):
            os.rename(f"{name}.{ex}", chagneSep(os.path.join(foldername, f"{name}.{ex}")))
        else:
            os.rename(f"{name}.{ex}", chagneSep(os.path.join(foldername, f"{str(random())[2:]}-{name}.{ex}")))
    else:
        if not os.path.exists(os.path.join(foldername, name)):
            os.rename(name, chagneSep(os.path.join(foldername, name)))
        else:
            os.rename(name, chagneSep(os.path.join(foldername, f"{str(random())[2:]}-{name}")))


def groupDate(paramPath: str) -> None:
    from datetime import datetime
    fileList = scan_hidden_file(paramPath)
    os.chdir(paramPath)
    for name, ex in fileList:
        if ex == "sessile":
            ctime = datetime.fromtimestamp(os.stat(name).st_ctime).strftime("%d-%m-%Y")
            if not os.path.exists(ctime):
                os.mkdir(ctime)
                control2(name=name, ex=ex, foldername=ctime)
            else:
                control2(name=name, ex=ex, foldername=ctime)
        else:
            ctime = datetime.fromtimestamp(os.stat(f"{name}.{ex}").st_ctime).strftime("%d-%m-%Y")
            if not os.path.exists(ctime):
                os.mkdir(ctime)
                control2(name=name, ex=ex, foldername=ctime)
            else:
                control2(name=name, ex=ex, foldername=ctime)
    isFinished()


if __name__ == "__main__":
    def DisplayMenu() -> None:
        while True:

            note = "Linux systems will be grouped according to the last modified date"
            options = f"1-Group By Extentions\n2-Group By Create Date\n3-Quit"
            print(options)
            print("*" * len(sys.version), note.center(len(sys.version)),
                  "Your Python Version Info".center(len(sys.version)), sys.version, "*" * len(sys.version), sep="\n")
            option = input("Option:")
            print()
            if option == "1":
                path = chagneSep(input("Enter a Folder Path:"))
                if path == "":
                    continue
                groupByExtentions(path)
            elif option == "2":
                path = chagneSep(input("Enter a Folder Path:"))
                if path == "":
                    continue
                groupDate(path)
            elif option == "3":
                break
            else:
                continue


    DisplayMenu()
