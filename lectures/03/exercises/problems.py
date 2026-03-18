"""Lecture 03 practice problems.

Implement each class/function below so tests pass.
Rules:
- Do not change names/signatures.
- Use only the Python standard library.

Problems:
1. Countdown iterator
2. Step iterator
3. Unique consecutive iterator
4. Circular iterator
6. File word reader generator
7. Batch generator
8. Recursive flatten generator (optional)
9. log_calls decorator
10. measure_time decorator
11. count_calls decorator
12. ensure_non_negative decorator
13. retry decorator (optional)
14. lru_cache decorator (optional)
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import Any


class Countdown:
    """Problem 1. Countdown iterator.

    Build an iterator class that starts at `n` and yields down to `0` inclusive.

    Example:
    >>> list(Countdown(3))
    [3, 2, 1, 0]
    """

    def __init__(self, n: int) -> None:
        self.current = n

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


class StepIterator:
    """Problem 2. Step iterator.

    Iterate through a list by taking every `step`-th element.
    Default `step` is `2`.
    Raise `ValueError` when `step <= 0`.

    Example:
    >>> list(StepIterator([10, 20, 30, 40, 50, 60]))
    [10, 30, 50]
    >>> list(StepIterator([1, 2, 3, 4, 5, 6, 7], step=3))
    [1, 4, 7]
    """

    def __init__(self, values: list[Any], step: int = 2) -> None:
        self.values = values
        if step <= 0:
            raise ValueError
        else:
            self.step = step
        self.index = 0

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        try:
            value = self.values[self.index]
        except IndexError:
            raise StopIteration
        self.index += self.step
        return value


class UniqueConsecutiveIterator:
    """Problem 3. Unique consecutive iterator.

    Yield values while removing only *consecutive* duplicates.

    Example:
    >>> list(UniqueConsecutiveIterator([1, 1, 2, 2, 2, 3, 1, 1]))
    [1, 2, 3, 1]
    """

    def __init__(self, values: list[Any]) -> None:
        prev = object()
        self.values = [prev := v for v in values if prev != v]

        self.index = 0

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:

        try:
            return self.values[self.index]
        except IndexError:
            raise StopIteration
        finally:
            # apparently finally always gets called before the return
            self.index += 1


class CircularIterator:
    """Problem 4. Circular iterator.

    Return exactly `k` values by cycling through `sequence`.
    Raise `ValueError` when sequence is empty or when `k < 0`.

    Example:
    >>> list(CircularIterator(["A", "B", "C"], 8))
    ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B']
    """

    def __init__(self, sequence: Sequence[Any], k: int) -> None:
        if sequence and k >= 0:
            self.sequence = sequence
            self.k = k
        else:
            raise ValueError
        self.index = 0

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        if self.k <= 0:
            raise StopIteration
        try:
            value = self.sequence[self.index]
        except IndexError:
            self.index = 0
            value = self.sequence[0]

        self.index += 1
        self.k -= 1
        return value


class FlattenIterator:
    """Problem 5 (optional). Flatten iterator.

    Build an iterator class that yields scalar values from nested lists
    of arbitrary depth.

    Example:
    >>> list(FlattenIterator([1, [2, 3], [4, [5, 6]], 7]))
    [1, 2, 3, 4, 5, 6, 7]
    """

    def __init__(self, data: list[Any]) -> None:
        raise NotImplementedError

    def __iter__(self) -> Iterator[Any]:
        raise NotImplementedError

    def __next__(self) -> Any:
        raise NotImplementedError


def read_words(filename: str) -> Iterator[str]:
    """Problem 6. File word reader generator.

    Yield one word at a time from a text file without loading the whole
    file into memory.

    Example:
    >>> list(read_words("sample.txt"))
    ['one', 'two', 'three']
    """
    with open(filename, "r") as f:
        for line in f:
            yield from line.split()


def batch(iterable: Iterable[Any], size: int) -> Iterator[list[Any]]:
    """Problem 7. Batch generator.

    Yield lists containing at most `size` items from `iterable`.
    Raise `ValueError` when `size <= 0`.

    Example:
    >>> list(batch([1, 2, 3, 4, 5, 6, 7], 3))
    [[1, 2, 3], [4, 5, 6], [7]]
    """

    if size <= 0:
        raise ValueError
    iterator = iter(iterable)

    # implementation stolen from python docs frfr
    def _islice_simplified(iterable: Iterable[Any], stop: int) -> Iterable[Any]:
        next_i = 0

        for i, element in zip(range(max(0, stop)), iterable):
            if i == next_i:
                yield element
                next_i += 1

    while batch := list(_islice_simplified(iterator, size)):
        yield batch


def flatten(data: list[Any]) -> Iterator[Any]:
    """Problem 8 (optional). Recursive flatten generator.

    Recursively yield all scalar values from a nested list.

    Example:
    >>> list(flatten([1, [2, 3], [4, [5, 6]], 7]))
    [1, 2, 3, 4, 5, 6, 7]
    """
    for a in data:
        if type(a) is list:
            yield from flatten(a)
        else:
            yield a


def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 9. `log_calls` decorator.

    Print each function call in this format:
    `name(arg1, arg2, kw=value) -> result`

    Hint:
    - Function name: `func.__name__`
    - Positional values: `args`
    - Keyword names/values: `kwargs.items()`

    Example:
    >>> @log_calls
    ... def add(a, b):
    ...     return a + b
    >>> add(2, 3)
    add(2, 3) -> 5
    5
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        youter = func(*args, **kwargs)

        arguers = (*(str(b) for b in args), *(f"{k}={v}" for k, v in kwargs.items()))
        # blegh no lazy evaulation
        print(f"{func.__name__}({', '.join(arguers)}) -> {youter}")

        return youter

    return wrapper


def measure_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 10. `measure_time` decorator.

    Measure function execution time and print:
    `Executed in <milliseconds> ms`

    Example:
    >>> @measure_time
    ... def work():
    ...     return "done"
    >>> work()
    done
    """
    from time import perf_counter_ns

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = perf_counter_ns()
        result = func(*args, **kwargs)
        elapsed = perf_counter_ns() - start
        print(f"Executed in {elapsed / 1000000} ms")
        return result

    return wrapper


