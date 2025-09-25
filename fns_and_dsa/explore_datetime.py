from datetime import datetime, timedelta
# gets the current date 
def display_current_datetime():
    global current_date  
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")
display_current_datetime()
no_days = int(input("Enter the number of days to add to the current date: "))
# calculate the future date using timedelta
def calculate_future_date ():
    future_date = timedelta(days=no_days) + current_date
    future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {future_date}")
calculate_future_date()