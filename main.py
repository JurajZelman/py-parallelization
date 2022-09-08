"""Copyright (c) 2022 Juraj Zelman"""

import time
from multiprocessing import Pool, cpu_count


def main() -> None:
    """
    Compares both parallel and sequential approaches. Firstly, tasks are
    computed in parallel. Then, tasks are computed sequentially for time
    comparison.
    """
    print(f"You have {cpu_count()} CPUs.", "\n")

    arguments = [1, 2, 3, 4]

    run_tasks_in_parallel(arguments)
    run_tasks_sequentially(arguments)


def run_tasks_in_parallel(arguments: list[int]) -> None:
    """
    Run tasks in parallel using the multiprocessing module.

    Args:
        arguments: List of subtask indices.
    """
    start_t = time.perf_counter()

    with Pool() as pool:
        output = pool.map(run_subtask, arguments)

    # For functions with multiple input arguments use:
    # # multi_args = [(arg1_task1, arg2_task1), (arg1_task2, arg2_task2)]
    # arguments2 = [arg + 10 for arg in arguments]
    # multi_args = zip(arguments, arguments2)
    # with Pool() as pool:
    #     output = pool.starmap(run_subtask_multi_args, multi_args)

    # Different alternatives to map are map_async, imap or imap_unordered.
    # These might be more suitable with respect to speed and memory allocation,
    # depending on your application.

    end_t = time.perf_counter()
    total_t = end_t - start_t

    print(f"Parallel execution completed in {total_t: .3f} seconds.")
    print("Output: ", output, "\n")


def run_tasks_sequentially(arguments: list[int]) -> None:
    """
    Run tasks in sequential order.

    Args:
        arguments: List of subtask indices.
    """

    start_t = time.perf_counter()

    output = []
    for arg in arguments:
        output.append(run_subtask(arg))

    end_t = time.perf_counter()
    total_t = end_t - start_t

    print(f"Sequential execution completed in {total_t: .3f} seconds.")
    print("Output: ", output, "\n")


def run_subtask(index: int) -> tuple[int, float]:
    """
    Function representing the subtask that should be parallelized. This
    template version freezes the program for one second.

    Args:
        index: Index representing the number of the subtask.

    Returns:
        The index of the subtask and the total time of subtask execution.
    """
    start_t = time.perf_counter()
    time.sleep(1)
    end_t = time.perf_counter()
    total_t = round(end_t - start_t, 3)

    return index, total_t


def run_subtask_multi_args(index: int, index2: int) -> tuple[int, int, float]:
    """
    Function representing the subtask with multiple arguments that should be
    parallelized. This template version freezes the program for one second.

    Args:
        index: Index representing the number of the subtask.
        index2: Index representing the number of the subtask added with 10.

    Returns:
        The index of the subtask, the index of the subtask plus 10 and the
        total time of subtask execution.
    """
    start_t = time.perf_counter()
    time.sleep(1)
    end_t = time.perf_counter()
    total_t = round(end_t - start_t, 3)

    return index, index2, total_t


if __name__ == "__main__":
    main()
