import random
import service
import csv


def sort_asc(data_size):
    return [*range(1, data_size + 1)]


def random_without_repeats(data_size):
    temp_list = [*range(1, data_size + 1)]
    random.shuffle(temp_list)
    return temp_list


def data_from_csv(number):

    data_size = number
    file_name = "random" + str(data_size) + ".csv"

    file_path = "randoms/" + file_name

    with open(file_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile)
        data = next(csvreader)
        data = [int(x) for x in data]
    return data


