"""
Project   : Pandasのメモ
Chapter   : 03 データフレームの加工
Title     : 21 行のインデックス操作
Date      : 2023/02/22
"""


# ＜目次＞
# 0 準備
# 1 インデックスの設定
# 2 インデックスのリセット
# 3 マルチインデックスの追加/再設定
# 4 マルチインデックスのレベル変更


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns


# データロード
iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')


# 1 インデックスの設定 -------------------------------------------------------------

# ＜ポイント＞
# - インデックス設定は単独/複数のどちらも可能
#   --- 複数の場合はマルチインデックスと呼ばれる


# インデックスの設定
iris.set_index('species')

# マルチインデックスの設定
tips.set_index(['day', 'time'])


# 2 インデックスのリセット ----------------------------------------------------------

# 準備：インデックスの設定
tips_temp = tips.set_index(['day', 'time'])

# インデックスのリセット
tips_temp.reset_index()


# 3 マルチインデックスの追加/再設定 --------------------------------------------------

# インデックスの追加
# --- append引数をTrueにする（Falseだとtimeだけがインデックスになる）
tips.set_index('day').set_index('time', append=True)

# インデックスの再設定
# --- リセットしてから再設定する方法もある
tips.reset_index().set_index(['day', 'time'], append=True)


# 4 マルチインデックスのレベル変更 ----------------------------------------------------

# ＜ポイント＞
# - インデックスのレベル変更は2つの入れ替えのみ
#   --- 複雑な入れ替えの場合はリセット＆再設定の方が早い

# 2レベルの変更
tips_idx2 = tips.set_index(['day', 'time'])
tips_idx2.swaplevel()

# 3レベルの変更
# --- 1つずつしか変換できない
tips_idx3 = tips.set_index(['day', 'time', 'sex'])
tips_idx3.swaplevel(i='sex', j='day')

# 3レベルの変更
# --- 1つずつしか変換できない
# --- リセットしてから再設定する方法もある
tips_idx3.reset_index().set_index(['sex', 'time', 'day'])
