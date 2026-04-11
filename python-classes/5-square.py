#!/usr/bin/python3
"""
Bu modul Kvadrat (Square) sinfinə vizual çap metodunu (my_print)
əlavə edir.
"""


class Square:
    """
    Kvadratı təmsil edən sinif.

    Atributlar:
        __size (int): Kvadratın tərəfinin ölçüsü (private).
    """

    def __init__(self, size=0):
        """
        Yeni bir Kvadrat obyekti yaradır.

        Args:
            size (int): Kvadratın ölçüsü. Susmaya görə 0-dır.
        """
        self.size = size

    @property
    def size(self):
        """
        Kvadratın ölçüsünü götürmək üçün Getter.

        Returns:
            int: Kvadratın ölçüsü.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Kvadratın ölçüsünü təyin etmək üçün Setter.

        Args:
            value (int): Yeni ölçü dəyəri.

        Raises:
            TypeError: Əgər value integer deyilsə.
            ValueError: Əgər value 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Kvadratın sahəsini hesablayır.

        Returns:
            int: Kvadratın sahəsi.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Kvadratı '#' simvolu ilə terminalda çap edir.
        Əgər size 0-dırsa, boş bir sətir çap edir.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
