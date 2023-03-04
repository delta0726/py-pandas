"""
Category  : Grammar of Pandas
Chapter   : 01 基本操作
Title     : 13 学習用データセット
Date      : 2023/02/17
"""


# ＜目次＞
# 0 準備
# 1 データセット一覧
# 2 データロード


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import seaborn as sns


# 1 データセット一覧 ----------------------------------------------------------

# ＜ポイント＞
# - {seaborn}のデータセットは単純なpandas dataframeなので扱いやすい
# - GithubにはCSVデータも存在する
#   https://github.com/mwaskom/seaborn-data


# 一覧の取得
sns.get_dataset_names()


# 2 データロード --------------------------------------------------------------

# データロード
iris = sns.load_dataset('iris')

# データ確認
iris.info()
iris.columns
