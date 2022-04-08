def print_rates_chart() -> None:
    file_name = "pricing_sheet.csv"

    #The strip() method is here because we need to strip the carriage return off the autograder's inputs
    product_name = input("Enter Product Name: ").strip()
    lock_period = input("Enter Lock Period : ").strip()

print_rates_chart()