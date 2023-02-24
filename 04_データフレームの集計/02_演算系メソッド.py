# ******************************************************************************
# Project   : Pandasのメモ
# Chapter   : 04 データフレームの集計
# Theme     : 02 演算系メソッド
# Date      : 2023/02/25
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 基本統計量


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import numpy as np
import seaborn as sns


# データロード
iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')


# 1 基本統計量 -----------------------------------------------------------------------

# カウント
iris.count()
iris.nunique()

# 平均
iris.select_dtypes('float').sum()
iris.select_dtypes('float').mean()
iris.select_dtypes('float').median()

# 分散
iris.select_dtypes('float').std()
iris.select_dtypes('float').var()
iris.select_dtypes('float').mad()  # 標本平均絶対偏差
iris.select_dtypes('float').sem()  # (不偏)標本標準誤差

# 位置
iris.select_dtypes('float').min()
iris.select_dtypes('float').max()
iris.select_dtypes('float').quantile(q=0.25)

# 分布
iris.select_dtypes('float').skew()
iris.select_dtypes('float').kurtosis()
iris.select_dtypes('float').kurt()


# 2 累積処理 ---------------------------------------------------------------------------

# 累和
iris.select_dtypes('float').cumsum()

# 累積
iris_div = iris.groupby('species').transform(lambda x: x/x.mean())
iris_div.select_dtypes('float').cumprod()

# その他
iris.select_dtypes('float').cummin()
iris.select_dtypes('float').cummax()


# 3 差分処理 ----------------------------------------------------------------------------

# 差分
iris.select_dtypes('float').diff()
iris.select_dtypes('float').diff(periods=2)


# 4 シフト処理 --------------------------------------------------------------------------

# シフト
iris.select_dtypes('float').shift()
iris.select_dtypes('float').shift(periods=2)
iris.select_dtypes('float').shift(periods=-2)


# 5 行列計算 -----------------------------------------------------------------------------

iris.select_dtypes('float').cov()
iris.select_dtypes('float').corr()
