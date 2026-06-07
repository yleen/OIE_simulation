"""
@file: main.py
@brief: Test cases of complete sequential addition & complete sequential multiplication
@author: li.zhong.yuan@outlook.com
@date: 2025/1/23
"""
from test.full_CSA_diagram.generate import test_full_CSA_generation
from test.sequence_operation.test_add import test_addition_valid_1
from test.sequence_operation.test_multi import test_multiplication_valid_1

if __name__ == '__main__':

    # 1. For OIE and Complete Sequence Addition and Complete Sequence Multiplication
    # test_addition_valid_1()
    # test_multiplication_valid_1()

    # 2. For Full CSA Diagram
    test_full_CSA_generation()
