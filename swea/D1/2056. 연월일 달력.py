T = int(input())

months = ["01", '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
days = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']

for i in range(1, T + 1):
    data = input().strip()

    year = int(data[:4])
    month = data[4:6]
    day = int(data[6:])

    valid_m = False
    valid_d = False

    if month in months:
        valid_m = True

    try:
        a = months.index(month)
        if day in range(1, int(days[a]) + 1):
            valid_d = True
    except ValueError:
        pass

    if valid_d and valid_m:
        # Format year to always have four digits
        formatted_year = "{:04d}".format(year)
        formatted_day = "{:02d}".format(day)
        print("#{} {}/{}/{}".format(i, formatted_year, month, formatted_day))
    else:
        print("#{} {}".format(i, -1))
