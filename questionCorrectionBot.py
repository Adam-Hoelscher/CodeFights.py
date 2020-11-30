import re


def questionCorrectionBot(question):

    temp = question
    temp = re.sub(pattern=' *, *', repl=', ', string=temp.strip())
    temp = re.sub(pattern=' +', repl=' ', string=temp)
    temp = temp[0].upper() + temp[1:]
    temp = re.sub(pattern='\?', repl='', string=temp) + '?'
    return temp
    