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

    parameters = [1, 2, 3, 4]

    run_tasks_in_parallel(parameters)
    run_tasks_sequentially(parameters)


def run_tasks_in_parallel(parameters: list[int]) -> None:
    """
    Run tasks in parallel using the multiprocessing module.

    Args:
        parameters: List of subtask indices.
    """
    start_t = time.perf_counter()

    with Pool() as pool:
        output = pool.map(run_subtask, parameters)

    end_t = time.perf_counter()
    total_t = end_t - start_t

    print(f"Parallel execution completed in {total_t: .3f} seconds.")
    print("Output: ", output, "\n")


def run_tasks_sequentially(parameters: list[int]) -> None:
    """
    Run tasks in sequential order.

    Args:
        parameters: List of subtask indices.
    """

    start_t = time.perf_counter()

    output = []
    for param in parameters:
        output.append(run_subtask(param))

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


if __name__ == "__main__":
    main()
