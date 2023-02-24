# ******************************************************************************
# Project   : Pandasのメモ
# Chapter   : 03 データフレームの加工
# Title     : 32 欠損値の補完
# Date      : 2023/02/25
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 データフレーム全体を統一的に補完
# 2 列単位で補完
# 3 集計値で補完
# 4 グループ単位の集計値で補完


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import numpy as np
import seaborn as sns


# データロード
iris = sns.load_dataset('iris')

# データ加工
# --- NaNを追加
iris_num = iris.drop(columns='species').mask(lambda x: np.random.random(x.shape) < .3)
iris_lab = iris.filter(['species'])
iris_nan = pd.concat([iris_num, iris_lab], axis=1)


# 1 データフレーム全体を補完 ----------------------------------------------------------

# フロント・フィル
iris_nan.ffill()

# バック・フィル
iris_nan.bfill()

# 全ての欠損値を補完
iris_nan.ffill().bfill()


# 2 列単位で補完 -----------------------------------------------------------------------

# フロント・フィル
iris_nan.assign(sepal_length=lambda x: x['sepal_length'].ffill())

# バック・フィル
iris_nan.assign(sepal_length=lambda x: x['sepal_length'].bfill())

# 全ての欠損値を補完
iris_nan.assign(sepal_length=lambda x: x['sepal_length'].ffill().bfill())


# 3 集計値で補完 -----------------------------------------------------------------------

# データフレーム全体の平均値
iris_nan.assign(sepal_length=lambda x: x.fillna(x['sepal_length'].mean()))


# 4 グループ単位の集計値で補完 -------------------------------------------------------------

# グループ単位の平均値
iris_nan.assign(sepal_length=lambda x: x['sepal_length']
                .fillna(x.groupby('species')['sepal_length'].transform('mean')))

