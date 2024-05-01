import data_samples
import copy
import csv
import os

target_directory = "randoms/"

# kod ktory generuje 20 plikow csv, kazda z randomowymi liczbami od 100 do 2000
def random_array_files():
    for i in range(20):
        n = (i + 1) * 100;
        array = copy.deepcopy(data_samples.random_without_repeats(n))
        save_file(array)


def save_file(array):
    file_name = "random" + str(len(array)) + '.csv'

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    target_file_path = os.path.join(target_directory, file_name)

    with open(target_file_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(array)

random_array_files()
