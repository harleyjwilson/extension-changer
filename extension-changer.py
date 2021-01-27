import os
import shutil

folder = ""
oldExt = ""
newExt = ""


def renameFile(folder, oldExt, newExt):
    print('Renaming files')

    # walks through folder using os.walk(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        print('Scanning ' + folder)
        for file in filenames:
            # select files with the old extension
            if file.endswith(oldExt):
                # moves these files to destination, printing result
                oldFilePath = os.path.join(folder, file)
                newFilePath = os.path.join(
                    folder, file.replace(oldExt, newExt))
                print('folder: %s' % (folder))
                print('file: %s' % (file))
                # print('Renaming %s to %s' % (
                #   oldFilePath, newFilePath))
                # shutil.move(oldFilePath, newFilePath)
    print('File rename complete')


def folderValidation(folder):
    if not folder.startswith('/'):
        folder = '/' + folder

    if not folder.endswith('/'):
        folder = folder + '/'

    return folder


def extValidaiton(extension):
    if not extension.startswith('.'):
        extension = '.' + extension

    return extension


print("Bulk Extension Changer\n")
print("Enter folder location:")
while folder == "":
    folder = str(input())

print("Enter enter old extension:")
while oldExt == "":
    oldExt = str(input())

print("Enter next extension:")
while newExt == "":
    newExt = str(input())

folder = folderValidation(folder)
oldExt = extValidaiton(oldExt)
newExt = extValidaiton(newExt)

renameFile(folder, oldExt, newExt)
