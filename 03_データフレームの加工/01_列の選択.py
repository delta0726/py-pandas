"""
Project   : Pandasのメモ
Chapter   : 03 データフレームの加工
Theme     : 01 列の選択
Date      : 2023/02/14
"""


# ＜目次＞
# 0 準備
# 1 列名による選択
# 2 インデックスによる選択
# 3 列名の一部から選択
# 4 データ型による列選択
# 5 内包表記による選択


# 0 準備 --------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns


# データ準備
iris = sns.load_dataset('iris')


# 1 列名による選択 -----------------------------------------------------------

# ＜ポイント＞
# - いづれの方法も列名をリストで渡している
# - locプロパティを使って列選択を行うのが一般的（Pythonではlocを列選択に使う人が多い）
# - SQLではfilterは｢行選択｣だが、Pandasでは｢列選択｣なので注意


# ブラケットによる選択
# --- ブラケットでリストを指定（二重のブラケット）
iris[['sepal_length', 'petal_width', 'species']]

# locプロパティによる選択
# --- 列のリストを渡す
# --- 列に｢:｣を指定すると全列を選択（使うことは少ない）
iris.loc[:, ['sepal_length', 'petal_width', 'species']]
iris.loc[:, :]

# filterによる選択
# --- 列のリストを渡す
iris.filter(['sepal_length', 'petal_width', 'species'])


# 2 インデックスによる選択 -------------------------------------------------------

# ＜ポイント＞
# - 列番号で列を選択する場合はilocプロパティを使う（iloc ⇒ Index Loc）
# - locの場合と同様に


# ilocで番号による選択
# --- DataFrame(列をリストで指定)
iris.iloc[:, [0, 2, 4]]

# データフレーム全体を指定
iris.iloc[:, :]


# 3 列名の一部から選択 -------------------------------------------------------

# ＜ポイント＞
# - ラムダ式を用いる方法とfilterメソッドを用いる方法がある
#   --- ラムダ式はstringモジュールを使って文字列を選択して列取得
#   --- fitlterメソッドは正規表現で文字列を選択して列取得


# locプロパティ
# --- 先頭一致（str.startswith）
# --- 後方一致（str.endswith）
# --- 部分一致（str.contains）
iris.loc[:, lambda x: x.columns.str.startswith("sepal")]
iris.loc[:, lambda x: x.columns.str.endswith("width")]
iris.loc[:, lambda x: x.columns.str.contains("wid")]

# filterメソッド
# --- 正規表現を用いる
# --- 先頭一致（regex="^Sepal"）
# --- 後方一致（regex="Width$"）
# --- 部分一致（like="Wid"）
iris.filter(regex="^Ssepal")
iris.filter(regex="width$")
iris.filter(like="wid")


# 4 データ型による列選択 ---------------------------------------------------------

# ＜ポイント＞
# - select_dtypeメソッドを使うと選択する列をデータ型で指定することができる


# 数値列の選択
iris.select_dtypes(include=float)

# 文字列の選択
iris.select_dtypes(include=object)

# 参考：データ型の確認
iris.dtypes


# 5 内包表記による選択 -----------------------------------------------------------

# ＜ポイント＞
# - リスト内包表記を使うことで列選択することも可能
#   --- 上記の方法で列選択が可能なのでユースケースは多くない

iris.loc[:, lambda x: [c.startswith('sepal') for c in x.columns]]
