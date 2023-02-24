# ******************************************************************************
# Project   : Pandasのメモ
# Chapter   : 04 データフレームの集計
# Theme     : 22 グループ抽出
# Date      : 2023/02/24
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 グループデータの抽出
# 2 グループフィルタ
# 3 グループのサンプリング抽出
# 4 グループ集計を伴うレコード抽出


# 0 準備 ---------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns

# データロード
iris = sns.load_dataset('iris')


# 1 グループデータの抽出 ---------------------------------------------------------------

# ＜ポイント＞
# - groupbyオブジェクトにメソッドを適用することでデータを抽出することができる

# 準備：グループ化
iris_grp = iris.groupby(['species'])

# 先頭/末尾データの抽出
# --- グループごとに指定したレコード数
iris_grp.head()
iris_grp.tail()

# 先頭/末尾データの抽出
# --- グループごとに最初の1行のみ
iris_grp.first()
iris_grp.last()

# n行目のデータの抽出
iris_grp.nth(5)
iris_grp.nth([5, 10])


# 2 グループフィルタ ---------------------------------------------------------------

# 準備：グループ化
iris_grp = iris.groupby(['species'])

# グループ名で抽出
iris_grp.get_group('versicolor')

# 複数グループの抽出
# --- get_groupでの抽出はできない
iris.loc[lambda x: x['species'].isin(['setosa', 'versicolor'])]
pd.concat([iris_grp.get_group(name) for name in iris_grp.groups.keys()])


# 3 グループのサンプリング抽出 ---------------------------------------------------------

# サンプリング
# --- グループ単位で適用される
iris.groupby(['species']).sample(5)


# 4 グループ集計を伴うレコード抽出-------------------------------------------------------

# ＜ポイント＞
# - ラムダ式のxはいずれもグループ化されたirisである点に注意

# 条件抽出
# --- グループごとの最大値が6以上のグループを抽出
iris.groupby(['species'])\
    .filter(lambda x: x['sepal_length'].max() >= 6)

# グループ集計
# --- グループごと平均値を上回るレコードを抽出
iris.groupby(['species'])\
    .apply(lambda x: x[x['sepal_length'] >= x['sepal_length'].mean()])
