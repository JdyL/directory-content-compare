import os


def get_content_directory(directory):
    return os.listdir(directory)  # returns list


def compare_content(directory_one, directory_two):
    directory_one_contents = get_content_directory(directory_one)
    directory_two_contents = get_content_directory(directory_two)

    if (len(directory_one_contents) > len(directory_two_contents)):
        return compare_file_operation(directory_one_contents, directory_two_contents)
    else:
        return compare_file_operation(directory_two_contents, directory_one_contents)


def compare_file_operation(major_list, minor_list):
    difference = []
    for x in major_list:
        found = False
        for y in minor_list:
            if (str(x) == str(y)):
                found = True
                break
        if not found:
            difference.append(str(x))

    return difference


# def input():
firstDirectory = input("First directory? ")
secondDirectory = input("Second directory? ")
answer = input("Confirm to compare contents of " +
               firstDirectory + " and " + secondDirectory + "? (Y/n) ")

if (answer == 'Y'):
    for x in compare_content(firstDirectory, secondDirectory):
        print(x)
