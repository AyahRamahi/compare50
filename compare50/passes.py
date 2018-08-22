from pkg_resources import resource_filename

from . import comparators, preprocessors
from ._data import Pass

__all__ = ["winnowing", "winnowing_exact", "misspellings"]


class structure(Pass):
    """Compares code structure by removing all whitespace, normalizing all comments, variable names, and string literals, and running the winnowing algorithm."""

    preprocessors = [preprocessors.strip_whitespace,
                     preprocessors.strip_comments,
                     preprocessors.normalize_identifiers,
                     preprocessors.normalize_string_literals,
                     preprocessors.normalize_numeric_literals]
    comparator = comparators.Winnowing(k=25, t=35)


class exact(Pass):
    """Removes all whitespace, then uses the winnowing algorithm to compare submissions."""
    preprocessors = [preprocessors.strip_whitespace,
                     preprocessors.split_on_whitespace]
    comparator = comparators.Winnowing(k=25, t=35)


class misspellings(Pass):
    """Compares comments for identically misspelled English words."""

    preprocessors = [preprocessors.comments,
                     preprocessors.normalize_case,
                     preprocessors.words]
    comparator = comparators.Misspellings(resource_filename("compare50.comparators",
                                                            "english_dictionary.txt"))
