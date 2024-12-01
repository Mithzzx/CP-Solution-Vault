class Solution:
    def numberToWords(self, num: int) -> str:

        k=str(num)
        numname = {0: 'Zero ',
                   1: "One",
                   2: "Two",
                   3: "Three",
                   4: "Four",
                   5: "Five",
                   6: "Six",
                   7: "Seven",
                   8: "Eight",
                   9: "Nine",}
        numteen = {0: "Ten",
                   1: "Eleven",
                   2: "Twelve",
                   3: "Thirteen",
                   4: "Fourteen",
                   5: "Fifteen",
                   6: "Sixteen",
                   7: "Seventeen",
                   8: "Eighteen",
                   9: "Nineteen", }
        numten = {2: "Twenty",
                  3: "Thirty",
                  4: "Forty",
                  5: "Fifty",
                  6: "Sixty",
                  7: "Seventy",
                  8: "Eighty",
                  9: "Ninety", }
        tens = {1: "Thousand",
                2: "Million",
                3: "Billion"
                }

        def name(x):
            if x=='0' : return numname[0]
            while len(x) < 3:
                x = '0' + x

            s = ''
            if x[0] != '0': s += numname[int(x[0])] + " Hundred "
            if x[1] not in ('0', '1'):
                s += numten[int(x[1])] + " "
            elif x[1] != '0':
                s += numteen[int(x[2])] + " "
                return s
            if x[2] != '0':
                s += numname[int(x[2])] + " "

            return s

        o = 0
        s = ''
        for i in range(0, len(k), 3):
            if i == 0:
                s = name(k[-3:]) + " " + s
            elif k[o - 3:o] != '000':
                s = name(k[o - 3:o]) + tens[(o / -3)] + " " + s
            o -= 3

        return s[:-2]
