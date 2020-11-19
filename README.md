# exi-COVID19-projections

NOTE: PREDICTING MORE THAN THE TOP 8 MOST POPULOUS COUNTIES WITH THE CURRENT EXECUTABLE WILL NOT WORK DUE TO MISSINGNESS IN API DATA.
WE WILL UPDATE A NEW EXECUTABLE UNDER A NEW BRANCH TO PRESERVE CONTEST INTEGRITY AND STILL ALLOW RESEARCHERS AND PUBLIC HEALTH OFFICIALS TO UTILZE OUR WORK.

This is a GBM model leveraging c3.ai's expansive data lake. We achieve 2% error on LA county with an error less than 10% for the top 5 most populous counties in the US. This is better than current CDC top models. In the leaderboard below. Our model will be validated by them soon.

https://github.com/youyanggu/covid19-forecast-hub-evaluation

In the meantime, here are our results:

LosAngeles_California_UnitedStates  ...2.198157163298805% error

Cook_Illinois_UnitedStates          ...1.4643759588576224% error

Harris_Texas_UnitedStates           ...8.109221562925217% error

Maricopa_Arizona_UnitedStates       ...4.42502011514675% error

SanDiego_California_UnitedStates    ...2.7067607178570268% error

Orange_California_UnitedStates      ...3.863724116648829% error

Miami-Dade_Florida_UnitedStates     ...5.443478609018028% error

Dallas_Texas_UnitedStates           ...7.1840531839591355% error
