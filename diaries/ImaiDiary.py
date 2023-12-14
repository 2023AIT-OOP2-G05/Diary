from diaries.AbstractDiary import AbstractDiary
class ImaiDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-14"
    def get_summary(self):
        return "今日はオブジェクト指向プログラミング演習2のグループワーク演習だった。とても疲れた。"
    def get_author(self):
        return "Shota Imai"