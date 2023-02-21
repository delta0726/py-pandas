# ******************************************************************************
# Project   : Pandasのメモ
# Chapter   : 03 データフレームの加工
# Title     : 13 行のソート
# Date      : 2023/02/18
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 行方向のソート
# 2 列方向のソート
# 3 文字列を任意の順番にソート
# 4 インデックスのソート
# 5 マルチインデックスのソート


# 0 準備 ----------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns


# データロード
iris = sns.load_dataset('iris')

# データ準備
# --- ランダムソート
iris = iris.sample(frac=1, random_state=0)


# 1 行方向のソート ---------------------------------------------------------

# 単一キーでソート
iris.sort_values(by='sepal_length', ascending=True)

# 複数キーでソート
# --- リストでキーを指定
iris.sort_values(by=['sepal_length', 'sepal_width'], ascending=[True, False])

# ランダムソート
# --- ランダムサンプリングで全て残す
iris.sample(frac=1, random_state=0)


# 2 列方向のソート ------------------------------------------------------------

# 列の並び替え
iris.sort_index(axis=1, ascending=False)


# 3 文字列を任意の順番にソート -------------------------------------------------

# ＜ポイント＞
# - 直接的なソート方法がないので、作業列を介在してソートする

# オーダー指定
order = {'versicolor': 0, 'setosa': 1, 'virginica': 2}

# 任意の順番にソート
iris.assign(order=lambda x: x['species'].map(order))\
    .sort_values(by='order', ascending=True)\
    .drop('order', axis=1)\
    .reset_index(drop=True)


# 4 インデックスのソート -----------------------------------------------------

# インデックスでソート
# --- 昇順
# --- 降順
iris.sort_index(axis=0, ascending=True)
iris.sort_index(axis=0, ascending=False)


# 5 マルチインデックスのソート --------------------------------------------------

# 準備
iris_multi = iris.set_index(['sepal_length', 'petal_length'])

# マルチインデックスのソート
iris_multi.sort_index(level=['sepal_length', 'petal_length'], ascending=True)
iris_multi.sort_index(level=['petal_length', 'sepal_length'], ascending=True)
