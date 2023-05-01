from typing import List, Union, Optional


def calc(a: Optional[int], b: Optional[int]) -> Union[int, float]:
    return a + b


def to_int(a_list: List[str]) -> List[int]:
    return [int(e) for e in a_list]


if __name__ == '__main__':
    print('hi')
