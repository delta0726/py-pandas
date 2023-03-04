"""
Category  : Grammar of Pandas
Chapter   : 繰り返し処理
Title     : apply
Update    : 2023/03/04
"""


# ＜目次＞
# 0 準備
# 1 関数の逐次適用
# 2 データフレームの列に関数を適用


# 0 準備 ---------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns


# データ読み込み
iris = sns.load_dataset('iris')


# 1 行ごとの関数適用 -------------------------------------------------------------------

# ＜ポイント＞
# - applyメソッドはデータフレームを受けて逐次処理を行う
#   --- インプットにデータフレームを受けるため複数列のデータを使った処理が可能となる
#   --- インプットがシリーズの場合はmapメソッドを使う（mapの方が高速）


# 関数定義
def func(df):
    if df['species'] == 'setosa':
        return df['sepal_length']
    elif df['species'] == 'versicolor':
        return 2
    elif df['species'] == 'virginica':
        return 3
    else:
        None


# 関数適用（逐次適用）
# --- mapメソッドに関数を適用することで逐次処理が可能
iris.apply(func, axis=1)


# 2 データフレームの列に関数を適用 -----------------------------------------------------

# ＜ポイント＞
# - applyメソッドで適用する関数がシリーズを出力する場合はassignメソッドと相性が良い


# 関数定義
def func(df):
    if df['species'] == 'setosa':
        return df['sepal_length']
    elif df['species'] == 'versicolor':
        return 2
    elif df['species'] == 'virginica':
        return 3
    else:
        None


# データフレームの列に関数を適用
iris.assign(new_col=lambda x: x.apply(func, axis=1))
