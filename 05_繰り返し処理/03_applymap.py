"""
Category  : Grammar of Pandas
Chapter   : 繰り返し処理
Title     : applymap
Update    : 2023/03/04
"""


# ＜概要＞
# - applymapメソッドはデータフレームをインプットとして全ての列に関数を適用する


# ＜目次＞
# 0 準備
# 1 全ての列に関数を適用


# 0 準備 ---------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns


# データ読み込み
iris = sns.load_dataset('iris').drop(columns='species')


# 1 全ての列に関数を適用 --------------------------------------------------------------

# ＜ポイント＞
# - applymapメソッドはデータフレームをインプットして全ての列に逐次処理を行う
#   --- 簡単な関数を適用することが多い（複数列に同じ処理を適用するという性質上）


# 関数定義
def func(x):
    return x * 100


# 全ての列に関数適用
# --- 定義済の関数を使用
iris.applymap(func)

# 全ての列に関数適用
# --- ラムダ式を使用（xはcolumn）
iris.applymap(lambda x: x * 100)
