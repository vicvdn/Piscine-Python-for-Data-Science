import datetime

#we get the datetime class inside the datetime module
firstDate = datetime.datetime(1970, 1, 1)
actualDate = datetime.datetime.now() - firstDate
secondsSinceFirstDate = int(actualDate.total_seconds())

print(f"Seconds since January 1, 1970: {secondsSinceFirstDate:,.2f} or {secondsSinceFirstDate:.2e} in scientific notation")