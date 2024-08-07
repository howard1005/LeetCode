class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        funit = [
            "Zero",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]

        sunit = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety"
        ]

        tunit = [
            "Thousand",
            "Million",
            "Billion"
        ]

        def proc2(n):
            if n > 99:
                raise Exception("need 2 digit number")
            ret = ""
            if n > 0 and n < 20:
                ret += funit[n]
            else:
                a = n//10
                b = n%10
                ret += sunit[a]
                if b:
                    ret += " " + funit[n%10]
            return ret

        def proc3(n):
            if n > 999:
                raise Exception("need 3 digit number")
            ret = ""
            a = n//100
            if a != 0:
                ret += funit[a] + " Hundred"
            b = n%100
            if b != 0:
                if ret:
                    ret += " "
                ret += proc2(b)
            return ret
            
        def proc(n):
            ret = ""
            a = n//1000000000
            if a != 0:
                ret += proc3(a) + " " + tunit[2]
            b = (n%1000000000)//1000000
            if b != 0:
                if ret:
                    ret += " "
                ret += proc3(b) + " " + tunit[1]
            c = (n%1000000)//1000
            if c != 0:
                if ret:
                    ret += " "
                ret += proc3(c) + " " + tunit[0]
            d = n%1000
            if d != 0:
                if ret:
                    ret += " "
                ret += proc3(d)
            return ret
        
        ans = proc(num)

        return ans