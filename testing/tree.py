import os

#This can print a tree structure of the folder. try it.
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        dir_indent = "|   " * (level - 1) + "|-- "
        file_indent = "|   " * level + "|-- "
        if not level:
            print('.')
        else:
            print('{}{}'.format(dir_indent, os.path.basename(root)))
        for f in files:
            print('{}{}'.format(file_indent, f))


list_files(os.path.dirname(__file__))


