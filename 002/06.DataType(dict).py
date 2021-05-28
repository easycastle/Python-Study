f1 = {
    'tom' : 1, 
    'jerry' : 2, 
    'smith' : 3, 
    'jack' : 4, 
    'lucy' : 5
    }

f2 = {
    'tom' : 'A', 
    'jerry' : 'B', 
    'smith' : 'C', 
    'jack' : 'D', 
    'lucy' : 'E'
    }

f3 = {
    1 : 170,
    2 : 165, 
    3 : 182, 
    4 : 177, 
    5 : 168
    }

f4 = {
    1 : 'apple', 
    2 : 'banana', 
    3 : 'orange', 
    4 : 'mango', 
    5 : 'kiwi'
    }

f5 = {
    1 : {
        'tom' : 1, 
        'jerry' : 2, 
        'smith' : 3, 
        'jack' : 4, 
        'lucy' : 5
        }, 
    2 : {
        'tom' : 'A', 
        'jerry' : 'B', 
        'smith' : 'C', 
        'jack' : 'D', 
        'lucy' : 'E'
        }, 
    3 : {
        1 : 170,
        2 : 165, 
        3 : 182, 
        4 : 176, 
        5 : 168
        }, 
    4 : {
        1 : 'apple', 
        2 : 'banana', 
        3 : 'orange', 
        4 : 'mango', 
        5 : 'kiwi'
        } 
    }

print(f1['tom'])
print(type(f1))

print(f2)

print(type(f3[1]))

print(f4[2])

print(f5[3][4])