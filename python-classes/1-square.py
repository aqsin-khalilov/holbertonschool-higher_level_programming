#!/usr/bin/python3
"""
Bu modul bir Kvadrat (Square) sinfi təyin edir.
Bu mərhələdə private atribut anlayışını öyrənirik.
"""


class Square:
    """
    Kvadratı təmsil edən sinif.

    Atributlar:
        __size (int): Kvadratın bir tərəfinin ölçüsü (private).
    """

    def __init__(self, size):
        """
        Yeni bir Kvadrat obyekti yaradır.

        Args:
            size (int): Kvadratın ölçüsü.
        """
        self.__size = size
