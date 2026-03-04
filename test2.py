""" def honi(letter):
    x = {{block.lower}}
    
    for letter in x:
 """

import sys

def solve():
    word = sys.stdin.read().strip()
    
    target = "HONI"
    
    honi_idx = 0
    
    count = 0
    
    for letter in word:
        if letter == target[honi_idx]:
            honi_idx += 1
            
            if honi_idx == 4:
                count += 1
                honi_idx = 0
                
    print(count)

if __name__ == '__main__':
    solve()