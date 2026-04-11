#!/usr/bin/python3
"""
Bu modul Kvadrat (Square) sinfinə koordinat (position) məntiqini
əlavə edir.
"""


class Square:
    """
    Kvadratı təmsil edən sinif.

    Atributlar:
        __size (int): Kvadratın ölçüsü.
        __position (tuple): Kvadratın koordinatları.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Yeni bir Kvadrat obyekti yaradır.

        Args:
            size (int): Kvadratın ölçüsü.
            position (tuple): Kvadratın koordinatları.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Kvadratın ölçüsünü götürmək üçün Getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Kvadratın ölçüsünü təyin etmək üçün Setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Kvadratın koordinatlarını götürmək üçün Getter."""
        return self.__position

    @position.setter
    def position(self, value):
        """Kvadratın koordinatlarını təyin etmək üçün Setter."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Kvadratın sahəsini hesablayır."""
        return (self.__size * self.__size)

    def my_print(self):
        """
        Kvadratı '#' simvolu və 'position' nəzərə alınmaqla çap edir.
        """
        if self.__size == 0:
            print("")
            return

        # Yuxarıdan boşluq (position[1])
        for _ in range(self.__position[1]):
            print("")

        # Kvadratın çapı
        for _ in range(self.__size):
            # Soldan boşluq (position[0]) + kvadratın tərəfi
            print(" " * self.__position[0] + "#" * self.__size)
