# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:40:43 2020

@author: choieastsea
"""

#import modules
import random

#test 'print matrix'
def print_matrix(field):
    for row in field:
        for element in row:
            print(element,end='  ')
        print()

#k개의 mine을 field에 'b'로 심고, 어디에 심었는지 리턴한다
def plant_mine(field,k):
    #print('\n\nfunc : plant_mine,','field :',field,', k :',k,'\n\n')
    mine_list = []
    i = 0
    while i < k:
        #print('i : ',i)
        row = random.randint(0, len(field)-1) #양 끝값 모두 포함한 범위의 랜덤 정수
        col = random.randint(0, len(field[0])-1)
        #print('row :',row,', col :',col)
        if field[row][col] == 0:
            i += 1
            field[row][col] = 'b'
            mine_list.append([row,col]) #mine_list에는 mine의 matrix coord를 list로 갖고 있음
        else:
            #print('중복')
            continue
    #print('mine_list : ',mine_list)
    return [field, mine_list]

# #mine_list를 통하여 mine 주변의 field값을 +1해준다
# def make_map(field, mine_list):
#     #print(mine_list)
#     garo_end = len(field[0]) - 1
#     sero_end = len(field) - 1
#     for element in mine_list:
#         #case 1
#         if element[0]!=1 and element[1]!=0:
#             field[1]
#     #return map

def make_map(field,mine_list):
    #print('func make_map')
    map = [[0 for col in range(m)] for row in range(n)]
    for mine_loc in mine_list:
        row = mine_loc[0]
        col = mine_loc[1]
        if row == 0 and col ==0:
            #case1
            map[row][col+1] +=1
            map[row+1][col] +=1
            map[row+1][col+1] +=1

        elif row == 0 and col == len(field[0])-1:
            #case2
            map[row][col-1] +=1
            map[row+1][col] +=1
            map[row+1][col-1] +=1

        elif row == 0:
            #case3
            map[row][col-1] +=1
            map[row][col+1] +=1
            map[row+1][col] +=1
            map[row+1][col+1] +=1
            map[row+1][col-1] +=1
            
        elif row == len(field) - 1 and col == len(field[0])-1:
            #case4
            map[row-1][col] +=1
            map[row][col-1] +=1
            map[row-1][col-1] +=1

        elif col == len(field[0])-1:
            #case5
            map[row+1][col] +=1
            map[row-1][col] +=1
            map[row][col-1] +=1
            map[row+1][col-1] +=1
            map[row-1][col-1] +=1

        elif row == len(field)-1 and col == 0:
            #case6
            map[row-1][col] +=1
            map[row][col+1] +=1
            map[row-1][col+1] +=1

        elif col == 0:
            #case7
            map[row+1][col] +=1
            map[row-1][col] +=1
            map[row][col+1] +=1
            map[row+1][col+1] +=1
            map[row-1][col+1] +=1

        elif row == len(field)-1:
            #case8
            map[row][col+1] +=1
            map[row][col-1] +=1
            map[row-1][col] +=1
            map[row-1][col+1] +=1
            map[row-1][col-1] +=1

        else:
            #case9
            map[row+1][col] +=1
            map[row-1][col] +=1
            map[row][col+1] +=1
            map[row][col-1] +=1
            map[row+1][col-1] +=1
            map[row+1][col+1] +=1
            map[row-1][col+1] +=1
            map[row-1][col-1] +=1
        
    for mine in mine_list:
        map[mine[0]][mine[1]] = 'b'
    return map

def uncover(mine_map, user_map, row, col):
    '''
    user_map[row][col]의 정보를 출력한다.
    만약 폭탄이면 게임 끝
    0이 아닌 숫자면 해당 숫자만 드러남
    0이면 주변 블록의 숫자를 드러냄(거기에 또 0이 있으면 주변 드러냄)
    '''
    user_map[row][col] = mine_map[row][col]
    if mine_map[row][col]=='b': #지뢰 밟음
        print('game over')
        return -1
        #not_over = False
    elif mine_map[row][col] !=0:
        return user_map
    else:   #0이라면, 주변 다 출력하면 된다.
        if row == 0 and col ==0:
            #case1
            uncover[row][col+1]
            uncover[row+1][col]
            uncover[row+1][col+1]

        elif row == 0 and col == len(field[0])-1:
            #case2
            uncover[row][col-1]
            uncover[row+1][col] 
            uncover[row+1][col-1] 

        elif row == 0:
            #case3
            uncover[row][col-1] 
            uncover[row][col+1] 
            uncover[row+1][col] 
            uncover[row+1][col+1] 
            uncover[row+1][col-1] 
            
        elif row == len(field) - 1 and col == len(field[0])-1:
            #case4
            uncover[row-1][col] 
            uncover[row][col-1] 
            uncover[row-1][col-1] 

        elif col == len(field[0])-1:
            #case5
            uncover[row+1][col] 
            uncover[row-1][col] 
            uncover[row][col-1] 
            uncover[row+1][col-1] 
            uncover[row-1][col-1] 

        elif row == len(field)-1 and col == 0:
            #case6
            uncover[row-1][col] 
            uncover[row][col+1] 
            uncover[row-1][col+1] 

        elif col == 0:
            #case7
            uncover[row+1][col] 
            uncover[row-1][col] 
            uncover[row][col+1] 
            uncover[row+1][col+1] 
            uncover[row-1][col+1] 

        elif row == len(field)-1:
            #case8
            uncover[row][col+1] 
            uncover[row][col-1] 
            uncover[row-1][col] 
            uncover[row-1][col+1] 
            uncover[row-1][col-1] 

        else:
            #case9
            uncover[row+1][col] 
            uncover[row-1][col] 
            uncover[row][col+1] 
            uncover[row][col-1] 
            uncover[row+1][col-1] 
            uncover[row+1][col+1] 
            uncover[row-1][col+1] 
            uncover[row-1][col-1] 


def flag(mine_list, user_map, row, col):
    '''
    map의 row, col 위치에 flag를 설정, flag 수 감소시키기
    field에는 'b'의 정보가 있음
    '''
    print('func flag')    


#get size of matrix from user input
m = int(input('col : '))
n = int(input('row : '))
k = int(input('number of mines : '))

#game over
not_over = True

#make m*n matrix, each element is initialized to zero.
field = [[0 for col in range(m)] for row in range(n)]
user_map = [['▢' for col in range(m)] for row in range(n)]
[field, mine_list] = plant_mine(field, k)
#mine_map : answer sheet of mine_sweeper
mine_map = make_map(field, mine_list)
print_matrix(mine_map)

print_matrix(user_map)
while not_over:
    row,col = input('row col(0~) : ').split()
    print(row,',',col)
    opt = input('1 : flag, 2: uncover ==>')
    if opt == '1':
        #flag
        user_map = flag(mine_list, user_map, row, col)
    elif opt == '2':
        #uncover
        user_map = uncover(user_map,row,col)
        if user_map == -1:
            not_over = False
        print_matrix(user_map)
    else:
        continue
    