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

samples = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
results = []
sample_method_names = ['data_from_csv']

# function_name = 'create_linked_and_add_sorted'
# function_name = 'search_many_from_linked'
# function_name =  'delete_from_start()'
# function_name =  'linked_list.delete_from_end()'


# function_name = 'bst_tree.create_bst_from_array'
# function_name = 'bst_tree.search_in_bst_by_array'
# function_name = 'bst_tree.delete_tree_in_order'
function_name = 'bst_tree.delete_tree_reverse_order'



machine_name = 'mikolaj'
# machine_name = 'mac'
# machine_name = 'lenovo'

for sample_method_name in sample_method_names:
    print('============================================================')
    print('= ' + sample_method_name)
    results = []
    for sample_size in samples:
        setup_core = f'''
import random
import data_samples
import time
import service
import linked_list
import bst_tree
data = data_samples.data_from_csv({sample_size})
linked_list_instance = linked_list.create_linked_and_add_sorted(data)
bst_tree_instance = bst_tree.create_bst_from_array(data)
'''

        # Tworzenie linked
        # stmt = 'linked_list.create_linked_and_add_sorted(data)'

        #  szukanie w linked
        # stmt = "linked_list.search_many_from_linked(linked_list_instance, data)"

        # usuwanie od poczatku
        # stmt = 'linked_list.delete_from_start(linked_list_instance)'
        # usuwanie od konca
        # stmt = 'linked_list.delete_from_end(linked_list_instance)'

        # tworzenie bst
        # stmt = 'bst_tree.create_bst_from_array(data)'
        # szukanie w bst
        # stmt = 'bst_tree.search_in_bst_by_array(bst_tree_instance, data)'
        # uuswanie w bst in order
        # stmt = 'bst_tree.delete_tree_in_order(bst_tree_instance)'
        # uuswanie w bst reverse in order
        stmt = 'bst_tree.delete_tree_reverse_order(bst_tree_instance)'



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
