# ******************************************************************************
# Project   : Pandasのメモ
# Chapter   : 03 データフレームの加工
# Theme     : 05 列のつい以下
# Date      : 2023/02/17
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 assignメソッドによる列追加
# 2 元データを更新しながら列追加
# 3 insertメソッドによる列追加


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns

# データロード
iris = sns.load_dataset('iris')


# 2 assignメソッドによる列追加 ------------------------------------------------------

# ＜ポイント＞
# - 元のデータが更新されないのでメソッドチェーンに適している
# - 追加する場合は一番最後の列に追加される


# 単純な列追加
# --- スカラー
# --- Pandas Series
iris.assign(other='test',
            species2=lambda x: x['species'])

# 列を加工して追加
iris.assign(species3=lambda x: x['species'].str.upper())

# 既存列を更新
iris.assign(sepal_length=lambda x: 1 / x['sepal_length'])


# 2 元データを更新しながら列追加 -----------------------------------------------------

# ＜ポイント＞
# - 元のデータを更新するという点で使い勝手が悪いが、よく見かける方法

# 列の追加
# --- スカラー
# --- Pandas Series
iris['other'] = 'test'
iris['species2'] = iris['species']


# 3 insertメソッドによる列追加 -----------------------------------------------------

# ＜ポイント＞
# - insertメソッドは任意の場所に列を追加する
# - 元のデータセットを更新する
#   --- 戻り値がないため、メソッドチェーンには使えない


# データ準備
df_temp = iris.filter(['sepal_length', 'species'])

# 列の追加
df_temp.insert(loc=1, column='test', value=1 / df_temp['sepal_length'])

# 列の確認
df_temp
df_temp.info()
