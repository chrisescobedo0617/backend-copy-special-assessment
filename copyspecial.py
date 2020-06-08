#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "chrisescobedo0617"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    file_list = []
    file_names = os.listdir(dirname)
    pattern = re.compile(r'__\w+__')
    for file_ in file_names:
        match_object = pattern.search(file_)
        if match_object:
            full_path = os.path.join(dirname, file_)
            file_list.append(os.path.abspath(full_path))
    return file_list


def copy_to(path_list, dest_dir):
    """Given a list of file paths, copies those
    files into the given directory."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    else:
        print('sorry, path exists')
    for file_ in path_list:
        print(f'copying {file_} to {dest_dir}')
        shutil.copy(file_, dest_dir)


def zip_to(path_list, dest_zip):
    """Given a list of file paths,
    zip those files up into the given zip path."""
    print("Command I'm going to do:")
    print(f"zip -j {dest_zip} {' '.join(path_list)}")
    cmd = ['zip', '-j', dest_zip]
    cmd.extend(path_list)
    subprocess.call(cmd)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    directory = ns.from_dir
    special_files = get_special_paths(directory)
    if ns.todir:
        copy_to(special_files, ns.todir)
    if ns.tozip:
        zip_to(special_files, ns.tozip)
    if not ns.tozip and not ns.todir:
        print('\n'.join(special_files))


if __name__ == "__main__":
    main(sys.argv[1:])
