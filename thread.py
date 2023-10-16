import threading

def print_even_numbers():
    for num in range(2, 21, 2):
        print("Even number:", num)

def print_odd_numbers():
    for num in range(1, 20, 2):
        print("Odd number:", num)

# Create threads
thread1 = threading.Thread(target=print_even_numbers)
thread2 = threading.Thread(target=print_odd_numbers)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

# Print the final message
print("All threads have finished.")