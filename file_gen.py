import random, logging
from archive import logger

logger("testlog.log")

code_list = []
# set test sample size
file_count = 100
count = 0
while count <= file_count:
    rand_seq = random.sample(range(100, 999), 5)
    filecode = ''
    for i in rand_seq:
        filecode += str(i)
    code_list.append(filecode)
    set(code_list)
    file_content = "Created: {f}\nResult One: {n1}\nResult Two: {n2}\n\nEnd: {f}".format(
        f=filecode,
        n1=rand_seq[0],
        n2=rand_seq[1]
        )
    filename = "0{code}_CD".format(code=filecode)
    file = open("{path}/{file}.txt".format(path='data',file=filename), "w")
    file.write(file_content)
    file.close()
    logging.info('record: {num} - test: {f}'.format(num=count,f=filecode))
    count += 1

for code in code_list:

    file = open('codes.txt', 'a')
    file.write(str(code))
    file.write('\n')
