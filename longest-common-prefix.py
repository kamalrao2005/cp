class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1] 
                if not prefix:
                    return ""
        return prefix
def main():
        try:
            raw=input("Enter strs :").strip()
        except ValueError:
            print("Invalid input ")
            return 
        sol = Solution()
        result = sol.longestCommonPrefix(strs)
        print(result)
    
if __name__=="__main__":
        main()
