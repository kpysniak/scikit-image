"""
:author: Damian Eads, 2009
:license: modified BSD
"""

import numpy as np


def square(width, dtype=np.uint8):
    """
    Generates a flat, square-shaped structuring element. Every pixel
    along the perimeter has a chessboard distance no greater than radius
    (radius=floor(width/2)) pixels.

    Parameters
    ----------
    width : int
       The width and height of the square

    Other Parameters
    ----------------
    dtype : data-type
       The data type of the structuring element.

    Returns
    -------
    selem : ndarray
       A structuring element consisting only of ones, i.e. every
       pixel belongs to the neighborhood.

    """
    return np.ones((width, width), dtype=dtype)


def rectangle(width, height, dtype=np.uint8):
    """
    Generates a flat, rectangular-shaped structuring element of a
    given width and height. Every pixel in the rectangle belongs
    to the neighboorhood.

    Parameters
    ----------
    width : int
       The width of the rectangle

    height : int
       The height of the rectangle

    Other Parameters
    ----------------
    dtype : data-type
       The data type of the structuring element.

    Returns
    -------
    selem : ndarray
       A structuring element consisting only of ones, i.e. every
       pixel belongs to the neighborhood.

    """
    return np.ones((width, height), dtype=dtype)


def diamond(radius, dtype=np.uint8):
    """
    Generates a flat, diamond-shaped structuring element of a given
    radius.  A pixel is part of the neighborhood (i.e. labeled 1) if
    the city block/manhattan distance between it and the center of the
    neighborhood is no greater than radius.

    Parameters
    ----------
    radius : int
       The radius of the diamond-shaped structuring element.

    dtype : data-type
       The data type of the structuring element.

    Returns
    -------

    selem : ndarray
       The structuring element where elements of the neighborhood
       are 1 and 0 otherwise.
    """
    half = radius
    (I, J) = np.meshgrid(range(0, radius * 2 + 1), range(0, radius * 2 + 1))
    s = np.abs(I - half) + np.abs(J - half)
    return np.array(s <= radius, dtype=dtype)


def disk(radius, dtype=np.uint8):
    """
    Generates a flat, disk-shaped structuring element of a given radius.
    A pixel is within the neighborhood if the euclidean distance between
    it and the origin is no greater than radius.

    Parameters
    ----------
    radius : int
       The radius of the disk-shaped structuring element.

    dtype : data-type
       The data type of the structuring element.

    Returns
    -------
    selem : ndarray
       The structuring element where elements of the neighborhood
       are 1 and 0 otherwise.
    """
    L = np.linspace(-radius, radius, 2 * radius + 1)
    (X, Y) = np.meshgrid(L, L)
    s = X**2
    s += Y**2
    return np.array(s <= radius * radius, dtype=dtype)


def cube(width, dtype=np.uint8):
    """
    Generates a cube-shaped structuring element (the 3D equivalent of
    a square). Every pixel along the perimeter has a chessboard distance
    no greater than radius (radius=floor(width/2)) pixels.

    Parameters
    ----------
    width : int
       The width, height and depth of the cube

    Other Parameters
    ----------------
    dtype : data-type
       The data type of the structuring element.

    Returns
    -------
    selem : ndarray
       A structuring element consisting only of ones, i.e. every
       pixel belongs to the neighborhood.

    """
    return np.ones((width, width, width), dtype=dtype)


def octahedron(radius, dtype=np.uint8):
    """
    Generates a octahedron-shaped structuring element of a given radius
    (the 3D equivalent of a diamond).  A pixel is part of the
    neighborhood (i.e. labeled 1) if the city block/manhattan distance
    between it and the center of the neighborhood is no greater than
    radius.

    Parameters
    ----------
    radius : int
       The radius of the octahedron-shaped structuring element.

    dtype : data-type
       The data type of the structuring element.

    Returns
    -------

    selem : ndarray
       The structuring element where elements of the neighborhood
       are 1 and 0 otherwise.
    """
    # note that in contrast to diamond(), this method allows non-integer radii
    n = 2 * radius + 1
    Z, Y, X = np.mgrid[ -radius:radius:n*1j, 
                        -radius:radius:n*1j,
                        -radius:radius:n*1j]
    s = np.abs(X) + np.abs(Y) + np.abs(Z) 
    return np.array(s <= radius, dtype=dtype)


def ball(radius, dtype=np.uint8):
    """
    Generates a ball-shaped structuring element of a given radius (the
    3D equivalent of a disk). A pixel is within the neighborhood if the
    euclidean distance between it and the origin is no greater than
    radius.

    Parameters
    ----------
    radius : int
       The radius of the ball-shaped structuring element.

    dtype : data-type
       The data type of the structuring element.

    Returns
    -------
    selem : ndarray
       The structuring element where elements of the neighborhood
       are 1 and 0 otherwise.
    """
    n = 2 * radius + 1
    Z, Y, X = np.mgrid[ -radius:radius:n*1j, 
                        -radius:radius:n*1j, 
                        -radius:radius:n*1j]
    s = X**2 + Y**2 + Z**2
    return np.array(s <= radius * radius, dtype=dtype)
