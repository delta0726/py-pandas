# ******************************************************************************
# Project   : Pandasのメモ
# Chapter   : 03 データフレームの加工
# Title     : 41 データ結合
# Date      : 2023/02/18
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 行方向のデータ結合
# 2 列方向のデータ結合
# 3 mergeによるテーブル結合
# 4 joinによるテーブル結合


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns


# データロード
iris = sns.load_dataset('iris')


# 1 行方向のデータ結合 -------------------------------------------------

# ＜ポイント＞
# - 同一形式のデータセットを行方向で結合する
#   --- ｢列名｣｢データ型｣が一致していることを前提とする


# 列名が一致する場合 ---------------------------------------

# 準備
iris_1 = iris.query('species == "setosa"').head()
iris_2 = iris.query('species == "versicolor"').head()
iris_3 = iris.query('species == "virginica"').head()

# データ結合
# --- 全ての列を結合
# --- インデックスをリセット
pd.concat([iris_1, iris_2, iris_3])
pd.concat([iris_1, iris_2, iris_3], ignore_index=True)


# 列名が異なる場合 -----------------------------------------

# 準備
iris_1 = iris.query('species == "setosa"').rename(columns={'species': 'species1'}).head()
iris_2 = iris.query('species == "versicolor"').rename(columns={'species': 'species2'}).head()
iris_3 = iris.query('species == "virginica"').rename(columns={'species': 'species3'}).head()

# データ結合
# --- 全ての列を結合
# --- 一致列のみ結合
pd.concat([iris_1, iris_2, iris_3])
pd.concat([iris_1, iris_2, iris_3], join='inner')


# 2 列方向のデータ結合 -----------------------------------------------------------

# ＜ポイント＞
# - インデックスが一致していることを前提とする


# インデックスが一致する -------------------------------------------------

# 準備
iris_sl = iris[['sepal_length']]
iris_sw = iris[['sepal_width']]
iris_pl = iris[['petal_length']]
iris_pw = iris[['petal_width']]

# データ結合
pd.concat([iris_sl, iris_sw, iris_pl, iris_pw], axis=1)


# インデックスが異なるデータ ----------------------------------------------

# 準備
iris_sl = iris[['sepal_length']].iloc[0:5, :]
iris_sw = iris[['sepal_width']].iloc[5:10, :]
iris_pl = iris[['petal_length']].iloc[10:15, :]
iris_pw = iris[['petal_width']].iloc[15:20, :]

# データ結合
# --- 全ての行を結合
pd.concat([iris_sl, iris_sw, iris_pl, iris_pw], axis=1)

# データ結合
# --- インデックスをリセット
pd.concat([iris_sl.reset_index(),
           iris_sw.reset_index(),
           iris_pl.reset_index(),
           iris_pw.reset_index()], axis=1)


# インデックスが一部共通するデータ ----------------------------------------------

# 準備
iris_sl = iris[['sepal_length']].iloc[0:5, :]
iris_sw = iris[['sepal_width']].iloc[0:10, :]
iris_pl = iris[['petal_length']].iloc[0:15, :]
iris_pw = iris[['petal_width']].iloc[0:20, :]

# データ結合
# --- 全ての行を結合
# --- 一致行のみ結合
pd.concat([iris_sl, iris_sw, iris_pl, iris_pw], axis=1)
pd.concat([iris_sl, iris_sw, iris_pl, iris_pw], axis=1, join='inner')


# 3 mergeによるテーブル結合 -----------------------------------------------------------------

# ＜ポイント＞
# - 単純に列同士でテーブルを結合する
#   --- joinはインデックスを用いる


# 列名が一致する場合 --------------------------------------------------------------

# 準備
ab = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                   'b': ['b_1', 'b_2', 'b_3']})
ac = pd.DataFrame({'a': ['a_1', 'a_2', 'a_4'],
                   'c': ['c_1', 'c_2', 'c_4']})

