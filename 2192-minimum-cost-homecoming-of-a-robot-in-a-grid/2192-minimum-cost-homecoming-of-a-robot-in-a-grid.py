class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        i,j=startPos
        a,b=homePos
        cost=0
        if i<a:
            for k in range(i,a):
                cost+=rowCosts[k+1]
        else:
            for m in range(a,i):
                cost+=rowCosts[m]
        if j<b:
            for l in range(j,b):
                cost+=colCosts[l+1]
        else:
            for n in range(b,j):
                cost+=colCosts[n]
            
        return cost
"""
Intuition
Since the question asks about the minimum cost, You just have to go straight to the Home without any extra moves, by directly changing the position of Robot to required Row and Column accordingly. Do refer to the Hint if you don't understand what I mean.

Approach
My approach was to simply traverse through the rows and columns between the Start and Home locations and add the cost of corresponding rows and columns to the cost variable.

When the Robot starts at a lower indexed row than the Home, We have to add the cost of the indexes starting from the index of Start's next row, since the Robot is moving to that particular index, including the index of Home's row.
On the contrary, if the Robot starts at a higher indexed row than the Home,We have to add the cost of the indexes starting from the index of the Home to the index of the row, which is just above the Start. The point of this is that the Robot will start to move to the row just above the Home and continue moving upto Home's row. So we are adding the costs of this, just in the Reverse way.
The logic is pretty much same for the Columns.
Complexity
Time complexity:
Space complexity: O(1)




"""