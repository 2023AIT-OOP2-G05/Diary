from diaries.AbstractDiary import AbstractDiary
class TakanoDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-11"
    def get_summary(self):
        return "20歳の誕生日だった。ワイン飲んだ。"
    def get_author(self):
        return "Harumitsu Takano"