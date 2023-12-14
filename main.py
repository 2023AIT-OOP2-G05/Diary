from diaries.DiarySample import DiarySample
from diaries.TakanoDiary import TakanoDiary
from diaries.TsuzukiDiary import TsuzukiDiary
from diaries.ImaiDiary import ImaiDiary
from diaries.SugiyamaDiary import SugiyamaDiary
from diaries.SakakibaraDiary import SakakibaraDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           TakanoDiary(),
           TsuzukiDiary(),
           ImaiDiary(), 
           SugiyamaDiary(),
           SakakibaraDiary() ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()