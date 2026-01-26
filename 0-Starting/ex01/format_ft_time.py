import time
import datetime

timestamp = time.time()

print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")
print(datetime.datetime.fromtimestamp(timestamp).strftime('%b %d %Y'))
