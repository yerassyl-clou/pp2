from datetime import datetime

current_datetime = datetime.now()

new = current_datetime.replace(microsecond=0)

print("Datetime without microseconds:", new)
