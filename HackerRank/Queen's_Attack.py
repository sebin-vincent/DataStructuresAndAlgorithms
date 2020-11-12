#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    r_top_d = 0
    r
    for obstacle in obstacles:
        r_o, c_o = obstacle
        if (r_o > r_q):
            d_width = r_o - r_q
            d = c_o - c_q
            if (d == d_width):
                # right_diagonal
                continue
            elif (d == -d_width):
                # left_diagonal
                continue
            elif (d == 0):
                # vertically above
                continue
            else:
                continue
        elif (r_o < r_q):
            d_width = r_q - r_o
            d = c_o - c_q
            if (d == d_width):
                # right_diagonal
                continue
            elif (d == -d_width):
                # left_diagonal
                continue
            elif (d == 0):
                # vertically above
                continue
            else:
                continue
        else:
            if (c_o > c_q):
                # right side
                continue
            else:
                # leftside
                continue