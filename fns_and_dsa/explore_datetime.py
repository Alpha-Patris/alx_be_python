from datetime import datetime, timedelta

def display_current_datetime():
    current_datetime = datetime.now()
    global current_date
    current_date = current_datetime.date()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d\s*%H:%M:%S")
    print("Current date and time:", formatted_datetime)
    return

def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date: ", future_date)


display_current_datetime()
calculate_future_date()