import re


class solution(object):

    def twosum(self, numbs, target):

        processed_list = re.split(r'\,', numbs)

        print(processed_list)
        print(target)
        length = len(processed_list)
        print('the length is:%s' % length)
        over = 1
        for x in range(0, length):
            for y in range(over, length):
                a = int(processed_list[x]) + int(processed_list[y])
                if a == int(target):
                    return('this is the right: %s,%s,%s' %
                           (processed_list[x], processed_list[y], target))

                # print()
            over = over + 1


test = solution()
test_numbs = input('PLEASE INPUT YOUR NUMBS WITH ",":')
test_target = input('PLEASE INPUT YOUR TARGET:')
a = test.twosum(test_numbs, test_target)
print(a)
