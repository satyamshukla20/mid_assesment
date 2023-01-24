#Create function to check if date is in given range

from datetime import datetime, date

def is_date_in_range(curdate, start_date, end_date):
    if isinstance(curdate, (datetime, date)):
        return start_date <= curdate <= end_date
    else:
        raise TypeError("current date is not a datetime or date object")

check_date = date(2023, 1, 24)
start_date = date(2023, 1, 1)
end_date = date(2023, 12, 31)
print(is_date_in_range(check_date, start_date, end_date))
