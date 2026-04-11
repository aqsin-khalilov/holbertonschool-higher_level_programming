#!/usr/bin/python3
"""
Bu modul Kvadrat (Square) sinfinə sahə hesablama metodu əlavə edir.
"""


class Square:
    """
    Kvadratı təmsil edən sinif.

    Atributlar:
        __size (int): Kvadratın tərəfinin ölçüsü (private).
    """

    def __init__(self, size=0):
        """
        Yeni bir Kvadrat obyekti yaradır və ölçünü yoxlayır.

        Args:
            size (int): Kvadratın ölçüsü. Susmaya görə 0-dır.

        Raises:
            TypeError: Əgər size integer (tam ədəd) deyilsə.
            ValueError: Əgər size 0-dan kiçikdirsə.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Kvadratın cari sahəsini hesablayır və qaytarır.

        Returns:
            int: Kvadratın sahəsi (size * size).
        """
        return (self.__size * self.__size)
