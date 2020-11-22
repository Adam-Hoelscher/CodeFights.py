from datetime import datetime


def dailyOHLC(timestamp, instrument, side, price, size):
    
    records = {}
    
    for t, i, p in zip(timestamp, instrument, price):
        date = datetime.fromtimestamp(t).strftime('%Y-%m-%d')
        k = date, i
        o, h, l, c = records.get(k, (p, p, p, p))
        h = max(h, p)
        l = min(l, p)
        c = p
        records[k] = o, h, l, c

    ans = []
    for key, val in sorted(records.items()):
        ans.append(key + tuple(f'{v:.2f}' for v in val))
        
    return ans
