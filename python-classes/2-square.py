#!/usr/bin/python3
"""
Bu modul Kvadrat (Square) sinfi üçün məlumatların doğrulanmasını
(validation) təmin edir.
"""


class Square:
    """
    Kvadratı təmsil edən sinif.

    Atributlar:
        __size (int): Kvadratın tərəfinin ölçüsü (private).
    """

    def __init__(self, size=0):
        """
        Yeni bir Kvadrat obyekti yaradır və daxil edilən ölçünü yoxlayır.

        Args:
            size (int): Kvadratın ölçüsü. Susmaya görə 0-dır.

        Raises:
            TypeError: Əgər size integer (tam ədəd) deyilsə.
            ValueError: Əgər size 0-dan kiçikdirsə.
        """
        # 1. Tip yoxlanışı: Integer olmalıdır
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        # 2. Dəyər yoxlanışı: Mənfi ola bilməz
        if size < 0:
            raise ValueError("size must be >= 0")
        
        # Yoxlamalardan keçərsə, dəyəri mənimsədirik
        self.__size = size
