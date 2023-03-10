"""
Project   : Pandasのメモ
Chapter   : 03 データフレームの加工
Title     : 22 インデクスでフィルタ
Date      : 2023/02/22
"""


# ＜目次＞
# 0 準備
# 1 インデックスの構造
# 2 locによるフィルタ
# 3 pd.IndexSliceによるフィルタ
# 4 xsメソッドによるフィルタ


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns


# データロード
iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')

# データ準備
# --- インデックスの追加
iris_idx = iris.set_index('species')
tips_idx = tips.set_index(['day', 'sex', 'time'])


# 1 インデックスの構造 ------------------------------------------------------------

# ＜ポイント＞
# - 単独インデックスの場合はリスト
# - マルチインデックスの場合はリスト＆タプル

# インデックスの確認
iris_idx.index
tips_idx.index


# 2 locによるフィルタ -------------------------------------------------------------

# ＜ポイント＞
# - 抽出する要素が決まっている場合はlocプロパティで要素を指定することで抽出する
#   --- 複数要素の場合はリストで指定する
#   --- インデックスレベルはタプルで指定する

# レベル1のみ指定
# --- レベル2以降のみ表示される
tips_idx.loc['Sun']
tips_idx.loc['Sun', :]

# レベル1とレベル2を指定
# --- 複数レベルはタプルで指定
tips_idx.loc[('Sun', 'Female')]
tips_idx.loc[('Sun', 'Female'), :]

# 複数の要素を指定する
# --- 単独レベルの複数の要素はリストで指定する
# --- マルチレベルの場合はタプル＆リストで指定する（",:"は省略不可となる）
tips_idx.loc[['Sun', 'Sat']]
tips_idx.loc[(['Sun', 'Sat'], ['Female', 'Male']), :]


# 3 pd.IndexSliceによるフィルタ -------------------------------------------------------

# ＜ポイント＞
# - pd.IndexSliceを使ってlocプロパティを指定する方法もある
#   --- 複数レベルを指定するときにタプルが不要となる
#   --- ":"で全体を指定することが可能となる

# レベル1のみ指定
tips_idx.loc[pd.IndexSlice['Sun']]

# レベル1とレベル2を指定
tips_idx.loc[pd.IndexSlice['Sun', 'Female']]

# レベル2を":"で指定
tips_idx.loc[pd.IndexSlice[['Sun', 'Sat'], :, 'Dinner'], :]

# 複数の要素を指定する
# --- 単独レベルの複数の要素はリストで指定する
# --- マルチレベルの場合はタプル＆リストで指定する（",:"は省略不可となる）
tips_idx.loc[pd.IndexSlice[['Sun', 'Sat']], :]
tips_idx.loc[pd.IndexSlice[(['Sun', 'Sat'], 'Female')], :]


# 4 xsメソッドによるフィルタ -----------------------------------------------------------

# ＜ポイント＞
# - xsメソッドを使うとlocプロパティを使わずに操作することができる
#   --- 抽出対象をリストで指定することができない

# レベル1のみ指定
# --- インデックスレベルを指定する
# --- レベルはインデックスで指定することも可能
tips_idx.xs('Sun', level='day')
tips_idx.xs('Sun', level=0)

# 選択対象をスライスで指定
# --- リストで指定することはできない
tips_idx.xs(pd.IndexSlice['Sat':'Sun'], level='day')
