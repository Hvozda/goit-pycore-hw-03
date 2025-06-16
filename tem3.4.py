
import datetime
def get_days_from_today(date_str: str) -> int:
    input_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    today = datetime.datetime.today()
    delta = today.date() - input_date.date()
    return delta.days
print(get_days_from_today("2021-10-09"))

    
    
    

    