def count_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 11. `count_calls` decorator.

    Count how many times the wrapped function is called.
    Store the counter in `wrapper.calls`.

    Example:
    >>> @count_calls
    ... def ping():
    ...     return "ok"
    >>> ping(); ping()
    'ok'
    >>> ping.calls
    2
    """
    raise NotImplementedError


def ensure_non_negative(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 12. `ensure_non_negative` decorator.

    Raise `ValueError` when the decorated function returns a negative number.

    Example:
    >>> @ensure_non_negative
    ... def diff(a, b):
    ...     return a - b
    >>> diff(5, 2)
    3
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)

        # because it doesn't specify that it actually has to be a number
        # only that it's invalid if it is a number and negative lol
        if isinstance(result, (int, float)) and result < 0:
            raise ValueError
        else:
            return result

    return wrapper


def retry(times: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Problem 13 (optional). `retry(times)` decorator.

    Retry a function up to `times` retries after the initial attempt.
    Raise `ValueError` when `times < 0`.

    Example:
    >>> @retry(2)
    ... def flaky():
    ...     ...
    """
    raise NotImplementedError


def lru_cache(maxsize: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Problem 14 (optional). `lru_cache(maxsize)` decorator factory.

    Implement cache with Least Recently Used eviction policy.
    Keep only the last `maxsize` used results.
    Solve this one using a class.

    Example:
    >>> @lru_cache(2)
    ... def square(x):
    ...     return x * x
    >>> square(2), square(3), square(2)
    (4, 9, 4)
    """
    raise NotImplementedError
