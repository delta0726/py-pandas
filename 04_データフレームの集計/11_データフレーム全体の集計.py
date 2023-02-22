# ******************************************************************************
# Project   : Pandasのメモ
# Chapter   : 04 データフレームの集計
# Theme     : 11 データフレーム全体の集計
# Date      : 2023/02/23
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 データ数のカウント
# 2 列ごとのユニークデータをカウント
# 3 全ての列を集計
# 4 データ型で列を選択して集計
# 5 複数パターンの集計


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import numpy as np
import pandas as pd
import seaborn as sns


# データロード
iris = sns.load_dataset('iris')

# データ加工
# --- NaNを追加
iris_nan = iris.mask(np.random.random(iris.shape) < .1)


# 1 データ数のカウント --------------------------------------------------------------

# ＜ポイント＞
# - 有効データをカウントする

# 列のカウント
# --- NaNなしのデータ
# --- NaNありのデータ
iris.count()
iris_nan.count()

# 行のカウント
# --- NaNなしのデータ
# --- NaNありのデータ
iris.count(axis=1)
iris_nan.count(axis=1)


# 2 列ごとのユニークデータをカウント ----------------------------------------------------

# 列ごとのユニーク要素数を一括カウント
iris.nunique()

# カテゴリ変数のカウント
# --- グループ化しないでカウント
iris[['species']].value_counts()


# 3 全ての列を集計 -----------------------------------------------------------------

# 集計関数を直接適用
# --- 数値は合計、文字列は結合（意図しない集計）
# --- 集計関数の場合は数値列のみ
iris.sum()
iris.mean()


# 4 データ型で列を選択して集計 -------------------------------------------------------

# 集計関数を直接適用
# --- 数値列のみ
iris.select_dtypes(include='float').sum()
iris.select_dtypes(exclude='object').mean()
iris.select_dtypes(include='object').count()


# 5 複数パターンの集計 ----------------------------------------------------------------

# ＜ポイント＞
# - 複数パターンで集計する場合はaggregateメソッドに集計関数をリストで渡すことで実現する
#   --- agg()はaggregate()のエイリアス

# 全列を集計
iris.select_dtypes(include='float').agg([np.sum, np.mean, np.std])

# 列を指定して集計
iris.agg({'sepal_length': [np.sum, np.std],
          'sepal_width': [np.sum, np.mean]})

# aggregateメソッドによる複数集計
# --- aggメソッドと同様
iris.aggregate({'sepal_length': [np.sum, np.std],
                'sepal_width': [np.sum, np.mean]})


