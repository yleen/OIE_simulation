from typing import List

import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
from matplotlib import colors
import matplotlib as mpl
from matplotlib.colors import ListedColormap
from pandas.core.interchange.dataframe_protocol import DataFrame


def init_data_frame(p_table_headers: List[str]) -> DataFrame:
    return pd.DataFrame(index=p_table_headers,
                        columns=p_table_headers)


def has_no_common_element(p_combination1: str, p_combination2: str) -> bool:
    """
    Verify that the elements are distinct
    @param p_combination1: first element
    @param p_combination2: second element
    @return: True if there are no common elements, otherwise False
    """

    for element in p_combination1:
        if element in p_combination2:
            return False

    return True


def combination_merge(p_combination1, p_combination2) -> str:
    """
    Merge combinations
    @param p_combination1: first element
    @param p_combination2: second element
    @return: merged element
    """

    merged_combination: str = p_combination1 + p_combination2
    merged_combination: str = ''.join(sorted(merged_combination))

    return merged_combination


def gen_binomial_theorem_collection(p_elements: str,
                                    p_contain_zero: bool,
                                    p_zero_elem_mark: str,
                                    p_err_elem_mark: str) -> List[List[str]]:
    """
    Generate binomial theorem type collection
    @param p_elements: elements
    @param p_contain_zero: verify includes zero
    @param p_zero_elem_mark: zero element
    @param p_err_elem_mark: invalid OIE mark
    @return: binomial theorem type collection
    """

    comb_and_next_start_collection: List[List[dict]] = []
    binomial_theorem_collection: List[List[str]] = []

    if p_contain_zero:
        binomial_theorem_collection: List[List[str]] = [[p_zero_elem_mark]]

    binomial_theorem_collection.append([p_err_elem_mark])

    for i in range(len(p_elements)):
        cur_comb_and_next_start_list: List[dict] = []
        if i == 0:
            for j in range(len(p_elements)):
                cur_comb_and_next_start: dict = {
                    'combination': p_elements[j],
                    'next_trip_starting_idx': j + 1
                }
                cur_comb_and_next_start_list.append(cur_comb_and_next_start)
        else:
            pre_comb_and_next_start_list: List[dict] = comb_and_next_start_collection[i - 1]
            for pre_comb_and_next_start in pre_comb_and_next_start_list:
                pre_comb: str = pre_comb_and_next_start['combination']
                for j in range(pre_comb_and_next_start['next_trip_starting_idx'], len(p_elements)):
                    cur_comb: str = pre_comb + p_elements[j]
                    cur_comb_and_next_start: dict = {
                        'combination': cur_comb,
                        'next_trip_starting_idx': j + 1
                    }
                    cur_comb_and_next_start_list.append(cur_comb_and_next_start)
        comb_and_next_start_collection.append(cur_comb_and_next_start_list)

    for i in range(len(p_elements)):
        cur_binomial_theorem_item: List[str] = []
        for j in range(len(comb_and_next_start_collection[i])):
            cur_comb: str = comb_and_next_start_collection[i][j]['combination']
            cur_binomial_theorem_item.append(cur_comb)
        binomial_theorem_collection.append(cur_binomial_theorem_item)

    return binomial_theorem_collection


def gen_all_combos(p_binomial_theorem_collection: List[List[str]]) -> List[str]:
    """
    Generate all combinations
    @param p_binomial_theorem_collection: binomial theorem type collection
    @return: list of all combinations
    """

    all_combos: List[str] = []

    for combos in p_binomial_theorem_collection:
        for combo in combos:
            all_combos.append(combo)

    return all_combos


def gen_combinations_data_recur(elements):
    """
    Generate combination data (recursive)
    @param elements: elements
    @return: combination data
    """

    combinations_and_pivots_cache = []

    zero_element = '0'
    zero_element_array = ['0']
    combinations = [zero_element]
    binomial_theorem_array = [zero_element_array]

    gen_sub_combinations_data_recur(combinations_and_pivots_cache,
                                    combinations,
                                    binomial_theorem_array,
                                    len(elements),
                                    elements)

    return {
        'combinations': combinations,
        'binomial_theorem_array': binomial_theorem_array
    }


def gen_sub_combinations_data_recur(combinations_and_pivots_cache,
                                    combinations,
                                    binomial_theorem_array,
                                    count,
                                    elements):
    """
    Generate headers for sub-axes
    @param combinations_and_pivots_cache: array of element combinations and end pivot positions
    @param combinations: array of element combinations
    @param binomial_theorem_array: array of binomial coefficient distributions
    @param count: number of elements involoed in combinations
    @param elements: Complete set of elements array
    @return None
    """

    cur_combinations_and_pivots = []                                                        # current array of element combinations and end pivot positions 

    if count == 1:                                                                          # if elements is 1
        for i in range(len(elements)):                                                      # traverse elements:
            cur_combination_and_pivot = {                                                   #
                'combination': elements[i],
                'pivot': i
            }
            cur_combinations_and_pivots.append(cur_combination_and_pivot)
    else:
        gen_sub_combinations_data_recur(combinations_and_pivots_cache,
                                        combinations,
                                        binomial_theorem_array,
                                        count - 1,
                                        elements)

        pre_combinations_and_pivots = combinations_and_pivots_cache[count - 2]

        for i in range(len(pre_combinations_and_pivots)):
            pre_combination = pre_combinations_and_pivots[i]['combination']

            for j in range(pre_combinations_and_pivots[i]['pivot'] + 1, len(elements)):
                cur_combination = pre_combination + elements[j]
                cur_combination_and_pivot = {
                    'combination': cur_combination,
                    'pivot': j
                }
                cur_combinations_and_pivots.append(cur_combination_and_pivot)

    combinations_and_pivots_cache.append(cur_combinations_and_pivots)

    cur_binomial_theorem_item = []
    binomial_theorem_array.append([])
    for i in range(len(cur_combinations_and_pivots)):
        cur_combination = cur_combinations_and_pivots[i]['combination']
        combinations.append(cur_combination)
        cur_binomial_theorem_item.append(cur_combination)

    binomial_theorem_array.append(cur_binomial_theorem_item)


