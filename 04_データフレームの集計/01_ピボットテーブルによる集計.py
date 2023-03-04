"""
Project   : Pandasのメモ
Chapter   : 04 データフレームの集計
Theme     : 01 ピボットテーブルによる集計
Date      : 2023/02/23
"""


# ＜目次＞
# 0 準備
# 1 行方向のグループ集計
# 2 行と列を指定したピボット集計
# 3 集計関数の変更
# 4 複数の関数で集計
# 5 変数ごとに使用する関数を変更
# 6 引数を持つ関数/独自関数の扱い方
# 7 合計列の追加
# 8 NaNの置換
# 9 小数点の省略


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import numpy as np
import seaborn as sns


# データロード
iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')


# 1 行方向のグループ集計 -------------------------------------------------------------

# ＜ポイント＞
# - カテゴリカルデータで行方向のグループ集計を行う
#   --- 列にカテゴリカルデータを指定しない

# 単独列でグループ集計
# --- 列を省略するか、Noneを与える
iris.pivot_table(index="species", values="sepal_length", aggfunc="sum")
iris.pivot_table(index="species", columns=None, values="sepal_length", aggfunc="sum")

# 複数列でグループ集計
# --- group_by() + sum()の集計と同様
tips.pivot_table(index=["day", "sex"], columns=None, values="tip", aggfunc="sum")
tips.filter(["day", "sex", "tip"]).groupby(["day", "sex"]).sum()


# 2 行と列を指定したピボット集計 ------------------------------------------------------

# ＜ポイント＞
# - ピボットテーブルは行/列それぞれでカテゴリカル変数を選択することで集計する
#   --- 行/列ともに複数カテゴリを選択することが可能

# 単独カテゴリ同士で集計
tips.pivot_table(index="day", columns="sex", values="tip", aggfunc="sum")

# 複数カテゴリ同士で集計
tips.pivot_table(index=["day", "sex"], columns="smoker", values="tip", aggfunc="sum")
tips.pivot_table(index=["day", "sex"], columns=["time", "smoker"], values="tip", aggfunc="sum")


# 3 集計関数の変更 -----------------------------------------------------------------

# ＜ポイント＞
# - ピボットテーブルの集計関数は｢1.出力値が一意｣｢2.集計値が数値｣の要件を満たせば基本的に使える
# - 代表的な集計関数はsum/mean/max/min/median/len

# 用意された関数を使用
# --- 文字列で指定
tips.pivot_table(index="day", columns="sex", values="tip", aggfunc="sum")
tips.pivot_table(index="day", columns="sex", values="tip", aggfunc="mean")

# ベース関数を使用
# --- 関数オブジェクトで指定
tips.pivot_table(index="day", columns="sex", values="tip", aggfunc=len)

# Numpyの集計関数を使用
# --- 関数オブジェクトで指定
tips.pivot_table(index="day", columns="sex", values="tip", aggfunc=sum)
tips.pivot_table(index="day", columns="sex", values="tip", aggfunc=np.sum)


# 4 複数の関数で集計 ---------------------------------------------------------------

# ＜ポイント＞
# - ピボットテーブルの集計関数は｢1.出力値が一意｣｢2.集計値が数値｣の要件を満たせば基本的に使える

# 用意された関数を使用
# --- 文字列で指定
tips.pivot_table(index="day", columns="sex", values="tip", aggfunc=["sum", "mean"])

# 外部関数を指定
# --- 関数オブジェクトで指定
# --- 文字列と関数オブジェクトを混在することはできない
tips.pivot_table(index="day", columns="sex", values="tip", aggfunc=[len, np.sum])


# 5 変数ごとに使用する関数を変更 -----------------------------------------------------

# ＜ポイント＞
# - 集計関数を辞書で指定することで、変数ごとに使用する関数を変更することもできる
#   --- 基本的に行のみを集計する場合の発想

# 列ごとに集計関数を変更
iris.pivot_table(index="species", aggfunc={"sepal_length": np.sum, "petal_length": np.mean})

# 列によって集計関数の数を変える
iris.pivot_table(index="species", aggfunc={"sepal_length": np.sum, "petal_length": [np.sum, np.mean]})


# 6 引数を持つ関数/独自関数の扱い方 ---------------------------------------------------

# ＜ポイント＞
# - 外部関数/ラムダ式のいずれかで定義すると、引数を持つ関数や複雑な関数を扱うこともできる
#   --- ｢1.出力値が一意｣｢2.集計値が数値｣の要件を満たす必要がある


# 準備1：関数定義（引数を固定値にする）
def quantile_10p(x):
    return np.quantile(x, q=0.1)


# 準備2：関数定義（引数をパラメータとして与える）
def quantile_custom(x, q):
    return np.quantile(x, q=q)


# 引数を固定した関数
iris.pivot_table(index="species", aggfunc=quantile_10p)

# 引数をパラメータとして与える関数
# --- ラムダ式で記述
iris.pivot_table(index="species", aggfunc=lambda x: quantile_custom(x, q=0.1))

# 今回の場合は関数を直接ラムダ式で記述することで対処
iris.pivot_table(index="species", aggfunc=lambda x: np.quantile(x, q=0.1))


# 7 合計列の追加 -------------------------------------------------------------------

# ＜ポイント＞
# - ピボットテーブルは表の完成品としてつ

# 単独カテゴリ同士で集計
tips.pivot_table(index="day", columns="sex", values="tip",
                 aggfunc="sum", margins=True, margins_name="Total")


# 8 NaNの置換 ----------------------------------------------------------------------

# ＜ポイント＞
# - カテゴリが細かくなると対象データがない個所でNaNが発生する
#   --- 特定の数値で埋めるなどの処理が可能

# 集計によるNaN
# --- 処理なし
# --- 0で補完
tips.pivot_table(index=["day", "sex"], columns=["time", "smoker"], values="tip", aggfunc="sum")
tips.pivot_table(index=["day", "sex"], columns=["time", "smoker"], values="tip", aggfunc="sum", fill_value=0)


# 9 小数点の省略 --------------------------------------------------------------------

# ＜ポイント＞
# - 必要に応じて数値フォーマットを変更する

# 集計によるNaN
# --- 処理なし
# --- 0で補完
tips_pivot = tips.pivot_table(index="day", columns="sex", values="tip", aggfunc="sum")
tips_pivot.applymap('{:,.0f}'.format)
