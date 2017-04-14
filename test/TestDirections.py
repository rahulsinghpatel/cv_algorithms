#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
from numpy.testing import assert_approx_equal, assert_allclose, assert_array_equal
from nose.tools import assert_equal, assert_true, assert_false, assert_greater, assert_less
import cv2
import cv_algorithms
import numpy as np

class TestDirections(object):
    def test_binary_directions_simple(self):
        """Test binary direction detection"""
        img = np.zeros((10,8), dtype=np.uint8)
        y, x = 5, 4
        img[5,4] = 255
        # Currently just test whether it crashes
        directions = cv_algorithms.binary_directions(img)
        print(directions)
        assert_equal(0, directions[0,0])
        # Center
        assert_equal(0, directions[5, 4])
        # NW
        assert_equal((1 << 0), directions[y-1, x-1])
        # N
        assert_equal((1 << 1), directions[y-1, x])
        # NE
        assert_equal((1 << 2), directions[y-1, x+1])
        # W
        assert_equal((1 << 3), directions[y, x-1])
        # E
        assert_equal((1 << 4), directions[y, x+1])
        # SW
        assert_equal((1 << 5), directions[y+1, x-1])
        # S
        assert_equal((1 << 6), directions[y+1, x])
        # SE
        assert_equal((1 << 7), directions[y+1, x+1])

    def test_binary_directions_corner(self):
        # Just test if it crashes for something in the corners
        img = np.zeros((10,8), dtype=np.uint8)
        img[9,7] = 255
        img[0,0] = 255
        cv_algorithms.binary_directions(img)