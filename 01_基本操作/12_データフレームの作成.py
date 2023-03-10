"""
Category  : Grammar of Pandas
Chapter   : 01 基本操作
Title     : 12 データフレームの作成
Date      : 2023/02/08
"""


# ＜目次＞
# 0 準備
# 1 辞書から作成
# 2 二次元配列から作成


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import pandas as pd
import numpy as np


# 1 辞書から作成 --------------------------------------------------------------

# ＜ポイント＞
# - データフレームは列の集合体であるため、列の定義方法でパターンが分かれている


# リスト
pd.DataFrame(
    data={'Col1': [10, 20, 30, 40],
          'Col2': [50, 60, 70, 80],
          'Col3': ['a', 'b', 'c', 'd']})

# ndarray
pd.DataFrame(
    data={'Col1': np.array([10, 20, 30, 40]),
          'Col2': np.array([50, 60, 70, 80]),
          'Col3': np.array(['a', 'b', 'c', 'd'])})

# Pandas Series
pd.DataFrame(
    data={'Col1': pd.Series([10, 20, 30, 40]),
          'Col2': pd.Series([50, 60, 70, 80]),
          'Col3': pd.Series(['a', 'b', 'c', 'd'])}
)


# 2 二次元配列から作成 ---------------------------------------------------------

# 二次元配列から作成
pd.DataFrame(
    data=np.array([[10, 20, 30, 40],
                   [11, 21, 31, 41],
                   [12, 22, 32, 42]]),
    index=['Row1', 'Row2', 'Row3'],
    columns=['Col1', 'Col2', 'Col3', 'Col4']
)
