# exi-COVID19-projections

This is a GBM model leveraging c3.ai's expansive data lake. We achieve 2% error on LA county with an error less than 10% for the top 5 most populous counties in the US. This is better than current CDC top models. In the leaderboard below. Our model will be validated by them soon.

https://github.com/youyanggu/covid19-forecast-hub-evaluation

In the meantime, here are our results:

                              Location  ...              (MAE/MAP)*100
0   LosAngeles_California_UnitedStates  ...   2.198157163298805% error
1           Cook_Illinois_UnitedStates  ...  1.4643759588576224% error
2            Harris_Texas_UnitedStates  ...   8.109221562925217% error
3        Maricopa_Arizona_UnitedStates  ...    4.42502011514675% error
4     SanDiego_California_UnitedStates  ...  2.7067607178570268% error
5       Orange_California_UnitedStates  ...   3.863724116648829% error
6      Miami-Dade_Florida_UnitedStates  ...   5.443478609018028% error
7            Dallas_Texas_UnitedStates  ...  7.1840531839591355% error
