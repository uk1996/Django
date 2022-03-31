# 커스텀 Path Converter
class YearConverter_2000:
       regex = "20\d{2}"
       
       def to_python(self, value): # url로부터 추출한 문자열을 뷰에 넘겨주기 전에 변환
              return int(value)
       
       def to_url(self, value): # url reverse 시에 호출
              return str(value)

class MonthConverter(YearConverter_2000):
    regex = r"\d{1, 2}"

class DayConverter(YearConverter_2000):
    regex = r"[0123]\d"