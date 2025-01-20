from datetime import datetime, timedelta


def display_current_datetime():
    global current_datetime
    current_datetime = datetime.now()
    print(f"Current date and time: {current_datetime:%Y-%m-%d %H:%M:%S}") 
display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    current_date = current_datetime.date()
    future_date = current_date + timedelta(days=number_of_days)
    print(f"future date: {future_date.strftime('%Y-%m-%d')}")
calculate_future_date()