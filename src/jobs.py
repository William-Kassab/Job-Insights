from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open(path, mode="r") as file:
        path_reader = csv.DictReader(file)

        list_content = list(path_reader)

    return list_content
