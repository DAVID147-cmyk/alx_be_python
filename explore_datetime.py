def display_current_datetime():
    # Save current date and time inside current_date
    current_date = datetime.now()

    # Format: YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

    return current_date
def calculate_future_date(days):
    # Save the future date inside future_date
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)

    # Format: YYYY-MM-DD
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")

    return future_date


def main():
    # Part 1: Display current date & time
    display_current_datetime()

    # Part 2: Get days from user and calculate future date
    try:
        user_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
