class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

def main():
    try:
        # Read input: a single line of space-separated integers, e.g., "7 1 5 3 6 4"
        line = input("Enter prices as space-separated integers: ").strip()
        if not line:
            raise ValueError("Input is empty.")

        prices = [int(x) for x in line.split()]
        sol = Solution()
        result = sol.maxProfit(prices)
        print(f"Maximum profit: {result}")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
