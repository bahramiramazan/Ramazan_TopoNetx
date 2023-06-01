"""Simplex Class."""

from collections.abc import Hashable, Iterable
from itertools import combinations

__all__ = ["Combination"]


class Combination:
    """
    A class representing a combination in a simplicial complex.

    This class represents a combination in a simplicial complex, which is a set of nodes with a specific dimension. The
    combination is immutable, and the nodes in the combination must be hashable and unique.

    Parameters
    ----------
    elements: Iterable
        The nodes in the combination.
    name : str, optional
        A name for the combination.
    construct_tree : bool, default=True
        If True, construct the entire simplicial tree for the combination.
    attr : keyword arguments, optional
        Additional attributes to be associated with the combination.

    Examples
    --------

    """

    def __init__(self, elements, name=None, construct_tree=False, **attr):
        print('Combination init')
        if name is None:
            
            self.name = ""
        else:
            self.name = name
        self.construct_tree = construct_tree
        self.nodes = frozenset(elements)
        if len(self.nodes) != len(elements):
            raise ValueError("A simplex cannot contain duplicate nodes.")

        else:
            self._faces = frozenset()
        self.properties = dict()
        self.properties.update(attr)

    def __contains__(self, e):
        """Return True if the given element is a subset of the nodes."""
        if len(self.nodes) == 0:
            return False
        if isinstance(e, Iterable):
            if len(e) > len(self.nodes):
                return False
            else:
                if isinstance(e, frozenset):
                    return e <= self.nodes
                else:
                    return frozenset(e) <= self.nodes
        elif isinstance(e, Hashable):
            return frozenset({e}) <= self.nodes
        else:
            return False

    def sign(self, face):
        """Calculate the sign of the combination with respect to a given face.

        Parameters
        ----------
        face : combination
            A face of the combination.
        """
        raise NotImplementedError

    def __getitem__(self, item):
        """Get item.

        Get the value of the attribute associated with the combinataion.

        :param item: The name of the attribute.
        :type item: str
        :return: The value of the attribute.
        :raises KeyError: If the attribute is not found in the combination.
        """
        if item not in self.properties:
            raise KeyError(f"Attribute '{item}' is not found in the combination.")
        else:
            return self.properties[item]

    def __setitem__(self, key, item):
        """Set the value of an attribute associated with the combination.

        :param key: The name of the attribute.
        :type key: str
        :param item: The value of the attribute.
        """
        self.properties[key] = item

    def __len__(self):
        """Get the number of nodes in the combination.

        :return: The number of nodes in the combination.
        :rtype: int
        """
        return len(self.nodes)

    def __iter__(self):
        """Get an iterator over the nodes in the combination.

        :return: An iterator over the nodes in the combination.
        :rtype: iter
        """
        return iter(self.nodes)

    def __repr__(self):
        """Return string representation of the combination.

        :return: A string representation of the combination.
        :rtype: str
        """
        return f"Combination{tuple(self.nodes)}"

    def __str__(self):
        """Return string representation of the combination.

        :return: A string representation of the combination.
        :rtype: str
        """
        return f"Nodes set: {tuple(self.nodes)}, attrs: {self.properties}"
