from datetime import datetime
current_datetime = datetime.now()

datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Original Datetime:", current_datetime)
print("Datetime without Microseconds:", datetime_without_microseconds)
