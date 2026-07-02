import os
import datetime


folder = input("Enter the folder path: ")

if not os.path.exists(folder):
    print("Folder does not exist")
    exit()
total_files = 0
total_size = 0
largest_file_size = 0
largest_file_name = ""



for root, dirs, files in os.walk(folder):

    for file in files:
        total_files += 1
        file_size= os.path.getsize(os.path.join(root, file))
        total_size += file_size
        if file_size>largest_file_size:
            largest_file_size = file_size
            largest_file_name = file



def convert_size(size):

    if size < 1024:
        return f"{size} Bytes"

    elif size < 1024 * 1024:
        return f"{size / 1024:.2f} KB"

    elif size < 1024 * 1024 * 1024:
        return f"{size / (1024 * 1024):.2f} MB"

    else:
        return f"{size / (1024 * 1024 * 1024):.2f} GB"


def file_write(tfile,tsize,lname,lsize):
    result = (
        "=================DIRECTORY REPORT==================\n\n"
        f"Total Files        :  {tfile}\n"
        f"Total Size         :  {tsize}\n"
        f"Largest File       :  {lname}\n"
        f"Largest File Size  :  {lsize}\n"
        f"Generated on       : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    return result


def main():
    tfile = total_files
    tsize = convert_size(total_size)
    lname = largest_file_name
    lsize = convert_size(largest_file_size)

    print(file_write(tfile, tsize, lname, lsize))


    op = open("report.txt", "w")
    op.write(file_write(tfile, tsize, lname, lsize))

    op.close()


main()
