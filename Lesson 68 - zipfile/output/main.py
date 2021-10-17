from zipfile import ZipFile, Path
from glob import glob

files = glob("**/*.txt",recursive=True)
# print(files)

# with ZipFile("archive.zip","w") as zip:
#     for file in files:
#         zip.write(file)
#     zip.printdir()

# with ZipFile("archive.zip","a") as zip:
    # zip.write("update.txt")
    # zip.printdir()

with ZipFile("archive.zip","a") as zip:
    zip.extractall("archive")
    # zip.extract("test.txt","output")

    # if Path(zip.filename,"update.txt").exists():
        # with zip.open("update.txt","r") as file:
        #     print(file.read())
        # with zip.open("update.txt","w") as file:
        #     file.write(b"Another update")