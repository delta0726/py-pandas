"""
Project   : Pandasのメモ
Chapter   : 04 データフレームの集計
Theme     : 21 グループ化
Date      : 2023/03/09
"""


# ＜目次＞
# 0 準備
# 1 グループ化
# 2 グループ化の解除
# 3 gropubyの集計メソッド
# 4 グループ属性の確認


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


# 3 gropubyの集計メソッド -----------------------------------------------------------

# 集計
iris.groupby(['species']).sum()
iris.groupby(['species']).prod()
iris.groupby(['species']).mean()
iris.groupby(['species']).median()
iris.groupby(['species']).std()
iris.groupby(['species']).var()
iris.groupby(['species']).sem()     # 標準誤差

# データ取得
iris.groupby(['species']).head()
iris.groupby(['species']).tail()
iris.groupby(['species']).first()
iris.groupby(['species']).last()
iris.groupby(['species']).nth(2)

# カウント
iris.groupby(['species']).count()
iris.groupby(['species']).nunique()
iris.groupby(['species']).size()


# 4 グループ属性の確認 ---------------------------------------------------------------

# グループ数
iris.groupby(['species']).ngroups

# データタイプ
iris.groupby(['species']).dtypes

# インデックス情報
# --- グループごとのインデックスを辞書形式で取得
# --- グループごとのインデックスをNumpyのArray形式で取得
iris.groupby(['species']).groups
iris.groupby(['species']).indices

# グループキーの取得
iris.groupby(['species']).groups.keys()
