from diaries.AbstractDiary import AbstractDiary
class SakakibaraDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-14"
    def get_summary(self):
        return "今日もいい1日だった。明日も頑張ろう"
    def get_author(self):
        return "Ryuichi Sakakibara"