#!/usr/bin/python3
"""Reads '/etc/passwd' '/etc/group' and network configuration via ifconfig
and outputs the collected data to a csv file

Authors: Jin Nagai, Quinn Brittain
"""

import subprocess
import csv  # import csv module
import datetime
import os
import sys


def readLinuxData(filename):
    """Reads data from a passwd or group file into a dictionary of lists

    ### Args:
        filename : str
            Name of the file
    ### Returns:
        Type : list[str]
            list of user/group entries
    ### Raises:
        OSError
            If unable to open file
    """
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter=':')
        rows = []
        for row in csv_reader:
            rows.append(row)
    return rows


def readCSVData(filename):
    """Reads data from a csv file into a dictionary of lists

    ### Args:
        filename : str
            Name of the file
    ### Returns:
        Type : dict{list[str]}
            The dict uses:
                'headers' for the list headers
                'rows' for the list of rows
    ### Raises:
        OSError
            If unable to open file
    """
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        rows = []
        headers = next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    return {'headers': headers, 'rows': rows}


def writeUsers(users, filename):
    """Writes a 2D list of users into a file in csv format

    ### Args:
        users : list[list[str]]
            List of users and there properties
        filename : str
            Name of the file
    ### Returns:
        Type : void
    ### Raises:
        OSError
            If unable to open file
    """
    with open(filename, 'a') as file:
        file.write("==Users==\n")
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Username', 'X', 'UID', 'GID', 'Fullname',
                             'Home Directory', 'Default Shell'])
        count = 0
        for user in users:
            csv_writer.writerow(user)
            count += 1
        file.write("Total Users,{}\n\n".format(count))


def writeGroups(groups, filename):
    """Writes a 2D list of groups into a file in csv format

    ### Args:
        groups : list[list[str]]
            List of groups and there properties
        filename : str
            Name of the file
    ### Returns:
        Type : void
    ### Raises:
        OSError
            If unable to open file
    """
    with open(filename, 'a') as file:
        file.write("==Groups==\n")
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Group Name', 'X', 'GID', 'Users'])
        count = 0
        for group in groups:
            csv_writer.writerow(group)
            count += 1
        file.write("Total Groups,{}\n\n".format(count))


def main():
    """Reads '/etc/passwd' '/etc/group' and network configuration via ifconfig
    and outputs the collected data to a csv file
    """
    filename = "system_audit.csv"
    users = []
    groups = []

    try:
        users = readLinuxData('/etc/passwd')
    except FileNotFoundError:
        print("Error: File not found: '/etc/passwd'")
    except PermissionError:
        print("Error: Permission denied: Read access denied for '/etc/passwd'")
    try:
        groups = readLinuxData('/etc/group')
    except FileNotFoundError:
        print("Error: File not found: '/etc/group'")
    except PermissionError:
        print("Error: Permission denied: Read access denied for '/etc/group'")
    network = subprocess.run(["ifconfig"], capture_output=True, text=True, check=False)

    try:
        with open(filename, 'a') as file:
            file.write("Audit Started at: {}\n".format(datetime.datetime.now()))
            file.write("Audit Started by: {}\n\n".format(os.getlogin()))
            file.write("==Network==\n")
            file.write("{}\n\n".format(network.stdout))
        writeUsers(users, filename)
        writeGroups(groups, filename)
    except PermissionError:
        print("Error: Unable to create output file: Write access denied for '{}'".format(os.getcwd))


main()

# reading data --> returns output list of lists
# def read_data(csv_file):
#     reader = csv.reader(open(csv_file))
#     next(reader)
#     output = []
#     return output

# create new csv file to display users, groups, and network connection.
# def create_file(list_file):
#     with open("usercontent.csv", "w") as f:
#         p1 = subprocess.run(["cat", "/etc/passwd"], stdout=f, text=True)
#         p2 = subprocess.run(["cat", "/etc/passwd"], capture_output=True, text=True)
#         # show how many lines are in the file /etc/shadow
#         p3 = subprocess.run(["cat", "/etc/group"], capture_output=True, text=True, input=p2.stdout)
#         # displays network connection
#         p4 = subprocess.run(["ifconfig"], capture_output=True, text=True, input=p3.stdout)
#         p5 = subprocess.run(["wc", "-l", "usercontent.csv"],
#                             capture_output=True, text=True, input=p4.stdout)
#         writer = csv.writer(f)
#         writer.writerows(p3.stdout)
#         writer.writerows(p4.stdout)
#         writer.writerows(p5.stdout)
#         writer.writerows(list_file)

# calling methods
# result = read_data("usercontent.csv")
# create_file(result)
