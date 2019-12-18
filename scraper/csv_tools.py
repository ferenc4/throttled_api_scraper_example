import csv
import os
import os.path
import shutil
from csv import DictReader, DictWriter
from os import path
from tempfile import NamedTemporaryFile


def save_to(filename, obj):
    exists = path.exists(filename)
    headers: []
    if exists:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            headers = next(reader)
    with open(filename, 'a', newline='\n', encoding='utf-8') as f:
        current_headers = obj.__dict__.keys()
        if not exists:
            writer = csv.writer(f)
            writer.writerow(current_headers)
        elif headers != current_headers:
            raise Exception("Current headers {} didn't match the original ones {} in {}."
                            .format(headers.__dict__, current_headers, filename))
        writer = csv.DictWriter(f, fieldnames=current_headers)
        writer.writerow(obj.__dict__)


def append_csv(csv_filename, dict_val: dict):
    exists = path.exists(csv_filename)
    with open(csv_filename, 'a+', newline='\n', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        original_header = []
        if exists:
            csv_file.seek(0, os.SEEK_SET)
            original_header = next(csv.reader(csv_file))
        new_keys = set(dict_val.keys()).difference(original_header)
        if not new_keys:
            csv_file.seek(0, os.SEEK_END)
            writer = csv.DictWriter(csv_file, fieldnames=original_header)
            writer.writerow(dict_val)
        else:
            original_header.extend(sorted(new_keys))
            with open(temp_filename_for(csv_filename), 'w+', newline='\n', encoding='utf-8') as temp_file:
                writer = csv.DictWriter(temp_file, fieldnames=original_header, lineterminator='\n')
                writer.writeheader()
                csv_file.seek(0, os.SEEK_SET)
                writer.writerows(row for row in reader)
                writer.writerow(dict_val)
            shutil.move(temp_file.name, csv_filename)


def temp_filename_for(filename):
    index = filename.index('.')
    return filename[:index] + '-temp' + filename[index:]
