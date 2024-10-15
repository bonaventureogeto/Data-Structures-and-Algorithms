from collections import deque

def generate_binary_numbers(n):
    queue = deque(['1'])
    result = []

    for _ in range(n):
        front = queue.popleft()
        result.append(front)

        queue.append(front + '0')
        queue.append(front + '1') # 10, 11
    return result

n = int(input("Please enter a number: "))

print(generate_binary_numbers(n))
