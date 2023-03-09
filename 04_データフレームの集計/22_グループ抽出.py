"""
Project   : Pandasのメモ
Chapter   : 04 データフレームの集計
Theme     : 22 グループ抽出
Date      : 2023/03/10
"""


# ＜目次＞
# 0 準備
# 1 グループデータの抽出
# 2 グループフィルタ
# 3 グループ集計を伴うグループ抽出


# 0 準備 ---------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns

# データロード
iris = sns.load_dataset('iris')


# 1 グループデータの抽出 --------------------------------------------------------------

# レコード抽出
iris.groupby(['species']).head()
iris.groupby(['species']).tail()
iris.groupby(['species']).first()
iris.groupby(['species']).last()
iris.groupby(['species']).nth([5, 10])
iris.groupby(['species']).nth([5, 10])
iris.groupby(['species']).quantile(0.3)
iris.groupby(['species']).sample(5)


# 2 グループフィルタ ---------------------------------------------------------------

# グループ名で抽出
iris.groupby(['species']).get_group('versicolor')

# 複数グループの抽出
# --- get_groupでの抽出はできない
iris.loc[lambda x: x['species'].isin(['setosa', 'versicolor'])]


# 3 グループ集計を伴うグループ抽出-------------------------------------------------------

# 条件抽出
# --- グループごとの最大値が6以上のグループを抽出
iris.groupby(['species']).filter(lambda x: x['sepal_length'].max() >= 6)

# グループ集計
# --- グループごと平均値を上回るレコードを抽出
iris.groupby(['species']).apply(lambda x: x[x['sepal_length'] >= x['sepal_length'].mean()])
