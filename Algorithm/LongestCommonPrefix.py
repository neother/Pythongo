import re
import collections
import time


class solution:

    def LongestCommonPrefix(self, strs):

        listofstring = re.split(r',', strs)

        print(listofstring)
        if len(listofstring) < 2:
            return('not enough string')
        newlist = list()
        resultlist = list()
        ini_value = listofstring[0][0]

        x = 0
        y = 0

        try:

            for y in range(len(listofstring)):
                for x in range(len(listofstring)):
                    newlist.append(listofstring[x][y])
                    print(listofstring[x][y])
                    x = x + 1

                if y == 0 and newlist.count(newlist[0][0]) != len(listofstring):

                    print('no common prefix')
                    break

                elif y != 0 and newlist.count(newlist[0][0]) != len(listofstring):
                    break

                else:

                    resultlist.append(newlist[0][0])

                newlist = []
                y = y + 1

            return(''.join(resultlist))
        except Exception as e:
            raise
        # except:
        #    pass
        finally:
            pass


method = solution()
getstrs = input('Input your array of string:')

result = method.LongestCommonPrefix(getstrs)

print('this is the result: %s' % result)

input()
