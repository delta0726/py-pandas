"""
Category  : Grammar of Pandas
Chapter   : 繰り返し処理
Title     : map
Update    : 2023/03/04
"""


# ＜概要＞
# - mapメソッドはシリーズをインプットして要素ごとに関数を適用した結果を返す
#   --- インプットがシリーズなので単一列で処理できるものに適用（複数列にまたがる処理には不向き）
#   --- applyよりも高速に動作する


# ＜目次＞
# 0 準備
# 1 関数の逐次適用
# 2 データフレームの列に関数を適用
# 3 データフレームの要素置換


# 0 準備 ---------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns


# データ読み込み
iris = sns.load_dataset('iris')


# 1 関数の逐次適用 -------------------------------------------------------------------

# ＜ポイント＞
# - mapメソッドは要素に対して関数を逐次的に適用する処理を行う
#   --- シリーズをインプットとして要素ごとに適用するケースが多い


# 関数定義
def func(x):
    if x == 'setosa':
        return 'Setosa'
    elif x == 'versicolor':
        return 'Versicolor'
    elif x == 'virginica':
        return 'Virginica'
    else:
        return 'Other'


# 関数適用（単一要素）
# --- 引数は文字列なので要素にしか適用できない
func('setosa')

# 関数適用（逐次適用）
# --- mapメソッドに関数を適用することで逐次処理が可能
iris['species'].map(func)


# 2 データフレームの列に関数を適用 -----------------------------------------------------

# ＜ポイント＞
# - データフレームの要素ごとに関数を適用する場合に使用する
#   --- 条件分岐を伴う処理に使うことが多い（メソッド化されていない処理）


# 関数定義
def func(x):
    if x == 'setosa':
        return 'Setosa'
    elif x == 'versicolor':
        return 'Versicolor'
    elif x == 'virginica':
        return 'Virginica'
    else:
        return 'Other'


# データフレームの列に関数を適用
iris.assign(speces2=lambda x: x['species'].map(func))


# 3 データフレームの要素置換 -------------------------------------------------------------

# ＜ポイント＞
# - 簡単な条件分析の処理は辞書で表現することができる
#   --- mapメソッドと組み合わせることで、要素の置換処理が可能となる


# 置換用の辞書
replace_dict = {'setosa': 'Setosa',
                'versicolor': 'Versicolor',
                'virginica': 'Virginica'}

# mapによる要素置換
iris.assign(Species2=lambda x: x['species'].map(replace_dict))

# replaceによる要素置換
iris.assign(Species2=lambda x: x['species'].replace(replace_dict))
