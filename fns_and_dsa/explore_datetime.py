from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: " + str(current_date))

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = date.today() + timedelta(days=number_of_days)
    print("Future date: " + str(future_date.strftime("%Y-%m-%d")))

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
