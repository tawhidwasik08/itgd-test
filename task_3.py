import gspread
import pandas as pd


def read_sheet(worksheet):
    data = worksheet.get_all_values()
    headers = data[0]
    values = data[1:]
    df = pd.DataFrame(values, columns=headers)
    return df


def add_row_to_sheet(worksheet, values):
    worksheet.append_row(values)
    return None


def print_option_screen():
    print()
    print("+----------------- Task 3 Interactions ------------------+")
    print("| 1. Show data from sheet                                |")
    print("| 2. Add a new row to existing sheet                     |")
    print("+--------------------------------------------------------+")
    print()
    return None


def prompt_for_values(columns):
    values = []
    for col in columns:
        if col == "id":
            while True:
                try:
                    value = int(input(f"Enter value for '{col}' (integer): "))
                    break
                except ValueError:
                    print("Error: Please enter an integer value for 'id'.")
        else:
            value = input(f"Enter value for '{col}': ")
        values.append(value)
    return values


def main():
    gc = gspread.service_account(filename="itgd-tasks-72817a0cdc72.json")
    wks = gc.open("itgd_task_sheet").sheet1

    while True:
        print_option_screen()
        choice = input("Enter your choice (1 or 2, or 'q' to quit): ")
        if choice == "1":
            df = read_sheet(wks)
            print(df)
            input("Press any key to continue...")
        elif choice == "2":
            df = read_sheet(wks)
            headers = df.columns.tolist()
            new_row_values = prompt_for_values(headers)
            if all(new_row_values):
                add_row_to_sheet(wks, new_row_values)
                print("New row added successfully.")
            else:
                print("Error: All values must be provided.")
            input("Press any key to continue...")
        elif choice.lower() == "q":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
