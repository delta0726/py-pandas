# ******************************************************************************
# Project   : Pandasのメモ
# Chapter   : 02 シリーズの操作
# Title     : 02 シリーズの結合
# Date      : 2023/02/09
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 appendによる結合
# 2 concatによる結合


# 0 準備 ---------------------------------------------------------------------------

# ライブラリ
import pandas as pd


# データ準備
# --- Series_1
list1 = [9000, 4000, 200, 12000]
index1 = ["P001", "P002", "P003", "P004"]
ser1 = pd.Series(data=list1, index=index1)
ser1

# データ準備
# --- Series_2
list2 = [1000, 31000, 60]
index2 = ["P005", "P006", "P007"]
ser2 = pd.Series(data=list2, index=index2)
ser2

# データ準備
# --- Series_3
list3 = [10000, 3000, 6000]
index3 = ["P008", "P009", "P010"]
ser3 = pd.Series(data=list3, index=index3)
ser3


# 1 appendによる結合 ---------------------------------------------------------------

# ＜ポイント＞
# - appendメソッドを使ってシリーズを結合


# シリーズの結合
# --- インデックスを維持
# --- インデックスを初期化（reset_indexと同じ）
ser1.append(ser2, ignore_index=False)
ser1.append(ser2, ignore_index=True)

# 複数のシリーズを追加
ser1.append(ser2, ignore_index=False)\
    .append(ser3, ignore_index=False)


# 2 concatによる結合 ---------------------------------------------------------------

# ＜ポイント＞
# - pd.concat関数を使ってシリーズを結合


# シリーズの結合
# --- インデックスを維持
# --- インデックスを初期化（reset_indexと同じ）
pd.concat([ser1, ser2], ignore_index=False)
pd.concat([ser1, ser2], ignore_index=True)

# シリーズの結合
# --- 2つの結合
# --- 3つ以上の結合
pd.concat([ser1, ser2])
pd.concat([ser1, ser2, ser3])
