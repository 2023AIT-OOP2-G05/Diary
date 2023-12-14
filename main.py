from diaries.DiarySample import DiarySample
from diaries.K22041Diary import TsuzukiDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    # 日記の追加
    TsuzukiDiary(),
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()