#!/usr/bin/python3

import os
import sys

if not len(sys.argv) == 2:
    print("Usage: generate.py <folder>")
    sys.exit(1)


def get_script_filename():
    return os.path.basename(sys.argv[0])


excludes = ['index.html', get_script_filename()]


def is_valid_file_to_include(filename):
    return not (filename.startswith('.') or filename in excludes)


def process_file(file, filename, folder):
    path = os.path.join(folder, filename)
    if os.path.isdir(path):
        list_directory(path)
    file.write("<a href=\"%s\">%s</a>\n" % (filename, filename))


def process_file_if_valid(file, filename, folder):
    if is_valid_file_to_include(filename):
        process_file(file, filename, folder)


def loop_folder(file, folder):
    for filename in os.listdir(folder):
        process_file_if_valid(file, filename, folder)


def list_directory(folder):
    file = open(os.path.join(folder, 'index.html'), 'w+')
    file.write("<!DOCTYPE html>\n<html>\n<body>\n")
    loop_folder(file, folder)
    file.write("</body>\n</html>\n")
    file.close()


list_directory(sys.argv[1])