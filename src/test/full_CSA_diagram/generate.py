from typing import List
import matplotlib as mpl
import matplotlib.pyplot as plt
from pandas import DataFrame

from fullCsaDiagram.diagram_generator import gen_binomial_theorem_collection, gen_all_combos, init_data_frame, \
    build_data_frame, render_plot


def run() -> None:
    """
    Entry point for generating and saving the Cayley table diagram.
    """

    elements2 = '12'
    elements3 = '123'
    elements4 = '1234'
    elements5 = '12345'
    elements6 = '123456'
    elements7 = '1234567'
    elements8 = '12345678'
    elements9 = '123456789'

    zero_elem_mark = '0'
    err_elem_mark = 'E'

    # # 2 OIEs
    # dpi: int = 200
    # contain_zero = False
    # font_size: float = 5
    # no_tick_marks: bool = False
    # binomial_theorem_collection: List[List[str]] \
    #     = gen_binomial_theorem_collection(p_elements=elements2,
    #                                       p_contain_zero=contain_zero,
    #                                       p_zero_elem_mark=zero_elem_mark,
    #                                       p_err_elem_mark=err_elem_mark)

    # # 5 OIEs
    dpi: int = 500
    contain_zero = False
    font_size: float = 4
    no_tick_marks: bool = False
    binomial_theorem_collection: List[List[str]] \
        = gen_binomial_theorem_collection(p_elements=elements5,
                                          p_contain_zero=contain_zero,
                                          p_zero_elem_mark=zero_elem_mark,
                                          p_err_elem_mark=err_elem_mark)

    # 6 OIEs
    # dpi: int = 1000
    # contain_zero = True
    # font_size: float = 4
    # no_tick_marks: bool = False
    # binomial_theorem_collection: List[List[str]] \
    #     = gen_binomial_theorem_collection(p_elements=elements6,
    #                                       p_contain_zero=contain_zero,
    #                                       p_zero_elem_mark=zero_elem_mark,
    #                                       p_err_elem_mark=err_elem_mark)

    # # 7 OIEs
    # dpi: int = 2000
    # contain_zero = False
    # font_size: float = 0.7
    # no_tick_marks: bool = True
    # binomial_theorem_collection: List[List[str]] \
    #     = gen_binomial_theorem_collection(p_elements=elements7,
    #                                       p_contain_zero=contain_zero,
    #                                       p_zero_elem_mark=zero_elem_mark,
    #                                       p_err_elem_mark=err_elem_mark)

    # # 8 OIEs
    # dpi: int = 3000
    # contain_zero = True
    # font_size: float = 0.45
    # no_tick_marks: bool = True
    # binomial_theorem_collection: List[List[str]] \
    #     = gen_binomial_theorem_collection(p_elements=elements8,
    #                                       p_contain_zero=contain_zero,
    #                                       p_zero_elem_mark=zero_elem_mark,
    #                                       p_err_elem_mark=err_elem_mark)

    # 9 OIEs
    # dpi: int = 3000
    # contain_zero = True
    # font_size: float = 0.45
    # no_tick_marks: bool = True
    # binomial_theorem_collection: List[List[str]] \
    #     = gen_binomial_theorem_collection(p_elements=elements9,
    #                                       p_contain_zero=contain_zero,
    #                                       p_zero_elem_mark=zero_elem_mark,
    #                                       p_err_elem_mark=err_elem_mark)

    headers: List[str] = gen_all_combos(binomial_theorem_collection)

    data_frame: DataFrame = init_data_frame(p_table_headers=headers)

    build_data_frame(p_data_frame=data_frame,
                     p_zero_elem=zero_elem_mark,
                     p_err_elem=err_elem_mark)

    render_plot(p_data_frame=data_frame,
                p_mpl=mpl,
                p_dpi=dpi,
                p_font_size=font_size,
                p_no_tick_marks=no_tick_marks,
                p_err_elem='E')

    plt.savefig('../pics/test_pic.png')