from typing import List

def clean_recup() -> List[int]:
    text_list = [line.rstrip('\n') for line in open('data/day1.txt')]
    return list(map(int, text_list))

def get_simple_nb_increased() -> int:
    results = clean_recup()
    return sum(a < b for a, b in zip(results, results[1:]))

def get_group_nb_increased() -> int:
    results = clean_recup()
    return sum(a < b for a, b in zip(results, results[3:]))

if __name__ == "__main__":
    print(get_simple_nb_increased())
    print(get_group_nb_increased())
