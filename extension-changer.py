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
                # newFilePath = os.path.join(folder, file[len(prefix):])

                #print('oldFilePath %s' % (oldFilePath))
                #print('newFilePath %s' % (newFilePath))

                print('Renaming %s to %s' % (
                    oldFilePath, newFilePath))
                shutil.move(oldFilePath, newFilePath)
    print('File rename complete')


print("""
----------------------------
Rename Files in Folder
----------------------------""")
print("Enter folder location:")
folder = str(input())
print("Enter enter old extension:")
oldExt = str(input())
print("Enter next extension:")
newExt = str(input())

renameFile(folder, oldExt, newExt)
