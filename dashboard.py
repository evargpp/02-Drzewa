import copy
import random
import statistics
import config
import data_samples
import time
import service
import timeit
import sys
import linked_list
import bst_tree
sys.setrecursionlimit(10000)

setup_core = '''
import random
import data_samples
import time
import service
import linked_list
import bst_tree
'''

samples = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
results = []
# random.shuffle(samples)

sample_method_names = ['data_from_csv']

#               Linked
# function_name = 'create_linked_and_add_sorted'
function_name = 'search_many_from_linked'
# function_name = 'delete_from_start'
# function_name = 'delete_from_start'

#               Tree
# function_name = 'create_bst_from_array'

# machine_name = 'lenovo'
# machine_name = 'mac'
machine_name = 'mikolaj'

for sample_method_name in sample_method_names:
    print('============================================================')
    print('= ' + sample_method_name)
    results = []
    for sample_size in samples:
        #                         Tworzednie noda i dodawanie
        # stmt = 'linked_list.' + function_name + '(data_samples.' + sample_method_name + '(' + str(sample_size) + '))'

        #                          Szukanie (w opraciu o liste pomocniczą - od poczatku)
        # linked_list = linked_list.create_linked_and_add_sorted(data_samples.data_from_csv(str(sample_size)))
        stmt = 'linked_list.' + function_name + '(' + linked_list + ',data_samples.' + sample_method_name + '(' + str(sample_size) + '))'

        #                           Usuwanie od początku
        #                           Usuwanie od końca

        #                           budowanie drzewa
        # stmt = 'bst_tree.' + function_name + '(data_samples.' + sample_method_name + '(' + str(sample_size) + '))'




        # stmt = 'sorting_method.' + sorting_method_name + '(data_samples.' + sample_method_name + '(' + str(sample_size) + '))'
        results_times = timeit.Timer(stmt, setup=setup_core).repeat(config.ti_repeat, config.ti_number)
        result_one = {
            'sample_size': sample_size,
            'min': min(results_times),
            'max': max(results_times),
            'avg': statistics.mean(results_times)
        }
        results.append(result_one)
        print(result_one)
    service.create_file(results, function_name, sample_method_name, machine_name)
