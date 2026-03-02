def lang(sentence):
    words={sentence.lower}

lowercase_text = lang.lower()
count_t = lowercase_text.count('t')
count_s = lowercase_text.count('s')
t = 0
s = 0
for letter in words:
       t+=1


if count_t > count_s:
        print ("english")
else:
        print ("french")
