def get_valid_customer_code():
    customer_code = input('Enter customer code (R, C, or I): ')
    if customer_code not in ['R', 'C', 'I']:
        print('Invalid input (customer code)')
        exit()
    return customer_code

def get_valid_reading(prompt):
    while True:
        try:
            reading = int(input(prompt))
            if 0 <= reading <= 999999999:
                return reading
            else:
                print('Invalid input (beginning or ending reading value is out of the range)')
                exit()
        except ValueError:
            print('Invalid input. Please enter an integer value.')
            continue

def calculate_billing_amount(customer_code, used_gallons):
    if customer_code == 'R':  # residential
        return 5.00 + (0.0005 * used_gallons)
    elif customer_code == 'C':  # commercial
        if used_gallons <= 4000000:
            return 1000.00
        else:
            return 1000.00 + (0.00025 * (used_gallons - 4000000))
    elif customer_code == 'I':  # industrial
        if used_gallons <= 4000000:
            return 1000.00
        elif used_gallons <= 10000000:
            return 2000.00
        else:
            return 2000.00 + (0.00025 * (used_gallons - 10000000))

def main():
    # customer code input
    customer_code = get_valid_customer_code()

    # Step 2: Input Beginning and Ending Readings
    start_reading = get_valid_reading('Enter beginning reading (between 0 and 999999999): ')
    end_reading = get_valid_reading('Enter ending reading (between 0 and 999999999): ')

    # calculates water usage
    # converts to gallons
    start_gallons = start_reading / 10
    end_gallons = end_reading / 10


    if end_reading < start_reading:
        end_gallons += 1000000000 / 10  # Add the "wrap-around" value to end_reading

    used_gallons = end_gallons - start_gallons

    # this calculates the billing
    to_bill = calculate_billing_amount(customer_code, used_gallons)

    # outputs summary
    print(f"Customer code: {customer_code}")
    print(f"Beginning reading value in gallons and tenths of gallon {start_gallons:.1f}")
    print(f"Ending reading value in gallons and tenths of gallon {end_gallons:.1f}")
    print(f"Gallons of water used: {used_gallons:.1f}")
    print(f"Amount billed: ${to_bill:.2f}")

# Run the program
main()
