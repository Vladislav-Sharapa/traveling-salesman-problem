from typing import List
import os

def read_file() -> List[List[int]]:
    '''Read matrix from txt file'''
    matrix: List[List[int]] = None
    with open(os.path.join(os.path.dirname(__file__),'matrix.txt')) as f:
        matrix = [list(map(int, row.split())) for row in f.readlines()]
    return matrix


def write_matrix_in_file(matrix: List[List[int]]):
    '''Write matrix in txt file'''
    try:
        with open(os.path.join(os.path.dirname(__file__),'matrix.txt'), 'w') as file:
            for row in matrix:
                file.write(' '.join(str(element) for element in row) + '\n')
        print("The matrix was successfully written to the file")
    except IOError:
        print("Error writing to file")


def write_result_in_file(city_count, execution_time):
    is_existing_count = False

    with open(os.path.join(os.path.dirname(__file__),'results.txt'), 'a+') as file:
        file.seek(0)
        for line in file:
            saved_city_count, _ = line.split('-')
            saved_city_count = saved_city_count.strip()

            if saved_city_count == str(city_count):
                is_existing_count = True
                # file.seek(file.tell() - len(line))
                # file.write(f'{city_count}-{execution_time}\n')
                break

        if not is_existing_count:
            file.write(f'{city_count}-{execution_time}\n')

def read_pair_from_file():
    data = []
    print(os.path.dirname(__file__))
    with open(os.path.join(os.path.dirname(__file__),'results.txt'), 'r') as file:
        for line in file:
            x, y = line.strip().split('-')  
            data.append((float(x), float(y))) 
    return data