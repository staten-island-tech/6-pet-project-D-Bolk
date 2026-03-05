""" def honi(letter):
    x = {{block.lower}}
    
    for letter in x:
 """

""" def solve():
    word = honi
    honi = 0
    count = 0
    
    for letter in word:
        if letter==word[honi]:
            honi += 1
            
            if honi == 4:
                count += 1
                honi = 0
                
    print(count)

    solve() """
def magnus(word):
    count = 0
    state = 0
for char in word:
    if state == 0 and char.upper() == 'H':
        state == 1
    elif state == 1 and char.upper() == 'O'
        state = 2
    elif state == 2 and char.upper() == 'N':
        state = 3
    elif state == 3 and char.upper() == 'I':
        count +=1
        state = 0

print(count)