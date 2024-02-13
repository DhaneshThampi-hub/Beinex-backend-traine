'''4.	Write a Python program to extract year, month, date and time using Lambda.
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178'''

from datetime import datetime
extract_info = lambda dt: (dt.year, dt.month, dt.day, dt.strftime("%H:%M:%S"))
current_datetime = datetime.now()
result = extract_info(current_datetime)
print("Year:", result[0])
print("Month:", result[1])
print("Date:", result[2])
print("Time:", result[3])