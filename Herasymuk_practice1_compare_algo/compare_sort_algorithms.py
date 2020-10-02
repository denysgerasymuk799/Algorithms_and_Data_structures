import json
import random
import time

from sort_algorithms import selection_sort, insertion_sort, shell_sort, start_merge_sort


def generate_array(numbers_array, n_experiment, len_array):
    """

    :param numbers_array: a list of numbers from 0 to pow(2, 15) to save time on creating random lists,
    instead every time generate random number I use random.sample from this numbers_array
    :param n_experiment: a number of experiment to understand what type of array to return
    :param len_array: a length of returned array
    :return: a random array with len_array length
    """
    array = []
    if n_experiment == 1:
        # get an array of len_array length randomly chosen elements
        # from numbers_array
        array = random.sample(numbers_array, k=len_array)

    elif n_experiment == 2:
        # get an array of len_array length from 0 to len_array
        # in numbers_array
        array = numbers_array[:len_array]

    elif n_experiment == 3:
        # get an array of len_array length from 0 to len_array
        # in numbers_array and reverse it
        array = numbers_array[:len_array]
        array.reverse()

    elif n_experiment == 4:
        # shuffle elements of previous array fro fourth experiment
        random.shuffle(numbers_array)

    return array


def compare_algorithms_time():
    """

    :return: save a json with all experiments data, format is such:
     "experiment1": {
        "selection_sort": {
            "array_size": [],
            "algorithm_time": [],
            "algorithm_if_operations": []
            },
        "insertion_sort": {
            "array_size": [],
            "algorithm_time": [],
            "algorithm_if_operations": []
            }
        ...
    "experiment2": {....


    """
    # start power - a minimum length of array to sort
    # end power - a maximum length of array to sort
    start_pow = 5
    end_pow = 15
    end_len_array = pow(2, end_pow)
    numbers_array = [i for i in range(end_len_array)]

    # create array123 of {1, 2, 3} repeated elements
    one_third_len = end_len_array // 3
    array1 = [1 for _ in range(one_third_len)]
    array2 = [2 for _ in range(one_third_len)]
    array3 = [3 for _ in range(end_len_array - 2 * one_third_len)]
    array123 = array1 + array2 + array3

    # create len_arrays of length of arrays for cycle
    len_arrays = []
    for i in range(start_pow, end_pow + 1):
        len_arrays.append(pow(2, i))

    algorithms_names = ["selection_sort", "insertion_sort", "merge_sort", "shell_sort"]

    # create a structure of result json of data for experiments
    experiments_data_dict = dict()
    for n_experiment in range(1, 5):
        algorithms_data_dict = dict()
        for i, algo in enumerate(algorithms_names):
            algorithms_data_dict[algo] = {
                "array_size": len_arrays,
                "algorithm_time": [0 for _ in range(end_pow - start_pow + 1)],
                "algorithm_if_operations": [0 for _ in range(end_pow - start_pow + 1)]
            }

        experiments_data_dict["experiment" + str(n_experiment)] = algorithms_data_dict

    for n_experiment in range(1, 5):
        # a variable to save position length of a current array
        # to get it from len_arrays to save the result of experiment
        # on certain position in result json
        step_len_array = 0
        for len_array in len_arrays:
            print("len_array", len_array)
            print("n_experiment", n_experiment)

            # a variable to repeat experiments 1th and 4th
            make_experiments = 1

            if n_experiment == 1:
                make_experiments = 5

            elif n_experiment == 4:
                make_experiments = 3

            array = []

            # dicts to save time of each repeated experiment and after to get mean value of it
            algo_times_dict = {
                0: [],
                1: [],
                2: [],
                3: []
            }

            algo_if_operations_dict = {
                0: [],
                1: [],
                2: [],
                3: []
            }
            for i in range(make_experiments):
                if n_experiment == 4:
                    if i == 0:
                        array = random.sample(array123, k=len_array)

                    else:
                        # for 4th experiment after first repetition of experiment we should
                        # shuffle the same elements of first array
                        generate_array(array, n_experiment, len_array)

                else:
                    array = generate_array(numbers_array, n_experiment, len_array)

                algo_time, if_operations = 0, 0
                time_difference = 0
                for n_algorithm in range(1, 5):
                    if n_algorithm == 1:
                        start_time = time.perf_counter()
                        if_operations = selection_sort(array)
                        time_difference = time.perf_counter() - start_time
                        print("Selection sort time", time_difference)

                    elif n_algorithm == 2:
                        start_time = time.perf_counter()
                        if_operations = insertion_sort(array)
                        time_difference = time.perf_counter() - start_time
                        print("Insertion sort time", time_difference)

                    elif n_algorithm == 3:
                        start_time = time.perf_counter()
                        if_operations = start_merge_sort(array, if_operations)
                        time_difference = time.perf_counter() - start_time
                        print("Merge sort time", time_difference)

                    elif n_algorithm == 4:
                        start_time = time.perf_counter()
                        if_operations = shell_sort(array)
                        time_difference = time.perf_counter() - start_time
                        print("Shell sort time", time_difference, '\n\n\n\n')

                    algo_times_dict[n_algorithm - 1].append(time_difference)
                    algo_if_operations_dict[n_algorithm - 1].append(if_operations)

            # add mean variable of all repetitions of the experiment to result json
            for n_algo_name in range(4):
                experiments_data_dict["experiment" + str(n_experiment)][algorithms_names[n_algo_name]]["algorithm_time"][step_len_array] \
                    = sum(algo_times_dict[n_algo_name]) / len(algo_times_dict[n_algo_name])

                experiments_data_dict["experiment" + str(n_experiment)][algorithms_names[n_algo_name]]["algorithm_if_operations"][step_len_array] \
                    = sum(algo_if_operations_dict[n_algo_name]) / len(algo_if_operations_dict[n_algo_name])

            step_len_array += 1

    with open("algorithms_data.json", "w", encoding="utf-8") as f:
        json.dump(experiments_data_dict, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    compare_algorithms_time()
