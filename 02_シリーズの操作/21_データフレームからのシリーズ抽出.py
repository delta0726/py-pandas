"""
Project   : Pandasのメモ
Chapter   : 02 シリーズの操作
Theme     : 21 データフレームからのシリーズ抽出
Date      : 2023/02/09
"""

# ＜目次＞
# 0 準備
# 1 列をシリーズとして抽出
# 2 行をシリーズとして抽出


# 0 準備 ------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import numpy as np
import seaborn as sns


# データセットの準備
iris = sns.load_dataset('iris')


# 1 列をシリーズとして抽出 ---------------------------------------------------------

# ＜ポイント＞
# - ドットで取得する方法はコラム名にドットが含まれない場合しか使えない
# - [[]]で取得するとデータフレームになる


# ブラケットで指定
# --- 最もベーシック
iris['sepal_length']

# locプロパティを使用
# --- 列名を指定
# --- 列インデックスを指定
iris.loc[:, 'sepal_length']
iris.iloc[:, 0]

# シリーズ作成
# --- コラム名にドットが含まれると使用不可
iris.sepal_length


# 2 行をシリーズとして抽出 ---------------------------------------------------------

# データ準備
iris2 = iris\
    .assign(row_num=lambda x: np.arange(len(x)))\
    .assign(row_num=lambda x: 'row_' + x['row_num'].astype(str))\
    .set_index('row_num')

# インデックスがない場合
# --- 列名を指定（インデックスが数値）
# --- 列インデックスを指定
iris.loc[0, :]
iris.iloc[0, :]

# インデックスがある場合
# --- 列名を指定
# --- 列インデックスを指定
iris2.loc['row_1', :]
iris.iloc[0, :]
