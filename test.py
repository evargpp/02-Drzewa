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

# Zaimportowanie Twoich modułów z klasami linked_list i Node oraz funkcje pomocnicze
import linked_list
import data_samples


sample_method_name = 'data_from_csv'

#               Linked
# function_name = 'create_linked_and_add_sorted'
function_name = 'search_many_from_linked'
# function_name = 'delete_from_start'
# function_name = 'delete_from_start'

#               Tree
# function_name = 'create_bst_from_array'
# Rozmiary próbek, dla których chcesz przeprowadzić test

# machine_name = 'lenovo'
# machine_name = 'mac'
machine_name = 'mikolaj'


samples = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Wyniki dla każdego rozmiaru próbki
results = []

for sample_size in samples:
    setup_code = f"""
from __main__ import linked_list, data_samples
data = data_samples.data_from_csv({sample_size})
linked_list_instance = linked_list.create_linked_and_add_sorted(data)
"""

    # Definiowanie funkcji do zmierzenia
    function_to_measure = "linked_list.search_many_from_linked(linked_list_instance, data)"

    # Uruchomienie timeit
    results_times = timeit.repeat(stmt=function_to_measure, setup=setup_code, number=10, repeat=3)

    # Zapisywanie wyników
    result = {
        'sample_size': sample_size,
        'min': min(results_times),
        'max': max(results_times),
        'avg': statistics.mean(results_times)
    }
    results.append(result)
    print(result)

service.create_file(results, function_name, sample_method_name, machine_name)

# Po zakończeniu pętli można np. zapisać wyniki do pliku lub dalej przetwarzać
