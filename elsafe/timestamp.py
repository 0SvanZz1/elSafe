import time
import pytz
from datetime import datetime

def generate_timestamp():
    current_date_utc = datetime.fromtimestamp(time.time(),tz=pytz.utc)
    timestamp = current_date_utc.strftime("%Y-%m-%dT%H:%M:%S.%f")
    return timestamp
