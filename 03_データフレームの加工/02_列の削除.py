# ******************************************************************************
# Project   : Pandasのメモ
# Chapter   : 03 データフレームの加工
# Theme     : 02 列の削除
# Date      : 2023/02/15
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 列名を指定して列削除（単独行）
# 2 列名を指定して列削除（複数行）
# 3 列名パターンで列削除
# 4 データ型で列削除
# 5 全てNaNの列の削除


# 0 準備 ---------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import numpy as np
import seaborn as sns


# データロード
iris = sns.load_dataset('iris')


# 1 列名を指定して列削除（単独行） ------------------------------------------------------

# ＜ポイント＞
# - ｢副作用なし｣と｢副作用あり｣の2つの方法がある
#   --- 通常は｢副作用なし｣を使う


# 副作用なし
# --- 元のデータセットが変化しない（inplace引数をTrueにすると｢副作用あり｣となる）
# --- columns引数で列を指定する
# --- 第1引数のlabels引数を使用する場合はaxis=1とする（axis引数のデフォルトは0）
iris.drop(columns="species")
iris.drop(labels="species", axis=1)

# 副作用あり
# --- del文をつかうので、iris変数が直接更新される
del iris["species"]
print(iris)

# 副作用あり
# --- popメソッドは単一行のみに対応
# --- iris変数が直接更新される
# --- 戻り値のiris_newにはspeciesが残る
iris_new = iris.pop("species")
print(iris)
print(iris_new)


# 2 列名を指定して列削除（複数行） ------------------------------------------------------

# 複数列の削除
# --- 元のデータセットが変化しない（inplace引数をTrueにすると｢副作用あり｣となる）
# --- columns引数で列を指定する
# --- 第1引数のlabels引数を使用する場合はaxis=1とする（axis引数のデフォルトは0）
iris.drop(labels=["sepal_length", "species"], axis=1)
iris.drop(columns=["sepal_length", "species"])

# 副作用あり
# --- del文をつかうので、iris変数が直接更新される
del iris["species"], iris["sepal_length"]
print(iris)


# 3 列名パターンで列削除 ---------------------------------------------------------

# ＜ポイント＞
# - パターン検索する場合はチルダ(~)を用いて真偽を反転させて選択する
# - 正規表現を用いると｢含まない｣も柔軟に表現できる


# 先頭不一致
# --- 真偽の反転を活用
iris.loc[:, lambda x: ~x.columns.str.startswith("sepal")]

# 後方不一致
iris.loc[:, lambda x: ~x.columns.str.startswith("width")]

# 部分不一致
iris.loc[:, lambda x: ~x.columns.str.contains("wid")]


# 4 データ型で列削除 --------------------------------------------------------------

# 数値列を削除
iris.select_dtypes(exclude=float)

# 文字列を削除
iris.select_dtypes(exclude=object)

# 参考：データ型の確認
iris.dtypes


# 5 全てNaNの列の削除 ---------------------------------------------------------------

# ＜ポイント＞
# - 全てNaNの列を削除する場合はdropna()のaxis引数を1にして適用する


# 準備：全てNaNの列を作成
iris_na = iris.assign(Col_NaN=np.nan)

# 全てNaNの列を削除
iris_na.dropna(axis=1)
