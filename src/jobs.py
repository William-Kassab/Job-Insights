from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open(path, mode="r") as file:
        path_reader = csv.DictReader(file)

        list_content = list(path_reader)

    """Reads a file from a given path and returns its contents
    
    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    return list_content
