def solution(brown, yellow):
    tiles = brown + yellow
    number_list = []
    for i in range(1, tiles + 1):
        if tiles % i == 0 and i > 2:
            size_1 = i
            size_2 = tiles/i
            brown_tiles = size_1 * 2 + size_2 * 2 - 4
            if brown_tiles == brown:
                return sorted([size_1, size_2], reverse=True)
            else:
                continue
        else:
            continue