# テーブル結合
# --- 明示的に列名を指定する必要がない
ab.merge(ac, on='a')
pd.merge(ab, ac, on='a')


# 列名が一致しない場合 -------------------------------------------------------------

# 準備
ab = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                   'b': ['b_1', 'b_2', 'b_3']})
aac = pd.DataFrame({'aa': ['a_1', 'a_2', 'a_4'],
                    'c': ['c_1', 'c_2', 'c_4']})

# テーブル結合
# --- 明示的に列名を指定する必要がある
ab.merge(aac, left_on='a', right_on='aa')
pd.merge(ab, aac, left_on='a', right_on='aa')


# 結合方法の指定 -------------------------------------------------------------------

# 準備
ab = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                   'b': ['b_1', 'b_2', 'b_3']})
ac = pd.DataFrame({'a': ['a_1', 'a_2', 'a_4'],
                   'c': ['c_1', 'c_2', 'c_4']})

# 様々なデータ結合
# --- 内部結合
# --- 外部結合
# --- Left結合
pd.merge(ab, ac, on='a', how='inner')
pd.merge(ab, ac, on='a', how='outer')
pd.merge(ab, ac, on='a', how='left')


# 複数キーでの結合 ----------------------------------------------------------------

# 準備
axb = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                    'x': ['x_2', 'x_2', 'x_3'],
                    'b': ['b_1', 'b_2', 'b_3']})
axc = pd.DataFrame({'a': ['a_1', 'a_2', 'a_4'],
                    'x': ['x_1', 'x_2', 'x_2'],
                    'c': ['c_1', 'c_2', 'c_4']})

# 複数キーで結合
# --- 冗長性なし
pd.merge(axb, axc, on=['a', 'x'])

# 単一キーで結合
# --- xに冗長性が残る
pd.merge(axb, axc, on='a')


# 4 joinによるテーブル結合 ------------------------------------------------------------------

# ＜ポイント＞
# - インデックスを用いてテーブルを結合する
#   --- mergeは単純に列のみを用いる


# 列名が一致する場合 --------------------------------------------------

# 準備
ab = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                   'b': ['b_1', 'b_2', 'b_3']}).set_index('a')
ac = pd.DataFrame({'a': ['a_1', 'a_2', 'a_4'],
                   'c': ['c_1', 'c_2', 'c_4']}).set_index('a')

# メソッドによる結合
ab.join(ac, on='a')


# インデクス名が一致しない場合 -----------------------------------------

# 準備
ab = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                   'b': ['b_1', 'b_2', 'b_3']}).set_index('a')
aac = pd.DataFrame({'aa': ['a_1', 'a_2', 'a_4'],
                    'c': ['c_1', 'c_2', 'c_4']}).set_index('aa')

# メソッドによる結合
ab.join(aac, on='a')
ab.join(aac, on='a')


# 結合方法の指定 ------------------------------------------------------

# 準備
ab = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                   'b': ['b_1', 'b_2', 'b_3']}).set_index('a')
ac = pd.DataFrame({'a': ['a_1', 'a_2', 'a_4'],
                   'c': ['c_1', 'c_2', 'c_4']}).set_index('a')

# インデックスで結合
# --- 内部結合
# --- 外部結合
# --- Left結合
ab.join(aac, on='a', how='inner')
ab.join(aac, on='a', how='outer')
ab.join(aac, on='a', how='left')


# 複数キーでの結合 ----------------------------------------------------------------

# 準備
axb = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                    'x': ['x_2', 'x_2', 'x_3'],
                    'b': ['b_1', 'b_2', 'b_3']}).set_index(['a', 'x'])
axc = pd.DataFrame({'a': ['a_1', 'a_2', 'a_4'],
                    'x': ['x_1', 'x_2', 'x_2'],
                    'c': ['c_1', 'c_2', 'c_4']}).set_index(['a', 'x'])

# 複数キーで結合
# --- mergeと異なりインデックスは全て指定しなければならない
axb.join(axc, on=['a', 'x'])
