"""
Project   : Pandasのメモ
Chapter   : 04 データフレームの集計
Theme     : 12 列の集計変換
Date      : 2023/03/14
"""


# ＜目次＞
# 0 準備
# 1 数値列のスケーリング
# 2 数値列のZスコア変換
# 3 数値列のZスコア変換
# 4 数値列の順位変換
# 5 数値列の分位変換
# 6 行番号の追加


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import numpy as np
import pandas as pd
import seaborn as sns


# データロード
iris = sns.load_dataset('iris')


# 1 数値列のスケーリング --------------------------------------------------------------

# ライブラリ
from sklearn import preprocessing


# 関数定義
def rescaling(x):
    return (x - x.min()) / (x.max() - x.min())


# 関数定義して適用
iris.filter(['sepal_length'])\
    .assign(rescaling=lambda x: rescaling(x))

# ラムダ式で定義
iris.filter(['sepal_length'])\
    .assign(zscore=lambda x: (x - x.min()) / (x.max() - x.min()))

# {sklearn}の関数を使用
iris.filter(['sepal_length'])\
    .assign(zscore=lambda x: preprocessing.minmax_scale(x))

# {sklearn}のメソッドを使用
mm = preprocessing.MinMaxScaler()
iris.filter(['sepal_length'])\
    .assign(zscore=lambda x: mm.fit_transform(x))


# 2 数値列のZスコア変換 --------------------------------------------------------------

# 関数定義
def my_zscoer(x):
    return (x - x.mean()) / x.std(dof=0)


# 関数定義して適用
iris.filter(['sepal_length'])\
    .assign(zscore=lambda x: my_zscoer(x))

# ラムダ式で定義
iris.filter(['sepal_length'])\
    .assign(zscore=lambda x: (x - x.mean()) / x.std())

# {scipy]による定義
import scipy.stats
iris.filter(['sepal_length'])\
    .assign(zscore=lambda x: scipy.stats.zscore(x))


# 3 異常値の置換 -------------------------------------------------------------------

# 準備：数値範囲の確認
# --- 25% : 5.100000
# --- 75% : 6.400000
iris['sepal_length'].describe()

# 異常値を固定値で指定
iris.filter(['sepal_length'])\
    .assign(clip=lambda x: x['sepal_length'].clip(lower=5.1, upper=6.4))

# 異常値をパーセンタイルで指定
iris.filter(['sepal_length'])\
    .assign(clip=lambda x: x['sepal_length'].clip(lower=x['sepal_length'].quantile(0.25),
                                                  upper=x['sepal_length'].quantile(0.75)))


# 3 数値列のZスコア変換 --------------------------------------------------------------------

# 関数定義
def my_zscoer(x):
    return (x - x.mean()) / x.std(dof=0)


# 関数定義して適用
iris.filter(['sepal_length'])\
    .assign(zscore=lambda x: my_zscoer(x))

# ラムダ式で定義
iris.filter(['sepal_length'])\
    .assign(zscore=lambda x: (x - x.mean()) / x.std())

# {scipy]による定義
import scipy.stats
iris.filter(['sepal_length'])\
    .assign(zscore=lambda x: scipy.stats.zscore(x))


# 4 数値列の順位変換 --------------------------------------------------------------------

# ＜ポイント＞
# - ｢method｣や｢na_options｣などの引数があって、細かいコントロールをすることも可能

# 順位
iris.assign(pct_rank=lambda x: x['sepal_length'].rank())

# パーセントランク
iris.assign(pct_rank=lambda x: x['sepal_length'].rank(pct=True))


# 5 数値列の分位変換 --------------------------------------------------------------------

# ＜ポイント＞
# - qcut()は数値データをカテゴリカルの範囲データに変換する
#   --- 分位変換の際は範囲データにラベルを付けることで対処する


# 分位変換
# --- 分位はカテゴリカルとして出力
iris.assign(tile=lambda x: pd.qcut(x['sepal_length'], q=5, labels=range(1, 5+1)))

# 分位変換
# --- 分位を文字列に変換
iris.assign(tile=lambda x: 'F' + pd.qcut(x['sepal_length'], q=5, labels=range(1, 5+1)).astype(str))

# ＜参考＞
# qcut()の動作
# --- ラベル指定なし
pd.qcut(iris['sepal_length'], q=5)


# 6 行番号の追加 --------------------------------------------------------------------

# 数値番号を生成して追加
iris.assign(row_number=lambda x: np.arange(x.shape[0]))

# インデクスが行番号の場合
iris.reset_index()
