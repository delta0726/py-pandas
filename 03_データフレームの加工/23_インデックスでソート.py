"""
Project   : Pandasのメモ
Chapter   : 03 データフレームの加工
Title     : 23 インデクスでソート
Date      : 2023/02/22
"""


# ＜目次＞
# 0 準備
# 1 インデックスの構造
# 2 locによるフィルタ
# 3 pd.IndexSliceによるフィルタ
# 4 xsメソッドによるフィルタ


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns


# データロード
iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')

# データ準備
# --- インデックスの追加
tips_idx = tips.set_index(['day', 'sex', 'time'])


# 1 インデックスの構造 ------------------------------------------------------------

# ＜ポイント＞
# - 単独インデックスの場合はリスト
# - マルチインデックスの場合はリスト＆タプル

# インデックスの確認
tips_idx.index
tips_idx.index.unique()


# 2 インデックスでソート -------------------------------------------------------------

# ＜ポイント＞
# -


# 全体をソート
tips_idx.sort_index()

# レベル指定でソート
tips_idx.sort_index(level='day')
