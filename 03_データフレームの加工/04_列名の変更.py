"""
Project   : Pandasのメモ
Chapter   : 03 データフレームの加工
Theme     : 04 列名の変更
Date      : 2023/02/15
"""


# ＜目次＞
# 0 準備
# 1 単一列の列名変更
# 2 複数列の列名変更
# 3 列名のパターン変更
# 4 列名の再定義


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns

# データロード
iris = sns.load_dataset('iris')

# その他のデータセット
iris_dot = iris.rename(columns=lambda x: x.replace('_', '.'))

# 1 単一列の列名変更 --------------------------------------------------------------

# ＜ポイント＞
# - renameメソッドを使って辞書形式で{'旧名称':'新名称'}を指定する
# - dict()を用いることもできるが、列名にドット(.)が含まれるとエラーになる

# 単一列の列名変更
# --- 列名にドットが含まれない場合
iris.rename(columns={'sepal_length': 'SL'})
iris.rename(columns=dict(sepal_length='SL'))

# 単一列の列名変更
# --- 列名にドットが含まれる場合は使えない（sepal.lengthにクオテーションを付けないため）
# iris_dot.rename(columns=dict(sepal.length='SL'))


# 2 複数列の列名変更 ---------------------------------------------------------------

# 複数列の列名変更
# --- 演算子で辞書を作成
iris.rename(columns={'sepal_length': 'SL', 'sepal_width': 'SW',
                     'petal_length': 'PL', 'petal_width': 'PW'})

# 複数列の列名変更
# --- dict()で辞書を作成
iris.rename(columns=dict(sepal_length='SL', sepal_width='SW',
                         petal_length='PL', petal_width='PW'))


# 3 列名のパターン変更 -------------------------------------------------------------

# ＜ポイント＞
# - 文字列のメソッドを活用して列名を変更する
#   --- よく使う方法


# 列名を大文字に変換
iris.rename(columns=str.upper)
iris.rename(columns=lambda x: x.upper())

# 列名の一部を置換
iris.rename(columns=lambda x: x.replace('.', '_').title())
iris.rename(columns=lambda x: x.replace(".", "_"))

# データフレームの属性を直接変更
temp_df = iris.copy()
temp_df.columns = iris.columns.str.upper()
iris.columns
temp_df.columns


# 4 列名の再定義 -------------------------------------------------------------------

# ＜ポイント＞
# - 元の列名を指定する必要がない（列数と同じ要素数のリストが必要）
#   --- 現実的によく使う方法

# 列名を再定義
iris.set_axis(['SL', 'SW', 'PL', 'PW', 'SPE'], axis=1)

# 列名を大文字に変換
cols = iris.columns.str.upper()
iris.set_axis(cols, axis=1)
