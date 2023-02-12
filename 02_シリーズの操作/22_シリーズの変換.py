# ******************************************************************************
# Project   : Pandasのメモ
# Chapter   : 02 シリーズの操作
# Theme     : 22 シリーズの変換
# Date      : 2023/02/09
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 データフレームの列に変換
# 2 データフレームの行に変換
# 3 辞書型に変換
# 4 リスト型に変換
# 5 ndarrayに変換


# 0 準備 ---------------------------------------------------------------------------

# ライブラリ
import numpy as np
import pandas as pd


# 1 データフレームの列に変換 -----------------------------------------------------------

# ＜ポイント＞


# データフレーム変換
# --- 列名を事前に追加
ser11 = pd.Series(data=[1, 2, 3], index=['A', 'B', 'C'], name='col1')
pd.DataFrame(ser11)

# データフレーム変換
# --- 列名を事後で追加
ser12 = pd.Series(data=[1, 2, 3], index=['A', 'B', 'C'])
pd.DataFrame(ser12).set_axis(['col1'], axis=1)


# 2 データフレームの行に変換 --------------------------------------------------------


# データフレームに行として変換
# --- 列名を事前に追加
ser21 = pd.Series(data=[1, 2, 3], index=['A', 'B', 'C'], name='row1')
pd.DataFrame([ser21])

# データフレームに行として変換
# --- 列名を事後で追加
ser22 = pd.Series(data=[1, 2, 3], index=['A', 'B', 'C'])
pd.DataFrame([ser22]).set_axis(['col1'], axis=0)


# 3 辞書型に変換 ----------------------------------------------------------------------

# 辞書型に変換
ser_dict = pd.Series(data=[1, 2, 3], index=['A', 'B', 'C'], name='col1')
ser_dict.to_dict()


# 4 リスト型に変換 ---------------------------------------------------------------------

# データ準備
ser_list = pd.Series(data=[1, 2, 3], index=['A', 'B', 'C'], name='col1')

# リストに変換
# --- インデックスは落ちてしまう
ser_list.tolist()

# リストに変換
# --- インデックスを保持
list(zip(ser_list, ser_list.index))

# 内包表記で変換
[idx for idx, val in enumerate(ser_list)]
[val for idx, val in enumerate(ser_list)]
[(val, idx) for idx, val in enumerate(ser_list)]


# 5 ndarrayに変換 ---------------------------------------------------------------------

# ndarrayに変換
ser_array = pd.Series(data=[1, 2, 3], index=['A', 'B', 'C'], name='col1')
ser_array.to_numpy()
