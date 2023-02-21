# ******************************************************************************
# Project   : Pandasのメモ
# Chapter   : 03 データフレームの加工
# Title     : 14 行のユニーク化
# Date      : 2023/02/18
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 重複行の削除
# 2 重複行のみ抽出


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns

# データロード
iris = sns.load_dataset('iris')


# 1 重複行の削除 ---------------------------------------------------------------------

# 全レコードを対象
# --- irisには1レコードだけ重複がある
iris.drop_duplicates()

# 列を指定
iris.filter(['species']).drop_duplicates(subset=['species'])


# 2 重複行のみ抽出 -------------------------------------------------------------------

# ＜ポイント＞
# - duplicatedメソッドを用いると重複行をTRUE/FALSEで判定することができる


# 重複行の判定
# --- duplicatedメソッドの抽出
iris.duplicated(keep=False)

# 重複行のみ抽出
# --- irisには1レコードだけ重複がある
iris[lambda x: x.duplicated(keep=False)]
iris.loc[lambda x: x.duplicated(keep=False), :]
