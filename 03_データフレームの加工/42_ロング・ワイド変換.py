"""
Project   : Pandasのメモ
Chapter   : 03 データフレームの加工
Title     : 42 ロング・ワイド変換
Date      : 2023/02/23
"""


# ＜目次＞
# 0 準備
# 1 ロング形式に変換(meltメソッド)
# 2 ロング型に変換(stackメソッド)
# 3 ワイド型に変換(pivotメソッド)
# 4 ワイド型に変換(unstackメソッド)


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns


# ファイル読込
iris = sns.load_dataset('iris')


# 1 ロング形式に変換(meltメソッド) ----------------------------------------------------

# ＜ポイント＞
# - meltメソッドによるロング形式への変換はインデックスを使わずに行われる
# - id_vars引数で残す列を指定する（リストで指定することも可能）

# 特定列のみ残す
iris.melt(id_vars="species", var_name="key", value_name="value")

# 複数列を残す
iris.melt(id_vars=["species", "sepal_length"], var_name="key", value_name="value")


# 2 ロング型に変換(stackメソッド) -----------------------------------------------------

# ＜ポイント＞
# - stackメソッドによるロング形式への変換はインデックスを使用して行われる

# stackによる変換
# --- キーがインデックスとなる
iris.set_index(["species"]).stack()

# stackによる変換
# --- インデックスを解除する
iris.set_index(["species"]) \
    .stack() \
    .reset_index() \
    .set_axis(["species", "key", "value"], axis=1)


# 3 ワイド型に変換(pivotメソッド) -------------------------------------------------

# ＜ポイント＞
# - ロングデータで列番号を保持しておかないとワイドデータに再変換できない


# 準備：ロングデータの作成
# --- ワイド変換のため列番号を保持しておく（reset_index）
iris_melt = iris \
    .reset_index() \
    .melt(id_vars=["index", "species"], var_name="key", value_name="value")

# ワイドデータに変換
iris_melt \
    .pivot(index=["index", "species"], columns="key", values="value") \
    .reset_index()


# 4 ワイド型に変換(unstackメソッド) ----------------------------------------------------

# ＜ポイント＞
# - unstackを行う際には予めキーをインデックスにしておく


# 全ての列をロング/ワイド変換 --------------------------------

# 準備：ロングデータの作成
iris_stack = iris.stack()

# ワイドデータに変換
iris_stack.unstack()


# 指定列をキーとして保持 -----------------------------------

# 準備：ロング型データの作成
# --- 列番号となっているインデックスもunstackの際に使用する
iris_stack = iris.set_index("species").stack()

# インデックスの確認
# --- 既存インデックスである列番号も保持されている
iris_stack.index

# ワイド型データに変換
iris_stack.unstack(level=1)
