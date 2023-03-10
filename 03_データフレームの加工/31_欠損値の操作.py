"""
Project   : Pandasのメモ
Chapter   : 03 データフレームの加工
Theme     : 31 欠損値の操作
Date      : 2023/03/04
"""


# ＜目次＞
# 0 準備
# 1 欠損値のカウント
# 2 欠損値の削除
# 3 欠損値の抽出
# 4 全て欠損値の列削除


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import numpy as np
import seaborn as sns


# データロード
iris = sns.load_dataset('iris')

# データ加工
# --- NaNを追加
iris = iris.mask(np.random.random(iris.shape) < .1)


# 1 欠損値のカウント --------------------------------------------------------------

# 総数
iris.isnull().values.sum()

# 列ごとのカウント
iris.isnull().sum()

# 行ごとのカウント
iris.isnull().sum(axis=1)


# 2 欠損値の削除 ------------------------------------------------------------------

# 全ての列を対象
iris.dropna()

# 特定列を対象
iris.dropna(subset=['sepal_length', 'sepal_width'])


# 3 欠損値の抽出 ------------------------------------------------------------------

# 欠損値を含む行
iris[iris.isnull().any(axis=1)]

# 指定列が欠損値の行
iris[iris['sepal_length'].isnull()]


# 4 全て欠損値の列削除 ----------------------------------------------------------

# データ準備
# --- 特定列が全てNaN
iris2 = iris.assign(sepal_length=np.NaN)

# 全て欠損値の列削除
iris2.dropna(axis=1, how='all')
