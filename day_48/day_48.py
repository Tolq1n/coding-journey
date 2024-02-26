#12. Integer to Roman
def intToRoman(num):
        """
        :type num: int
        :rtype: str
        """
        dec_rom = {
            1: "I",
            5: "V",
            4: "IV",
            9: "IX",
            10: "X",
            50: "L",
            40: "XL",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        ans = ''
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while n <= num:
                ans += dec_rom[n]
                num-=n
        return ans

intToRoman(9)