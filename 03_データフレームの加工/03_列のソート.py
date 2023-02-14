# ******************************************************************************
# Project   : Pandasのメモ
# Chapter   : 03 データフレームの加工
# Theme     : 03 列のソート
# Date      : 2023/02/14
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 列名を指定して並び替え
# 2 別のデータフレームの順番に並び替え
# 3 特定列を先頭にして並び替え
# 4 複数列を先頭にして並び替え


# 0 準備 --------------------------------------------------------------------

# ライブラリ
import numpy as np
import pandas as pd
import seaborn as sns


# データ準備
iris = sns.load_dataset('iris')
iris_na = iris.mask(np.random.random(iris.shape) < .1)


# 1 列名を指定して並び替え -------------------------------------------------------

# ＜ポイント＞
# - データフレームの列を並び替える方法は以下の2種類がある
#   --- 単純に列名を選択
#   --- メソッドによる並び替え


# 列名を確認
# --- コンソールに列名がリストで表示されるのでコピーして使用
iris.columns

# 列名選択を使用
# --- ブラケット
# --- locプロパティ
# --- filterメソッド
iris[['petal_length', 'petal_width', 'sepal_length', 'sepal_width']]
iris.loc[:, ['petal_length', 'petal_width', 'sepal_length', 'sepal_width']]
iris.filter(['petal_length', 'petal_width', 'sepal_length', 'sepal_width'])

# メソッドによる並び替え
# --- 明示的なメソッドを使用
iris.reindex(columns=['petal_length', 'petal_width', 'sepal_length', 'sepal_width'])


# 2 別のデータフレームの順番に並び替え ------------------------------------------------

# ＜ポイント＞
# - 特定のデータフレームの列順序を参照して並び替える

# 準備
# --- 異なる列順のデータフレーム
# --- speciesを除いたデータフレーム
iris_reorder = iris[['species', 'sepal_width', 'petal_width', 'sepal_length', 'petal_length']]
iris_col4 = iris[['sepal_width', 'petal_width', 'sepal_length', 'petal_length']]

# 参照データフレームの列順にソート
# --- 全ての列が揃っている場合
# --- 列の一部がない場合
iris.reindex_like(iris_reorder)
iris.reindex_like(iris_col4)

# 参照データフレームに列が存在しない場合
# --- 元のデータフレームに存在しない列はNaNとなる
# --- 必要に応じて不要列は削除
iris_col4.reindex_like(iris_reorder)
iris_col4.reindex_like(iris_reorder).dropna(axis=1)


# 3 特定列を先頭にして並び替え -------------------------------------------------------

# ＜ポイント＞
# - 直接的なソート手法がないため、データの分割＆結合を利用して並び替え


# データフレームを分割＆再結合
# --- ｢先頭に持ってきたい列｣｢それ以外の列｣でデータフレームを作成
# --- ｢先頭に持ってきたい列｣を先にして再結合
df1 = iris[['species']]
df2 = iris.drop('species', axis=1)
pd.concat([df1, df2], axis=1)

# 並び替え後のリストを作成
# --- 列名をリストで取得
# --- 先頭にしたい列を削除
# --- 先頭列をリストの先頭に指定（残りは*でリストをアンパック）
cols = iris.columns.tolist()
cols.remove('species')
iris[['species', *cols]]

# 参考：アンパックの動作
# --- アンパックなし（リストが維持される）
# --- アンパックあり（リストが解除される）
['species', cols]
['species', *cols]


# 4 複数列を先頭にして並び替え ------------------------------------------------------

# ＜ポイント＞
# - 直接的なソート手法がないため、データの分割＆結合を利用して並び替え


# 単純な方法
# --- 単一列の並び替えと同じ要領
col_lst = iris.columns.tolist()
col_lst.remove('petal_length')
col_lst.remove('petal_width')
iris[['petal_length', 'petal_width', *col_lst]]

# 内包表記の活用
col_lst = iris.columns.tolist()
cols_to_front = ['petal_length', 'petal_width']
l2 = [col for col in col_lst if col not in cols_to_front]
iris[[*cols_to_front, *l2]]
