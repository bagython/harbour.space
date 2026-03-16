"""Lecture 01 practice problems.

Implement each function below so tests pass.
Rules:
- Do not change function names/signatures.
- Keep implementations pure unless the function explicitly needs I/O.
- Use only the Python standard library.
"""

from __future__ import annotations


def normalize_username(name: str) -> str:
    """Return a normalized username.

    Rules:
    - Trim outer whitespace
    - Lowercase everything
    - Replace internal whitespace runs with a single underscore
    """

    return "_".join(name.split()).lower()


def is_valid_age(age: int) -> bool:
    """Return True if age is in [18, 120], otherwise False."""

    # if 18 <= age <= 120:
    #     return True
    # else:
    #     return False
    return 18 <= age <= 120


def truthy_values(values: list[object]) -> list[object]:
    """Return a new list containing only truthy values from input."""

    return [ob for ob in values if bool(ob)]


def sum_until_negative(numbers: list[int]) -> int:
    """Return sum of numbers until the first negative value (exclusive)."""

    total = 0

    for i in numbers:
        if i < 0:
            break
        else:
            total += i

    return total


def skip_multiples_of_three(numbers: list[int]) -> list[int]:
    """Return numbers excluding values divisible by 3."""

    return [i for i in numbers if (i % 3 != 0)]


def first_even_or_none(numbers: list[int]) -> int | None:
    """Return the first even number, or None if no even number exists."""

    for i in numbers:
        if i % 2 == 0:
            return i
    else:
        return None


def squares_of_even(numbers: list[int]) -> list[int]:
    """Return squares of all even numbers in input order."""

    return [(i**2) for i in numbers if i % 2 == 0]


def word_lengths(words: list[str]) -> dict[str, int]:
    """Return dict mapping each word to its length."""

    return {ob: len(ob) for ob in words}


def zip_to_pairs(keys: list[str], values: list[int]) -> list[tuple[str, int]]:
    """Zip keys and values into list of pairs. Ignore extras in longer list."""

    return list(zip((keys), values))


def build_user(
    name: str, role: str = "student", active: bool = True
) -> dict[str, object]:
    """Build and return {'name': name, 'role': role, 'active': active}."""

    # lol
    return {"name": name, "role": role, "active": active}


def append_tag_safe(tag: str, tags: list[str] | None = None) -> list[str]:
    """Append tag to tags safely (no shared mutable default across calls)."""

    # if tags:
    #     # return tags + [tag]
    #     tags.append(tag)
    #     return tags
    # else:
    #     return [tag]  # ehhhhhh?

    if tags is None:
        tags = []
    tags.append(tag)
    return tags


def invert_dict(mapping: dict[str, int]) -> dict[int, str]:
    """Invert mapping. Assume values are unique."""

    return {v: k for k, v in mapping.items()}


def unique_sorted_tags(tags: list[str]) -> list[str]:
    """Return unique tags sorted ascending."""

    return sorted(set(tags))


def count_words(words: list[str]) -> dict[str, int]:
    """Count occurrences of each word using collections.Counter."""

    from collections import Counter

    return dict(Counter(words))


def group_scores(records: list[tuple[str, int]]) -> dict[str, list[int]]:
    """Group scores by student name using collections.defaultdict(list)."""

    from collections import defaultdict

    grouper = defaultdict(list)
    for r in records:
        grouper[r[0]].append(r[1])
    return grouper


def rotate_queue(items: list[str], steps: int) -> list[str]:
    """Rotate queue to the right by `steps` using collections.deque and return as list."""

    from collections import deque

    dems = deque(items)
    dems.rotate(steps)
    return list(dems)


def safe_int(value: str) -> int | None:
    """Convert string to int, returning None if conversion fails."""

    try:
        return int(value)
    except ValueError:
        return None


def read_lines(path: str) -> list[str]:
    """Read a text file with a context manager and return non-empty stripped lines."""

    with open(path, "r") as f:
        # does strip() twice kinda cringe
        return [line.strip() for line in f if line.strip() != ""]


def top_n_scores(scores: list[int], n: int = 3) -> list[int]:
    """Return top `n` scores in descending order."""

    scores.sort(reverse=True)
    return scores[:n]


def all_passed(scores: list[int], threshold: int = 50) -> bool:
    """Return True if every score is >= threshold."""

    # for i in scores:
    #     if i < threshold:
    #         return False
    # else:
    #     return True

    return all(i >= 50 for i in scores)
