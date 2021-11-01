import random, logging, datetime, csv
from archive import logger

logger("testlog.log")

dt = datetime.datetime.now()
rec_list = [["","uid","date","datetime","text","num",""]]
rec_cnt = 10000
cnt = 0
# quartile comparison parameters to alter data values
lwr = rec_cnt * 0.25
mid = rec_cnt * 0.5
upp = rec_cnt * 0.75

while cnt <= rec_cnt:
    row = []
    rand_seq = random.sample(range(0, 9), 9)
    uid_code = ''
    for i in rand_seq: uid_code += str(i)
    code = f'0{uid_code}COD'
    # type index value
    row.append(cnt)
    # type unique unique identifier value
    row.append(code)
    # type date records
    row.append(dt.strftime("%x"))
    row.append(dt.strftime("%x %X"))
    # type text value or null
    if cnt % 50 == 0:
        row.append("test")
    else:
        row.append("")
    # type number value variable quartiles of count
    if cnt <= lwr:
        row.append("2")
    elif cnt > lwr and cnt <= mid:
        row.append("4")
    elif cnt > mid and cnt <= upp:
        row.append("6")
    else:
        row.append("8")
    # of 11 multiple, additional text value for extra column
    if cnt % 11 == 0:
        row.append("text")
    else:
        row.append("")
    rec_list.append(row)
    cnt += 1

with open(file="test.csv", mode="w+", newline="") as doc:
    wt = csv.writer(doc)
    wt.writerows(rec_list)