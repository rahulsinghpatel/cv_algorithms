#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
from numpy.testing import assert_approx_equal, assert_allclose, assert_array_equal
from nose.tools import assert_equal, assert_true, assert_false, assert_greater, assert_less
import cv2
import cv_algorithms
import numpy as np

class TestNeighbours(object):
    def test_binary_neighbours_simple(self):
        """Test binary direction detection"""
        img = np.zeros((10,8), dtype=np.uint8)
        y, x = 5, 4
        img[5,4] = 255
        # Currently just test whether it crashes
        directions = cv_algorithms.binary_neighbours(img)
        print(directions)
        assert_equal(0, directions[0,0])
        # NOTE: Directions are inversed, this is not a mistake
        # To the pixel on the NW of the white pixel
        #  the white pixel is SE!
        # Center
        assert_equal(0, directions[5, 4])
        # NW of the white pixel
        assert_equal((y-1, x-1), cv_algorithms.NeighbourCheck.northwest_coords(y, x))
        assert_equal((1 << 7), directions[y-1, x-1])
        assert_false(cv_algorithms.NeighbourCheck.is_northwest(directions[y-1, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_north(directions[y-1, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_northeast(directions[y-1, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_west(directions[y-1, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_east(directions[y-1, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_southwest(directions[y-1, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_south(directions[y-1, x-1]))
        assert_true(cv_algorithms.NeighbourCheck.is_southeast(directions[y-1, x-1]))
        # N of the white pixel
        assert_equal((y-1, x), cv_algorithms.NeighbourCheck.north_coords(y, x))
        assert_equal((1 << 6), directions[y-1, x])
        assert_false(cv_algorithms.NeighbourCheck.is_northwest(directions[y-1, x]))
        assert_false(cv_algorithms.NeighbourCheck.is_north(directions[y-1, x]))
        assert_false(cv_algorithms.NeighbourCheck.is_northeast(directions[y-1, x]))
        assert_false(cv_algorithms.NeighbourCheck.is_west(directions[y-1, x]))
        assert_false(cv_algorithms.NeighbourCheck.is_east(directions[y-1, x]))
        assert_false(cv_algorithms.NeighbourCheck.is_southwest(directions[y-1, x]))
        assert_true(cv_algorithms.NeighbourCheck.is_south(directions[y-1, x]))
        assert_false(cv_algorithms.NeighbourCheck.is_southeast(directions[y-1, x]))
        # NE of the white pixel
        assert_equal((y-1, x+1), cv_algorithms.NeighbourCheck.northeast_coords(y, x))
        assert_equal((1 << 5), directions[y-1, x+1])
        assert_false(cv_algorithms.NeighbourCheck.is_northwest(directions[y-1, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_north(directions[y-1, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_northeast(directions[y-1, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_west(directions[y-1, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_east(directions[y-1, x+1]))
        assert_true(cv_algorithms.NeighbourCheck.is_southwest(directions[y-1, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_south(directions[y-1, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_southeast(directions[y-1, x+1]))
        # W of the white pixel
        assert_equal((y, x-1), cv_algorithms.NeighbourCheck.west_coords(y, x))
        assert_equal((1 << 4), directions[y, x-1])
        assert_false(cv_algorithms.NeighbourCheck.is_northwest(directions[y, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_north(directions[y, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_northeast(directions[y, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_west(directions[y, x-1]))
        assert_true(cv_algorithms.NeighbourCheck.is_east(directions[y, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_southwest(directions[y, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_south(directions[y, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_southeast(directions[y, x-1]))
        # E of the white pixel
        assert_equal((y, x+1), cv_algorithms.NeighbourCheck.east_coords(y, x))
        assert_equal((1 << 3), directions[y, x+1])
        assert_false(cv_algorithms.NeighbourCheck.is_northwest(directions[y, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_north(directions[y, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_northeast(directions[y, x+1]))
        assert_true(cv_algorithms.NeighbourCheck.is_west(directions[y, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_east(directions[y, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_southwest(directions[y, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_south(directions[y, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_southeast(directions[y, x+1]))
        # SW of the white pixel
        assert_equal((y+1, x-1), cv_algorithms.NeighbourCheck.southwest_coords(y, x))
        assert_equal((1 << 2), directions[y+1, x-1])
        assert_false(cv_algorithms.NeighbourCheck.is_northwest(directions[y+1, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_north(directions[y+1, x-1]))
        assert_true(cv_algorithms.NeighbourCheck.is_northeast(directions[y+1, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_west(directions[y+1, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_east(directions[y+1, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_southwest(directions[y+1, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_south(directions[y+1, x-1]))
        assert_false(cv_algorithms.NeighbourCheck.is_southeast(directions[y+1, x-1]))
        # S of the white pixel
        assert_equal((y+1, x), cv_algorithms.NeighbourCheck.south_coords(y, x))
        assert_equal((1 << 1), directions[y+1, x])
        assert_false(cv_algorithms.NeighbourCheck.is_northwest(directions[y+1, x]))
        assert_true(cv_algorithms.NeighbourCheck.is_north(directions[y+1, x]))
        assert_false(cv_algorithms.NeighbourCheck.is_northeast(directions[y+1, x]))
        assert_false(cv_algorithms.NeighbourCheck.is_west(directions[y+1, x]))
        assert_false(cv_algorithms.NeighbourCheck.is_east(directions[y+1, x]))
        assert_false(cv_algorithms.NeighbourCheck.is_southwest(directions[y+1, x]))
        assert_false(cv_algorithms.NeighbourCheck.is_south(directions[y+1, x]))
        assert_false(cv_algorithms.NeighbourCheck.is_southeast(directions[y+1, x]))
        # SE of the white pixel
        assert_equal((y+1, x+1), cv_algorithms.NeighbourCheck.southeast_coords(y, x))
        assert_equal((1 << 0), directions[y+1, x+1])
        assert_true(cv_algorithms.NeighbourCheck.is_northwest(directions[y+1, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_north(directions[y+1, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_northeast(directions[y+1, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_west(directions[y+1, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_east(directions[y+1, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_southwest(directions[y+1, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_south(directions[y+1, x+1]))
        assert_false(cv_algorithms.NeighbourCheck.is_southeast(directions[y+1, x+1]))

    def test_binary_neighbours_corner(self):
        # Just test if it crashes for something in the corners
        img = np.zeros((10,8), dtype=np.uint8)
        img[9,7] = 255
        img[0,0] = 255
        cv_algorithms.binary_neighbours(img)