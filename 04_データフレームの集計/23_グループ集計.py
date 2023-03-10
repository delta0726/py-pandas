"""
Project   : Pandasのメモ
Chapter   : 04 データフレームの集計
Theme     : 23 グループ集計
Date      : 2023/03/09
"""


# ＜目次＞
# 0 準備
# 1 集計メソッドによる演算
# 2 グループ演算のパターン
# 3 aggメソッドによる集計
# 4 applyメソッドによる集計


# 0 準備 ---------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import numpy as np
import seaborn as sns


# データ読み込み
iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')


# 1 集計メソッドによる演算 ------------------------------------------------------------

# ＜ポイント＞
# - グループ化したオブジェクトに対して集計メソッドを適用するとグループレベルで集計される
# - グループ化に適用したキーはインデックスとして扱われる


# 集計メソッドによる集計
# --- 単一グループ
# --- 複数グループ
iris.groupby(['species']).mean()
tips.groupby(['day', 'sex']).mean()

# インデックス解除
# --- グループ化に適用したキーはインデックスとして扱われる
# --- 必要に応じてreset_index()を適用する
iris.groupby(['species']).mean().reset_index()

# インデックスを使わないグループ集計
# --- groupby()でas_index引数をFalseにすると
iris.groupby(['species'], as_index=False).mean()
#

# 2 グループ集計のパターン ------------------------------------------------------------

# ＜ポイント＞
# - グループ集計は集計メソッド/agg()/apply()を使って行うことができる
# - 集計はデータが一意に定義される演算によって実現される


# 集計メソッド
# --- 1つの値に集計される演算
iris.groupby(['species']).mean()

# aggメソッド
# --- 外部関数を使用
iris.groupby(['species']).agg(np.mean)

# applyメソッド
# --- applyメソッドはデータフレームをインプットして行ごとに関数を適用した結果を返す
iris.groupby(['species']).apply(np.mean)

# 独自関数
# --- ラムダ式
iris.groupby(['species']).agg(lambda x: np.max(x) - np.min(x))

# 独自関数
# --- 関数定義
def calc_range(x):
    return (np.max(x) - np.min(x))

iris.groupby(['species']).agg(calc_range)


# 3 aggメソッドによる集計 --------------------------------------------------------

# ＜ポイント＞
# - agg()は引数として与えた関数を指定列に適用して集計する
#   --- agg()はaggregate()のエイリアス


# 全ての列を集計
# --- 単一の関数で集計
# --- 複数の関数で集計（列がグループ化される）
iris.groupby(['species']).agg(np.mean)
iris.groupby(['species']).agg([np.mean, np.std])

# 指定列を集計（メソッド）
# --- 辞書で適用列ごとにメソッドを指定
iris.groupby(['species'])\
    .agg({'sepal_length':'mean',
          'sepal_width':'sum'})

# 指定列を集計（関数）
# --- 辞書で適用列ごとに関数を指定
iris.groupby(['species'])\
    .agg({'sepal_length': np.mean,
          'sepal_width': np.sum})

# 指定列を集計（ミックス）
# --- 辞書で適用列ごとにメソッド/関数/ラムダ式を指定
def my_range(x):
    return(np.max(x) - np.min(x))

iris.groupby(['species'])\
    .agg({'sepal_length':['max', 'min', 'mean', 'median',
                          np.sum,
                          my_range,
                          lambda x: np.percentile(x, q=20)]})

# ＜参考＞
# 同じ列を複数の関数で集計した場合は最後の演算が適用される
iris.groupby(['species'])\
    .agg({'sepal_length':'min',
          'sepal_length':'sum'})


# 4 applyメソッドによる集計 ----------------------------------------------------

# ＜ポイント＞
# - applyメソッドはデータフレームをインプットして行ごとに関数を適用した結果を返す
# - applyメソッドはパフォーマンスが劣る可能性が指摘される
#   --- 集計イテレーションごとに関数を呼び出しているため

# 全ての列を集計
# --- 単一の関数で集計
iris.groupby(['species']).apply(np.mean)

