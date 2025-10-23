class Solution:
    def isugly(self, n:int)->bool:
        if n <= 0:
            return False
        for p in [2,3,5]:
            while n % p == 0:
                n //= p
        return n == 1
def main():
        try:
            n=int(input("Enter n :").strip())
        except ValueError:
            print("Invalid input ")
            return 
        sol = Solution()
        result = sol.isugly(n)
        print(result)
    
if __name__=="__main__":
        main()
