# ******************************************************************************
# Project   : Pandasのメモ
# Chapter   : 03 データフレームの加工
# Theme     : 05 列の分解・結合
# Date      : 2023/02/16
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 データ結合
# 2 分割パーツを明示的に列追加


# 0 準備 ----------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns


# データロード
tips = sns.load_dataset('tips')


# 1 データ結合 -----------------------------------------------------------------

# ＜ポイント＞
# - データの結合は基本的にassign()でjoinメソッドを使えば実現できる
#   --- セパレータは基本的にアンダースコアが良い

# データ結合
tips_concat = tips \
    .assign(concat="_".join(['smoker', 'day', 'time'])) \
    .filter(['concat'])

# 確認
print(tips_concat)


# 2 単純な列分解 -------------------------------------------------------

# ＜ポイント＞
# - 列を直接的にセパレータで分解する

# ＜手順＞
# - 1列を独立したデータフレームにする
# - セパレータで列を分解＆列名設定
# - 必要に応じて元のデータセットと結合

# 指定列の分解
# --- 元の列は維持されない
temp_df = tips_concat['concat']\
    .str.split('_', expand=True)\
    .set_axis(['smoker', 'day', 'time'], axis=1)

# 元の列が必要なら結合
pd.concat([tips_concat, temp_df], axis=1)


# 2 分割パーツを明示的に列追加 --------------------------------------------------

# ＜ポイント＞
# - パーツごとに追加するかどうかを選択することができる

# 作業用データフレームを作成して分割
temp_df = tips_concat['concat'].str.split('_', expand=True)

# 元のデータフレームに追加
tips_concat\
    .assign(smoker=temp_df[0])\
    .assign(day=temp_df[1])\
    .assign(time=temp_df[2])

# パイプラインのみで結合
tips_concat\
    .assign(smoker=lambda x: x['concat'].str.split('_', expand=True)[0])\
    .assign(day=lambda x: x['concat'].str.split('_', expand=True)[1])\
    .assign(time=lambda x: x['concat'].str.split('_', expand=True)[2])
