import os
import hashlib
import csv


def calculate_md5(file_path):
    with open(file_path, 'rb') as file:
        md5_hash = hashlib.md5()
        while chunk := file.read(4096):
            md5_hash.update(chunk)
        return md5_hash.hexdigest()


def generate_file_list_csv(directory):
    file_list = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            md5 = calculate_md5(file_path)
            file_list.append((len(file_list) + 1, file_path, md5))

    with open('file_list.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Number", "File Path", "MD5"])
        writer.writerows(file_list)


# Specify the directory path
directory_path = "C:/Users/Tom/Desktop/Ex2"

# Generate the file list and CSV
generate_file_list_csv(directory_path)


