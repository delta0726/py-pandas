"""
Category  : Grammar of Pandas
Chapter   : 01 基本操作
Title     : 02 クイック操作
Date      : 2022/07/10
"""


# ＜概要＞
# - データセットに直接適用できるクイック分析メソッド


# ＜目次＞
# 0 準備
# 1 数値データをワンタッチで分析
# 2 数値データからプロット作成


# 0 準備 ----------------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.io as pio


# データロード
iris = sns.load_dataset('iris')
stocks = px.data.stocks()


# 1 数値データをクイック集計 ----------------------------------------------------------------

# ＜ポイント＞
# - pandas dataframeから簡単に出力できる集計などを列挙


# 基本統計量
# - 数値列のみを抽出して基本統計量を算出
iris.describe()

# 相関分析
# - 数値列のみを抽出して相関係数行列を作成
iris.corr()


# 2 数値データからプロット作成 --------------------------------------------------------------

# ＜ポイント＞
# - データフレームから簡単に出力する前提としてplotlyを用いる


# ブラウザに出力
# --- jupyterの場合は不要
pio.renderers.default = 'browser'

# プロット作成
p = px.scatter(iris, x="sepal_width", y="sepal_length")
pio.show(p)
