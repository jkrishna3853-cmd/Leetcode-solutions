class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negative = (dividend < 0) != (divisor < 0)

        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        
        quotient = 0

        while dividend_abs >= divisor_abs:
            temp_divisor = divisor_abs
            multiple = 1

            while dividend_abs >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
                
            dividend_abs -= temp_divisor
            quotient += multiple

        if negative:
            quotient = -quotient

        return max(MIN_INT, min(MAX_INT, quotient))