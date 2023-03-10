"""
Project   : Pandasのメモ
Chapter   : 04 データフレームの集計
Theme     : 12 列の集計変換
Date      : 2023/02/23
"""


# ＜目次＞
# 0 準備
# 1 全ての列を集計
# 2 カテゴリカルデータの列をカウント
# 3 パーセントランクに変換
# 4 連続データの離散化
# 5 列のデータ変換


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import numpy as np
import pandas as pd
import seaborn as sns


# データロード
iris = sns.load_dataset('iris')


# 3 パーセントランクに変換 ----------------------------------------------------

# ＜ポイント＞
#

# シリーズ
iris['sepal_length'].rank(pct=True)

# データフレーム
iris[['sepal_length']]\
    .assign(Pct_Rank=lambda x: x['sepal_length'].rank(pct=True))\
    .sort_values(by='sepal_length', ascending=True)


# ＜参考：Rankメソッド＞

# データフレーム作成
df = pd.DataFrame(data={'Animal': ['cat', 'penguin', 'dog', 'spider', 'snake'],
                        'legs': [4, 2, 4, 8, np.nan]})

# さまざまな順位
# --- デフォルトの順位計算方法はaverageになっている（一般的にmaxの方がイメージと合うか？）
# --- na_option引数でNAの処理方法を決めることができる
df.assign(default_rank=lambda x: x['legs'].rank(method='average'))\
    .assign(max_rank=lambda x: x['legs'].rank(method='max'))\
    .assign(NA_bottom=lambda x: x['legs'].rank(na_option='bottom'))\
    .assign(pct_rank=lambda x: x['legs'].rank(pct=True))


# 4 連続データの離散化 --------------------------------------------------------

# Seriesでビニング適用
# --- CategoricalDtypeとして格納
# --- 必要に応じて文字列変換
bins = pd.cut(iris['sepal_length'], 3, labels=['low', 'median', 'high'])
bins.dtype
bins.astype('str')

# 列のビニング適用
# --- 数値範囲が3分位となるように変換
iris[['sepal_length']]\
    .assign(price_group=lambda x: pd.cut(x['sepal_length'], bins=3))\
    .groupby('price_group')\
    .count()\
    .reset_index()

# 列のビニング適用
# --- 数値範囲が3分位となるように変換
iris[['sepal_length']]\
    .assign(price_group=lambda x: pd.qcut(x['sepal_length'], q=[0, 0.33, 0.66, 1], labels=['low', 'medium', 'high']))\
    .groupby('price_group')\
    .count()\
    .reset_index()


# 5 列のデータ変換 --------------------------------------------------------

# データ全体の集計
# --- 文字列の列が含まれないようにする
iris.select_dtypes("float")\
    .transform(lambda x: (x - x.mean()) / x.std())
