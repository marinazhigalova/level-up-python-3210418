def index_all(input, value):
    indices = []

    for index, i in enumerate(input):
        if i == value:
            indices.append([index])
        elif isinstance(input[index], list):
            for j in index_all(input[index], value):
                indices.append([index]+j)
                
    return indices


# commands used in solution video for reference
if __name__ == '__main__':
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(index_all(example, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
    print(index_all(example, [1, 2, 3]))  # [[0, 0], [1]]