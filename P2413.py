class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n%2==0 else n*2
    if n == "main":
        test_value= 5
        result= Solution().smallestEvenMultiple(test_value)
        print(f"The smallest even multiple of {test_value} is:{result}")
    