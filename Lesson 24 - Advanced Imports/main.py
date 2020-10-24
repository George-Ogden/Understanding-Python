import math
print(math.pi)
from math import pi
print(pi)
import base
print(base)
print(base.Base)
from base import Base
main_item = Base()
main_item.run()
from folder.file import File
main_item = File()
main_item.run()
from folder.subfolder import subfile
print(subfile)
print(subfile.File)
from folder.subfolder.subfile import File
main_item = File()
main_item.run()
# import file with spaces => SyntaxError: invalid syntax
file_with_spaces = __import__("file with spaces")
print(file_with_spaces)
main_item = file_with_spaces.Spaces()
main_item.run()
import class_folder
print(class_folder)
# print(class_folder.run) => AttributeError: module 'class_folder' has no attribute 'run'