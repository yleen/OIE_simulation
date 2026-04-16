"""
@file: main.py
@brief: Test cases of complete sequential addition & complete sequential multiplication
@author: li.zhong.yuan@outlook.com
@date: 2025/1/23
"""

from test.sequential_operation.test_add import test_addition_valid_1
from test.sequential_operation.test_multi import test_multiplication_valid_1
from LiZhongYuan_diagram.cayley_table.main import run as run_cayley_table

if __name__ == '__main__':

    test_addition_valid_1()

    test_multiplication_valid_1()

    run_cayley_table()
