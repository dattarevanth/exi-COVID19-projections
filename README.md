# exi-COVID19-projections
11/23/20 update: Model now predicts total new cases over next z days (user specified) rather than a 5 day window in the future. This change enhances utility and should have been implemented in the first place. The error with being unable to predict Kings County New York has been confirmed as due to missing data in the c3.ai API. The training loop will now succesfully iterate over the user specified number of counties beyond 8. Accuracy is also observably improved due to correcting an error in the code which had the model predicting in the past not future and due to the larger scale of the prediction. To save time in the loop we calculate MAE/average of the target prediction y (total new cases over next z days) and report a rough approximation of percent error. Due to the relatively low standard deviation, this approximation is reasonably close to actual percent error calculated for individual predictions.


                             Location  ...  (MAE/average real value y)*100
LosAngeles_California_UnitedStates  ...  1.2609956961239168% error

Cook_Illinois_UnitedStates  ...   3.653759919553285% error

Harris_Texas_UnitedStates  ...   2.017228131952422% error

Maricopa_Arizona_UnitedStates  ...  2.7888707738790384% error

SanDiego_California_UnitedStates  ...  2.1263462703364753% error

Orange_California_UnitedStates  ...  1.3033774391246662% error

Miami-Dade_Florida_UnitedStates  ...  2.9555846619835684% error

Dallas_Texas_UnitedStates  ...   5.824786330299069% error

Riverside_California_UnitedStates  ...  1.9223331068181557% error




NOTE: PREDICTING MORE THAN THE TOP 8 MOST POPULOUS COUNTIES WITH THE CURRENT EXECUTABLE WILL NOT WORK DUE TO MISSINGNESS IN API DATA.
WE WILL UPDATE A NEW EXECUTABLE UNDER A NEW BRANCH TO PRESERVE CONTEST INTEGRITY AND STILL ALLOW RESEARCHERS AND PUBLIC HEALTH OFFICIALS TO UTILZE OUR WORK.

This is a GBM model leveraging c3.ai's expansive data lake. We achieve 2% error on LA county with an error less than 10% for the top 5 most populous counties in the US. This is better than current CDC top national/state models in the leaderboard below. In fact, these models don't even predict at a county level which is where public health interventions can be applied most rapidly and surgically. 

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
