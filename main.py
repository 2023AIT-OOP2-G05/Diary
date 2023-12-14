from diaries.DiarySample import DiarySample
from diaries.TakanoDiary import TakanoDiary
from diaries.TsuzukiDiary import TsuzukiDiary
from diaries.ImaiDiary import ImaiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           TsuzukiDiary(),
           TakanoDiary(), 
           ImaiDiary(), ]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()