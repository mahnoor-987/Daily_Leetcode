class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        res = []
        
        # Check if result is negative
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        
        # Convert to positive for simplicity
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Integer part
        res.append(str(numerator // denominator))
        remainder = numerator % denominator
        
        if remainder == 0:
            return "".join(res)  # No fractional part
        
        res.append(".")
        
        # Dictionary to store seen remainders and their index in result
        remainder_map = {}
        
        while remainder != 0:
            if remainder in remainder_map:
                # Insert '(' at the index where the remainder was first seen
                res.insert(remainder_map[remainder], "(")
                res.append(")")
                break
            
            remainder_map[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(res)

        
