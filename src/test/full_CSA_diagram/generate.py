from typing import List
import matplotlib as mpl
import matplotlib.pyplot as plt
from pandas import DataFrame

from fullCsaDiagram.diagram_generator import gen_binomial_theorem_collection, gen_all_combos, init_data_frame, \
    build_data_frame, render_plot

def test_2d_generation(p_file_path: str, p_zero_elem: str) -> None:
    elements = '12'
    dpi: int = 200
    font_size: float = 5
    no_tick_marks: bool = False
    binomial_theorem_collection: List[List[str]] \
        = gen_binomial_theorem_collection(p_elements=elements,
                                          p_zero_elem_mark=p_zero_elem,
                                          )

    headers: List[str] = gen_all_combos(binomial_theorem_collection)
    data_frame: DataFrame = init_data_frame(p_table_headers=headers)
    build_data_frame(p_data_frame=data_frame,
                     p_zero_elem=p_zero_elem)
    render_plot(p_data_frame=data_frame,
                p_mpl=mpl,
                p_dpi=dpi,
                p_font_size=font_size,
                p_no_tick_marks=no_tick_marks,
                p_zero_elem=p_zero_elem)
    plt.savefig(p_file_path)


def test_5d_generation(p_file_path: str, p_zero_elem: str)-> None:
    elements = '12345'
    dpi: int = 500
    font_size: float = 4
    no_tick_marks: bool = False
    binomial_theorem_collection: List[List[str]] \
        = gen_binomial_theorem_collection(p_elements=elements,
                                          p_zero_elem_mark=p_zero_elem)

    headers: List[str] = gen_all_combos(binomial_theorem_collection)
    data_frame: DataFrame = init_data_frame(p_table_headers=headers)
    build_data_frame(p_data_frame=data_frame,
                     p_zero_elem=p_zero_elem)
    render_plot(p_data_frame=data_frame,
                p_mpl=mpl,
                p_dpi=dpi,
                p_font_size=font_size,
                p_no_tick_marks=no_tick_marks,
                p_zero_elem=p_zero_elem)
    plt.savefig(p_file_path)


def test_6d_generation(p_file_path: str, p_zero_elem: str)-> None:
    elements = '123456'
    dpi: int = 1000
    font_size: float = 4
    no_tick_marks: bool = False
    binomial_theorem_collection: List[List[str]] \
        = gen_binomial_theorem_collection(p_elements=elements,
                                          p_zero_elem_mark=p_zero_elem)
    headers: List[str] = gen_all_combos(binomial_theorem_collection)
    data_frame: DataFrame = init_data_frame(p_table_headers=headers)
    build_data_frame(p_data_frame=data_frame,
                     p_zero_elem=p_zero_elem)
    render_plot(p_data_frame=data_frame,
                p_mpl=mpl,
                p_dpi=dpi,
                p_font_size=font_size,
                p_no_tick_marks=no_tick_marks,
                p_zero_elem=p_zero_elem)
    plt.savefig(p_file_path)


def test_7d_generation(p_file_path: str, p_zero_elem: str)-> None:
    elements = '1234567'
    dpi: int = 2000
    font_size: float = 0.7
    no_tick_marks: bool = True
    binomial_theorem_collection: List[List[str]] \
        = gen_binomial_theorem_collection(p_elements=elements,
                                          p_zero_elem_mark=p_zero_elem)
    headers: List[str] = gen_all_combos(binomial_theorem_collection)
    data_frame: DataFrame = init_data_frame(p_table_headers=headers)
    build_data_frame(p_data_frame=data_frame,
                     p_zero_elem=p_zero_elem)
    render_plot(p_data_frame=data_frame,
                p_mpl=mpl,
                p_dpi=dpi,
                p_font_size=font_size,
                p_no_tick_marks=no_tick_marks,
                p_zero_elem=p_zero_elem)
    plt.savefig(p_file_path)


def test_8d_generation(p_file_path: str, p_zero_elem: str)-> None:
    elements = '12345678'
    dpi: int = 3000
    font_size: float = 0.45
    no_tick_marks: bool = True
    binomial_theorem_collection: List[List[str]] \
        = gen_binomial_theorem_collection(p_elements=elements,
                                          p_zero_elem_mark=p_zero_elem)
    headers: List[str] = gen_all_combos(binomial_theorem_collection)
    data_frame: DataFrame = init_data_frame(p_table_headers=headers)
    build_data_frame(p_data_frame=data_frame,
                     p_zero_elem=p_zero_elem)
    render_plot(p_data_frame=data_frame,
                p_mpl=mpl,
                p_dpi=dpi,
                p_font_size=font_size,
                p_no_tick_marks=no_tick_marks,
                p_zero_elem=p_zero_elem)
    plt.savefig(p_file_path)


def test_9d_generation(p_file_path: str, p_zero_elem: str)-> None:
    elements = '123456789'
    dpi: int = 3000
    font_size: float = 0.45
    no_tick_marks: bool = True
    binomial_theorem_collection: List[List[str]] \
        = gen_binomial_theorem_collection(p_elements=elements,
                                          p_zero_elem_mark=p_zero_elem)
    headers: List[str] = gen_all_combos(binomial_theorem_collection)
    data_frame: DataFrame = init_data_frame(p_table_headers=headers)
    build_data_frame(p_data_frame=data_frame,
                     p_zero_elem=p_zero_elem)
    render_plot(p_data_frame=data_frame,
                p_mpl=mpl,
                p_dpi=dpi,
                p_font_size=font_size,
                p_no_tick_marks=no_tick_marks,
                p_zero_elem=p_zero_elem)
    plt.savefig(p_file_path)


def test_full_CSA_generation(p_dim: int, p_file_path: str, p_zero_elem: str) -> None:
    """
    Entry point for generating and saving the Cayley table diagram.
    """

    match p_dim:
        case 2:
            test_2d_generation(p_file_path, p_zero_elem)
        case 5:
            test_5d_generation(p_file_path, p_zero_elem)
        case 6:
            test_6d_generation(p_file_path, p_zero_elem)
        case 7:
            test_7d_generation(p_file_path, p_zero_elem)
        case 8:
            test_8d_generation(p_file_path, p_zero_elem)
        case 9:
            test_9d_generation(p_file_path, p_zero_elem)
        case _:
            print("You can implement it by yourself")


