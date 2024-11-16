from datetime import datetime, timezone, timedelta

def get_KST()->datetime:
    # KST = UTC+9
    KST = timezone(timedelta(hours=9))
    
    # Remove milliseconds
    time_record = datetime.now(KST).replace(microsecond=0)
    
    return time_record