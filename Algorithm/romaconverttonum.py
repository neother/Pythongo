import re
'''
above is for special conditons
start here is define the normal conditon
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
'''
'''
            elif list_roma[index:index + 2] == ['I', 'V']:
                print('come to here IV')
                newlist.append(4)
                index = index + 2
'''


class solution(object):
    def romacoverttonum(self, roma):

        list_roma = list(roma)
        print(list_roma)
        length = len(list_roma)
        index = 0
        newlist = list()
        special = 0

        while index < length:
            ################## FOR CHAR I ############################
            if list_roma[index] == 'I':

                if index != length - 1:
                    print('i am 38')
                    if list_roma[index + 1] == 'V':
                        newlist.append(4)
                        index += 2
                    elif list_roma[index + 1] == 'X':
                        newlist.append(9)
                        index += 2
                    else:
                        newlist.append(1)
                        print('i am 47')
                        index += 1
                else:
                    newlist.append(1)
                    print('i am 51')
                    index += 1
###################FOR CHAR V #########################
            elif list_roma[index] == 'V':

                newlist.append(5)
                print('i am 55')
                index += 1
###################FOR CHAR X #########################
            elif list_roma[index] == 'X':

                if index != length - 1:
                    print('i am 65')
                    if list_roma[index + 1] == 'L':
                        newlist.append(40)
                        index += 2
                    elif list_roma[index + 1] == 'C':
                        newlist.append(90)
                        index += 2
                    else:
                        newlist.append(10)
                        print('i am 74')
                        index += 1
                else:
                    newlist.append(10)
                    print('i am 78')
                    index += 1
###################FOR CHAR L #########################
            elif list_roma[index] == 'L':

                newlist.append(50)
                print('i am 84')
                index += 1
###################FOR CHAR C #########################
            elif list_roma[index] == 'C':

                if index != length - 1:
                    print('i am 91')
                    if list_roma[index + 1] == 'D':
                        newlist.append(400)
                        index += 2
                    elif list_roma[index + 1] == 'M':
                        newlist.append(900)
                        index += 2
                    else:
                        newlist.append(100)
                        print('i am 100')
                        index += 1
                else:
                    newlist.append(100)
                    print('i am 104')
                    index += 1
###################FOR CHAR D #########################
            elif list_roma[index] == 'D':

                newlist.append(500)
                print('i am 108')
                index += 1
###################FOR CHAR M #########################

            elif list_roma[index] == 'M':

                newlist.append(1000)
                print('i am 115')
                index += 1
###################FOR CHAR OTHERS #########################

            else:
                print('wrong data')
                index += 1
        return(newlist)


input_roma = input('YOUR INPUT IS :')
test = solution()
a = test.romacoverttonum(input_roma)
print(a)
print(sum(a))
