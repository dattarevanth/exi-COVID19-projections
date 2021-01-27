# exi-COVID19-projections
This is a GBM model leveraging c3.ai's expansive data lake. We achieve <2% error on LA county with an error less than 10% for the top 5 most populous counties in the US. This is better than current CDC top national/state models in the leaderboard below. In fact, these models don't even predict at a county level which is where public health interventions can be applied most rapidly and surgically. 

https://github.com/youyanggu/covid19-forecast-hub-evaluation

Here are the latest models' results with percent error for predictions made on unseen test data. The percent error value reported describes average error of daily predictions made on unseen test data, predicting cumulative new cases for the next 28 days.

         Location.......................................................... Percent Error

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


