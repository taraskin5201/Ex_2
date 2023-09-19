import random
import threading

def calculate_pi_single_thread(num_points):
    inside_circle = 0
    for _ in range(num_points):
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (inside_circle / num_points) * 4

def calculate_pi_multi_thread(num_points, num_threads):
    points_per_thread = num_points // num_threads
    results = []

    def thread_function(thread_id):
        inside_circle = 0
        for _ in range(points_per_thread):
            x, y = random.uniform(0, 1), random.uniform(0, 1)
            if x**2 + y**2 <= 1:
                inside_circle += 1
        results.append(inside_circle)

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=thread_function, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_inside_circle = sum(results)
    return (total_inside_circle / num_points) * 4

if __name__ == "__main__":
    num_points = 1000000  # Змініть це значення на бажану кількість точок
    num_threads = 4  # Змініть це значення на бажану кількість потоків

    # Обчислення Пі в одному потоці
    pi_single_thread = calculate_pi_single_thread(num_points)
    print("Pi (Single Thread):", pi_single_thread)


