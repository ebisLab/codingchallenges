class Solution:

    def romanToInt(self, s: str) -> int:
        # print("range", range(len(s))
        print(range(len(s)))

        numeral_to_roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        curr = 0
        prev = 0
        print(s)

        for i in range(len(s)):
            # print('***')
            # print(i)
            curr = numeral_to_roman_map[s[i]]
            print("------")
            print(s[i])
            print('current--> ', curr)
            print('prev-> ', prev)

            if curr > prev:
                total += curr - 2 * prev
                # total = total + curr - 2 * prev
                print(total, '<--total')

            else:
                total += curr
                print(total, '<--total2')

            prev = curr

        return total
