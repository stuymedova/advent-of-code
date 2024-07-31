import sys
import os


def main():
    seeds, maps = handle_input()
    closest_seed = get_closest_seed(seeds, maps)
    print(closest_seed)


def handle_input():
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(
        dirname,
        sys.argv[1] if len(sys.argv) == 2 else 'input.txt'
    )
    seeds = []
    maps = []
    cur_map = []
    with open(file_path) as file:
        for i, line in enumerate(file):
            line = line.strip()
            if i == 0:
                seeds = list(map(lambda x: int(x), line.split(':')[1].split()))
                continue
            if len(line) == 0 or not line[0].isdigit():
                if cur_map:
                    maps.append(cur_map)
                    cur_map = []
                continue
            cur_map.append(list(map(lambda x: int(x), line.split())))
        if cur_map:
            maps.append(cur_map)
    return seeds, maps


def get_closest_seed(seeds, maps):
    closest_seed_location = None
    for seed in seeds:
        pointer = seed
        for map in maps:
            for line in map:
                destination, source, range_length = line
                if pointer in range(source, source + range_length):
                    diff = pointer - source
                    pointer = destination + diff
                    break
        if closest_seed_location is None or pointer < closest_seed_location:
            closest_seed_location = pointer
    return closest_seed_location


if __name__ == '__main__':
    main()
