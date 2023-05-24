import time

start_time = time.process_time()
result = 0
for i in range(100000):
    result += i 

print(result)
end_time = time.process_time()

print(start_time)
print(end_time)
print(f'{int((end_time - start_time) * 1000)} ms')
print('finish')
