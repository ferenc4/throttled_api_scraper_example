import csv
import os.path
from os import path


def save_to(filename, obj):
    exists = path.exists(filename)
    with open(filename, 'a', newline='\n', encoding='utf-8') as f:
        if not exists:
            writer = csv.writer(f)
            writer.writerow(obj.__dict__.keys())
        writer = csv.DictWriter(f, fieldnames=obj.__dict__.keys())
        writer.writerow(obj.__dict__)
