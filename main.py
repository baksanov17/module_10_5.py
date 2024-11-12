from time import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]
list(filenames)
print(filenames)


start = time()
for file in filenames:
    read_info(file)
end = time()
print(f'Время линейного вычисления: {end - start}')

if __name__ == '__main__':
    start = time()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    end = time()
    print(f'Время многопроцессорного вычисления: {end - start}')


