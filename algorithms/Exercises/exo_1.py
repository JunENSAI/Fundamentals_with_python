import time
from collections import deque

def measure_time(func, *args, repeats=1000):
    """
    Measures the total time to execute func(*args) 'repeats' times.
    """
    start_time = time.perf_counter()
    for _ in range(repeats):
        func(*args)
    end_time = time.perf_counter()
    return end_time - start_time

def run_experiment():

    # 1. Generate Datasets
    sizes = [10**3, 10**4, 10**5, 10**6]
    
    # Storage for results
    times_list_lookup = []
    times_set_lookup = []
    times_list_pop = []
    times_deque_pop = []

    print(f"{'N':<10} | {'List Search':<12} | {'Set Search':<12} | {'List Pop(0)':<12} | {'Deque Pop(0)':<12}")
    print("-" * 70)

    for n in sizes:

        data_list = list(range(n))
        data_set = set(data_list)
        data_deque = deque(data_list)
        
        # Target element that guarantees worst-case for List (not present)
        target = -1 
        
        # --- TASK A: Membership (x in collection) ---

        t_list = measure_time(lambda: target in data_list, repeats=100)
        times_list_lookup.append(t_list)

        t_set = measure_time(lambda: target in data_set, repeats=100)
        times_set_lookup.append(t_set)

        # --- TASK B: Deletion (pop(0)) ---
        # Note: We create a copy so we don't empty the original list during the loop
        temp_list = data_list[:] 
        temp_deque = data_deque.copy()
        

        # We define a specific wrapper to avoid measuring the setup time
        def pop_list_zero():
            if temp_list: temp_list.pop(0)
            
        t_list_pop = measure_time(pop_list_zero, repeats=1000)
        times_list_pop.append(t_list_pop)

        def pop_deque_zero():
            if temp_deque: temp_deque.popleft()
            
        t_deque_pop = measure_time(pop_deque_zero, repeats=1000)
        times_deque_pop.append(t_deque_pop)

        print(f"{n:<10} | {t_list:.6f}s    | {t_set:.6f}s    | {t_list_pop:.6f}s    | {t_deque_pop:.6f}s")

if __name__ == "__main__":
    run_experiment()