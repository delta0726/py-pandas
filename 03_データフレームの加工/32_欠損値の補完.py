"""
Project   : Pandasのメモ
Chapter   : 03 データフレームの加工
Title     : 32 欠損値の補完
Date      : 2023/03/05
"""


# ＜目次＞
# 0 準備
# 1 特定の値で補完
# 2 集計値で補完
# 3 グループ単位の集計値で補完
# 4 直前値/直後値で補完


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


# 1 特定の値で補完 ------------------------------------------------------------------

# 一律にゼロを指定
iris_nan.fillna(value=0)

# 列ごとに数値を指定
iris_nan.fillna(value={'sepal_length': 0, 'sepal_width': 1})


# 2 集計値で補完 -----------------------------------------------------------------------

# 全ての列平均値で補完
iris_nan.fillna(iris_nan.mean())

# 特定列を平均値で補完
iris_nan.assign(sepal_length=lambda x: x.fillna(x['sepal_length'].mean()))


# 3 グループ単位の集計値で補完 -------------------------------------------------------------

# グループ単位の平均値
iris_nan.assign(sepal_length=lambda x: x['sepal_length']
                .fillna(x.groupby('species')['sepal_length'].transform('mean')))


# 4 直前値/直後値で補完 ------------------------------------------------------------------

# データフレーム全体の補完
# --- フロント・フィル
# --- バック・フィル
# --- 全ての欠損値を補完
iris_nan.fillna(method='ffill')
iris_nan.fillna(method='bfill')
iris_nan.fillna(method='ffill').fillna(method='bfill')

# 独自のメソッドも存在する
iris_nan.ffill()
iris_nan.bfill()
iris_nan.ffill().bfill()

# 特定列の補完
iris_nan.fillna(method="ffill")


# 列単位の補完
iris_nan.assign(sepal_length=lambda x: x['sepal_length'].ffill())
iris_nan.assign(sepal_length=lambda x: x['sepal_length'].bfill())
iris_nan.assign(sepal_length=lambda x: x['sepal_length'].ffill().bfill())
