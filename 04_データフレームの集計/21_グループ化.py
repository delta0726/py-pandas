"""
Project   : Pandasのメモ
Chapter   : 04 データフレームの集計
Theme     : 21 グループ化
Date      : 2023/02/24
"""


# ＜目次＞
# 0 準備
# 1 グループ化
# 2 グループ化の解除
# 3 グループ属性の確認


# 0 準備 ---------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns

# データロード
iris = sns.load_dataset('iris')


# 1 グループ化 ---------------------------------------------------------------------

# グループ化
# --- 独自のオブジェクトが生成される（データは出力されない）
# --- pandas.core.groupby.generic.DataFrameGroupBy
iris.groupby(['species'])


# 2 グループ化の解除 -----------------------------------------------------------------

# ＜ポイント＞
# - グループ化を明示的に解除するメソッドは存在しない
#   --- 集計してからreset_index()を適用するのがセオリー
#   --- 代替的な方法として以下の操作がある

# 準備：グループ化
iris_grp = iris.groupby(['species'])

# グループ化の解除
iris_grp.apply(lambda x: x.reset_index(drop=True))

# 元データの抽出
iris_grp.obj


# 3 グループ属性の確認 ---------------------------------------------------------------

# 準備：グループ化
iris_grp = iris.groupby(['species'])

# グループ数
iris_grp.ngroups

# グループごとのレコード数
# --- グループ別
# --- 特定要素を抽出
iris_grp.size()
iris_grp.size()['versicolor']

# グループ要素のカウント
# --- 総数
# --- ユニークレコード数
iris_grp.count()
iris_grp.nunique()

# データタイプ
# ---グループ要素ごとのデータ型
iris_grp.dtypes

# インデックス情報
# --- グループごとのインデックスを辞書形式で取得
# --- グループごとのインデックスをNumpyのArray形式で取得
iris_grp.groups
iris_grp.indices

# グループキーの取得
iris_grp.groups.keys()
