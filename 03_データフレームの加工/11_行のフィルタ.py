# ******************************************************************************
# Project   : Pandasのメモ
# Chapter   : 03 データフレームの加工
# Title     : 11 行のフィルタ
# Date      : 2023/02/18
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 レコードの条件判定
# 2 フィルタの基本動作
# 3 理論演算子を用いた抽出
# 4 数値の範囲抽出
# 3 重複行の操作
# 4 数値の範囲抽出
# 5 文字列の部分一致の抽出
# 6 文字列の複数一致の抽出
# 7 queryメソッドにおける変数の扱い


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns


# データロード
iris = sns.load_dataset('iris')


# 1 レコードの条件判定 -------------------------------------------------------------

# ＜ポイント＞
# - 条件判定は列ごとに行うため、シリーズ単位でおこなわれる
#   --- True/Falseが戻り値となる
#   --- 戻り値がPandas Seriesというのが重要（シングルブラケットが付いた状態）

# 条件判定
iris["species"] == "virginica"


# 2 フィルタの基本動作 ----------------------------------------------------------------

# ＜ポイント＞
# - Pandasでは｢フィルタ(filter)｣は列抽出で使われるキーワード
#   --- SQLなど一般的にはレコード抽出の意味なので、以降は｢レコード抽出｣の意味で使う


# ブラケットによるフィルタ
# --- ラムダ式の結果はシリーズで返される
# --- シリーズは既にシングルブラケットのため、ブラケット1つで抽出できる
iris[lambda x: x["species"] == "virginica"]

# locプロパティによるフィルタ
# --- ブラケット内では行のみ指定すれば抽出できる（列は省略可能）
iris.loc[lambda x: x["species"] == "virginica"]
iris.loc[lambda x: x["species"] == "virginica", :]

# queryメソッドによるフィルタ
# --- 数値ならそのまま指定
# --- 列参照の場合もそのまま指定
# --- 文字列ならダブルクオーテーションで指定（外は必然的にシングルクオーテーション）
iris.query('petal_length > 5')
iris.query('petal_length < sepal_length * 0.8')
iris.query('species == "virginica"')


# 3 理論演算子を用いた抽出 --------------------------------------------------------------

# ＜ポイント＞
# - locプロパティを用いるとフィルタを行うことが可能
#   --- ラムダ式の使用が前提となる

# AND条件の抽出
iris[lambda x: (x["species"] == 'virginica') & (x["sepal_length"] >= 7)]
iris.query('species == "virginica" & sepal_length >= 7')

# OR条件の抽出
iris[lambda x: (x["species"] == 'virginica') | (x["sepal_length"] >= 7)]
iris.query('species == "virginica" | sepal_length >= 7')

# NOT抽出
# --- !=
# --- ~
iris[lambda x: x["species"] != "virginica"]
iris[lambda x: ~(x["species"] == "virginica")]
iris.query('species != "virginica"')
iris.query('(species == "virginica")')


# 4 数値の範囲抽出 ----------------------------------------------------------------------

# betweeenメソッド
iris[lambda x: x["sepal_length"].between(6.5, 7.2)]
iris.query('6.5 < sepal_length <= 7.2')

# AND抽出
# --- 次のようには書けない（6.5 < x["sepal_length"] < 7.2）
iris[lambda x: (6.5 < x["sepal_length"]) & (x["sepal_length"] < 7.2)]
iris.query('Sepal_Length > 5 and species == "setosa"')


# 5 文字列の部分一致の抽出  -----------------------------------------

# 先頭一致の抽出
iris[lambda x: x["species"].str.startswith('vir')]
iris.query('species.str.startswith("vir")', engine='python')

# 後方一致の抽出
iris[lambda x: x["species"].str.endswith('ica')]
iris.query('species.str.endswith("ica")', engine='python')

# 部分一致の抽出
iris[lambda x: x["species"].str.contains('irginic')]
iris.query('species.str.contains("irginic")', engine='python')

# 正規表現による抽出
iris[lambda x: x.species.str.match('.*i.*a')]
iris.query('species.str.match(".*i.*a")', engine='python')


# 6 文字列の複数一致の抽出 --------------------------------------------

# ＜ポイント＞
# - "isin"は"is in"と読む
# - Pandas Seriesに対して要素が含まれているかを判定する
# - isinはブラケット抽出、in演算子はqueryメソッドと相性が良い


# isinの動作
# --- シリーズに対して含まれているかどうかを判定
# --- チルダ(~)で判定を反転させることも可能
iris['species'].isin(['setosa', 'virginica'])
~iris['species'].isin(['setosa', 'virginica'])

# isinによる抽出
# --- 一致抽出
# --- 不一致抽出
iris[lambda x: x['species'].isin(['setosa', 'virginica'])]
iris[lambda x: ~x['species'].isin(['setosa', 'virginica'])]

# in演算子による抽出
# --- 一致抽出
# --- 不一致抽出
iris.query('species in ["setosa", "virginica"]')
iris.query('species not in ["setosa", "virginica"]')


# 7 queryメソッドにおける変数の扱い -----------------------------------

# ＜ポイント＞
# - queryメソッドでは条件を文字列で指定するので、変数をパラメータとする際は以下の記法を用いる
#   --- @変数による指定
#   --- f-stringによる条件抽出

# @変数による指定
# --- 単一条件
# --- 複数条件
x1 = "setosa"
x2 = ["setosa", "virginica"]
iris.query('species == @x1')
iris.query('species in @x2')

# f-stringによる条件抽出
# --- 単一条件
# --- 複数条件
x1 = "setosa"
x2 = ["setosa", "virginica"]
iris.query(f'species == "{x1}"')
iris.query(f'species in {x2}')
