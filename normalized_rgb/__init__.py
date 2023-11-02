def rgb(red: int, green: int, blue: int) -> tuple[float, float, float]:
    """
    Converts RGB values to a normalized values between 0 and 1.
    :param red: 0 - 255
    :param green: 0 - 255
    :param blue: 0 - 255
    :return: tuple (red, green, blue) (normalized)
    """
    valid = [
        isinstance(red, int) or isinstance(red, float),
        isinstance(green, int) or isinstance(green, float),
        isinstance(blue, int) or isinstance(blue, float),
    ]

    if not all(valid):
        raise TypeError("RGB values but be either types int or float.")

    return _normalize_integer(red), _normalize_integer(green), _normalize_integer(blue)


def rgba(red: int, green: int, blue: int, alpha: int) -> tuple[float, float, float, float]:
    """
    Convert RGBA values to a normalized values between 0 and 1.
    :param red: 0 - 255
    :param green: 0 - 255
    :param blue: 0 - 255
    :param alpha: 0 - 255
    :return: tuple (red, green, blue, alpha) (normalized
    """
    valid = [
        isinstance(red, int) or isinstance(red, float),
        isinstance(green, int) or isinstance(green, float),
        isinstance(blue, int) or isinstance(blue, float),
        isinstance(alpha, int) or isinstance(alpha, float),
    ]

    if not all(valid):
        raise TypeError("RGBA values but be either types int or float.")

    r, g, b = rgb(red, green, blue)
    a = _normalize_integer(alpha)
    return r, g, b, a


def _normalize_integer(integer: int) -> float:
    minimum = 0
    maximum = 255

    if not isinstance(integer, int) and not isinstance(integer, float):
        raise TypeError("Integer must be either types int or float")

    return (integer - min(integer, minimum)) / (max(integer, maximum) - min(integer, minimum))  # Normalizes into 0 - 1
