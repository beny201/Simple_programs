from typing import List, Tuple, Set, Dict, Union, Any, Optional, Callable
from dataclasses import dataclass
# for _ in range(10):
# 	print('xyz')
@dataclass
class Point:
	x: int = 0
	y: int = 0
# Jezyk dynamicznie typowany i silnie typowany

# def multiply(factor, text):
# 	"""
# 	:type factor: int
# 	:type text: str
# 	:rtype: str
# 	"""
# 	return factor * text

def multiply(factor: int, text: str) -> str:
	x = {}
	return factor * text

print(multiply(5, 'xyz'))

q: str = 'Lorem ipsum'
q: int = 1_000_000 # -> 1000000
q: float = 0.5
q: bool = True


x: List = [1, 2, 3]
x: Tuple = (1, 2, 3)
x: Set = {1, 2, 3}
x: Dict = {'one': 1, 'two': 2}


x: List[int] = [1, 2, 3]
x: Tuple[int, int, int] = (1, 2, 3)
x: Tuple[int, ...] = (1, 2, 3, 4, 5)
x: Set[int] = {1, 2, 3}
x: Dict[str, int] = {'one': 1, 'two': 2}


l1: List[int] = [1, 2, 3]
l2: List[Union[int, str]] = [1, 2, 3, 'str', 'text', 5]
l3: List[Any] = [1, 2, 3, 'str', 'text', 5, True, 3.5, bool]

l4: List[Tuple[Any, Any]] = [('1', 'two'), (3, True), (3, 7.3)]
l4: List[Dict[str, int]] = [{'one': 1, 'two': 2}, {'one': 1, 'two': 2}]


# def multiply(a: int, b: int, c: Union[int, None] = None) -> int:
def multiply(a: int, b: int, c: Optional[int] = None) -> int:
	if c is not None:
		return a * b * c
	return a * b
	# return a * b * c if c else a * b


print(multiply(5, 5,6))

def do_something(): pass

fun: Callable = do_something

fun()


p: Point = Point()