def build_data_frame(p_data_frame: DataFrame,
                     p_zero_elem: str,
                     p_err_elem: str) -> None:
    """
    p_data_frame creator
    @param p_data_frame: DataFrame instance
    @param p_zero_elem: 0 element
    @param p_err_elem: err element
    @return:
    """
    for row in p_data_frame.index:
        for col in p_data_frame.columns:
            if row == p_err_elem or col == p_err_elem:
                p_data_frame.loc[row, col] = p_err_elem
                continue

            if row == p_zero_elem:
                p_data_frame.loc[row, col] = col
            elif col == p_zero_elem:
                p_data_frame.loc[row, col] = row
            else:
                if has_no_common_element(row, col):
                    p_data_frame.loc[row, col] = combination_merge(row, col)
                else:
                    p_data_frame.loc[row, col] = p_err_elem


def render_plot(p_data_frame: DataFrame,
                p_mpl: mpl,
                p_dpi: int,
                p_font_size: float,
                p_no_tick_marks: bool,
                p_err_elem: str) -> None:
    """
    Render the plot
    @param p_data_frame: graph frame
    @param p_mpl: matplotlib
    @param p_dpi: dots per inch
    @param p_font_size: font size
    @param p_no_tick_marks: whether it has a tick mark
    @param p_err_elem: Error OIE's mark
    @return: None
    """

    p_mpl.rcParams["font.size"] = p_font_size

    if p_dpi is not None:
        p_mpl.rcParams["figure.dpi"] = p_dpi

    fig, ax = p_mpl.pyplot.subplots()

    ax.spines['top'].set_linewidth(0)
    ax.spines['bottom'].set_linewidth(0)
    ax.spines['left'].set_linewidth(0)
    ax.spines['right'].set_linewidth(0)

    if p_no_tick_marks:
        ax.tick_params(axis='both', which='both', length=0)
    else:
        ax.tick_params(axis='both', which='both', length=1, colors='navy')

    color_matrix: List[List[int]] = []
    for row_idx in range(p_data_frame.index.size):
        row_colors: List[int] = []
        for col_idx in range(p_data_frame.columns.size):
            if p_data_frame.values[row_idx][col_idx] == p_err_elem:
                row_colors.append(0)
            else:
#                row_colors.append(100)
                cur_comb_size: int = len(p_data_frame.values[row_idx][col_idx])
                value: int = (cur_comb_size + 1) * 5
                row_colors.append(value)
        color_matrix.append(row_colors)

#    cmap: ListedColormap = colors.ListedColormap(['#080402', '#D03D33'])
    cmap: ListedColormap = p_mpl.colormaps.get_cmap('gist_heat')
    ax.imshow(X=np.array(color_matrix),
              cmap=cmap)

    ax.set_xticks(ticks=np.arange(p_data_frame.columns.size),
                  labels=p_data_frame.columns)
    ax.set_yticks(ticks=np.arange(p_data_frame.index.size),
                  labels=p_data_frame.index)

    ax.tick_params(top=True,
                   bottom=False,
                   labeltop=True,
                   labelbottom=False)

    # Rotate the tick labels and set their alignment.
    p_mpl.pyplot.setp(ax.get_xticklabels(),
                      rotation=-70,
                      ha="right",
                      va="center_baseline",
                      rotation_mode="anchor")

    fig.tight_layout()


if __name__ == '__main__':

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
    # dpi: int = 500
    # contain_zero = False
    # font_size: float = 4
    # no_tick_marks: bool = False
    # binomial_theorem_collection: List[List[str]] \
    #     = gen_binomial_theorem_collection(p_elements=elements5,
    #                                       p_contain_zero=contain_zero,
    #                                       p_zero_elem_mark=zero_elem_mark,
    #                                       p_err_elem_mark=err_elem_mark)

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
    dpi: int = 3000
    contain_zero = True
    font_size: float = 0.45
    no_tick_marks: bool = True
    binomial_theorem_collection: List[List[str]] \
        = gen_binomial_theorem_collection(p_elements=elements9,
                                          p_contain_zero=contain_zero,
                                          p_zero_elem_mark=zero_elem_mark,
                                          p_err_elem_mark=err_elem_mark)

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

    mpl.pyplot.savefig('pic.png')
