
def lengthOfLongestSubstring(str):
    longest = 0
    longest_list = None

    for i1 in range(len(str)):
        current_longest = 1
        current_longest_list = []
        for i2 in range(i1, len(str)):
            if i1 != i2:
                print('Comparing {} against {}'.format(str[i1], str[i2]))
                if str[i1] != str[i2]:
                    current_longest += 1
                    current_longest_list.append(str[i2])
                else:
                    break

        if current_longest > longest:
            longest = current_longest
            print(current_longest_list)

    return longest

my_str = 'abcabcbb'

print(lengthOfLongestSubstring(my_str))