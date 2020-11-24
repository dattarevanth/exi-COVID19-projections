# exi-COVID19-projections
11/23/20 update: Model now predicts total new cases over next 28 days (user specified) rather than a 5 day window in the future. This change enhances utility and should have been implemented in the first place. The error with being unable to predict Kings County New York has been confirmed as due to missing data in the c3.ai API. The training loop will now succesfully iterate over the user specified number of counties beyond 8. Accuracy is also observably improved due to correcting an error in the code which had the model predicting in the past not future and due to the larger scale of the prediction. To save time in the loop we calculate MAE/average of the target prediction y (total new cases over next 28 days) and report a rough approximation of percent error. Due to the relatively low standard deviation, this approximation is reasonably close to actual percent error calculated for individual predictions.


                             Location  ...  (MAE/average real value y)*100
0       LosAngeles_California_UnitedStates  ...  1.2503106002193303% error

1               Cook_Illinois_UnitedStates  ...   3.653761533826847% error

2                Harris_Texas_UnitedStates  ...  2.0172355480118855% error

3            Maricopa_Arizona_UnitedStates  ...   2.788871509987053% error

4         SanDiego_California_UnitedStates  ...  2.1263464366001408% error

5           Orange_California_UnitedStates  ...  1.3033752839631478% error

6          Miami-Dade_Florida_UnitedStates  ...    3.35174910187414% error

7                Dallas_Texas_UnitedStates  ...   5.654946957710884% error

8        Riverside_California_UnitedStates  ...  1.8975864662258999% error

9                Clark_Nevada_UnitedStates  ...  0.7812851055136633% error

10             Queens_NewYork_UnitedStates  ...  3.8542194965159418% error

11            King_Washington_UnitedStates  ...   4.509753041294729% error

12   SanBernardino_California_UnitedStates  ...  3.1768895456913158% error

13              Tarrant_Texas_UnitedStates  ...   3.878228981285789% error

14                Bexar_Texas_UnitedStates  ...  1.3534693257748194% error

15            Broward_Florida_UnitedStates  ...  1.8980612342215466% error

16      SantaClara_California_UnitedStates  ...  1.5479287962608839% error

17             Wayne_Michigan_UnitedStates  ...   6.366410044000325% error

18         Alameda_California_UnitedStates  ...  1.5512122743609074% error

19            NewYork_NewYork_UnitedStates  ...   5.364641596804042% error

20    Middlesex_Massachusetts_UnitedStates  ...   4.506548326601432% error

21  Philadelphia_Pennsylvania_UnitedStates  ...   3.898557489958246% error

22      Sacramento_California_UnitedStates  ...   2.054471279347801% error

23          PalmBeach_Florida_UnitedStates  ...  1.4126520369796451% error

24            Suffolk_NewYork_UnitedStates  ...   4.643070381751109% error

25       Hillsborough_Florida_UnitedStates  ...  1.2085644873942214% error

26              Bronx_NewYork_UnitedStates  ...   5.492446675698457% error

27             Orange_Florida_UnitedStates  ...  1.9754856050119662% error

28             Nassau_NewYork_UnitedStates  ...  3.9251102369755277% error

29              Franklin_Ohio_UnitedStates  ...   3.818895647951647% error

OLD#BELOW###########################################################################################################################



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
