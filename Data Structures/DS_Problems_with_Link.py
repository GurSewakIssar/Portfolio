# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 11:08:08 2025

@author: gurse
"""

# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
# 88. Merge Sorted Array

def merge(nums1, m, nums2 , n):
    
    while n: 
        
        if m and nums1[m-1]>=nums2[n-1]: 
            nums1[m+n-1] = nums1[m-1]  
            m-=1
        else: 
            nums1[m+n-1] = nums2[n-1]
            n-=1 
            
    return nums1


nums1 = [1,2,3,0,0,0] 
m = 3 
nums2 = [2,5,6] 
n = 3


nums1 = [0] 
m = 0 
nums2 = [1] 
n = 1

merge(nums1, m, nums2 , n)


###############################################################################

# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
# 27. Remove Element 

def removeElement(nums, val):
    if not nums: return -1 
    
    def swap(l, r): 
        nums[l] = nums[r]  
        
    l,r = 0,0
    
    for i in range(len(nums)): 
        
        if l != r and nums[r] != val: 
            swap(l, r) 
            l += 1 
            r += 1

            
        elif nums[i] == val: 
            r += 1 
        else: 
            l += 1 
            r += 1 
    
    return len(nums) - l, nums

nums = [3,2,2,3] 
val = 3

nums = [0,1,2,2,3,0,4,2] 
val = 2

removeElement(nums,val)

###############################################################################

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150 
# 26. Remove Duplicates from Sorted Array 

def removeDuplicates(nums):
    if not nums: return -1 
    
    prev = nums[0]
    l, r = 1, 1
    
    def swap(l,r): 
        nums[l] = nums[r]
    
    for i in range(1, len(nums)):
        
        
        if l != r and nums[i] != prev:
            swap(l,r)
            l += 1 
            r += 1 
            prev = nums[i] 
            
            
        elif nums[i] == prev: 
            r += 1  
        
        else: 
            r += 1 
            l += 1 
    
    return l, nums 

nums = [1,1,2]

nums = [0,0,1,1,1,2,2,3,3,4]

removeDuplicates(nums)
        

###############################################################################

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
# 80. Remove Duplicates from sorted Array II 

def removeDuplicates(nums): 
    if not nums: return -1
    
    def swap(l, r): nums[l] = nums[r]
    
    l, r, cnt = 1, 1, 1 
    
    for i in range(1, len(nums)): 
        
        if l==r: 
            if nums[i] == nums[i-1] and cnt <2: 
                cnt += 1 
                l += 1 
                r += 1 
            
            elif nums[i] != nums[i-1]: 
                cnt = 1 
                l += 1 
                r += 1 
            
            else: 
                r += 1 
                cnt += 1
        
        elif l != r: 
            
            if nums[i] != nums[i-1]: 
                swap(l, r) 
                l += 1 
                r += 1 
                cnt = 1 
            
            elif (nums[i] == nums[i-1] and cnt<2):
                swap(l, r) 
                l += 1 
                r += 1 
                cnt += 1 
                
            else:
                r += 1
                cnt += 1 
                
    return l, nums 


nums = [1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]
nums = [1,1,2,2,3,3,3,3,3,4,5,6,6,6]

removeDuplicates(nums)
                

###############################################################################

# 169. Majority Element
# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150 

def majorityElements(nums): 
    if not nums: return -1
    
    cnt = 1 
    idx = 0
    
    for i in range(1,len(nums)): 
        
        if nums[i] != nums[i-1]: 
            cnt -= 1 
        else: 
            cnt += 1 
            
        if not cnt: 
            cnt = 1
            idx = i 
    
    return nums[idx]


nums = [3,2,3]
nums = [2,2,1,1,1,2,2]
nums = [1,2,3,1,2,1,1]

majorityElements(nums)


############################################################################### 

# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150 
# 189. Rotate Array

def rotate(nums, k): 
    if not nums: return 
    
    def rotate_subarray(ar, l, r): 

        while l<r:
            ar[l], ar[r] = ar[r], ar[l] 
            l += 1 
            r -= 1 
    rotate_subarray(nums, 0, len(nums)-1)
    rotate_subarray(nums, 0, k-1) 
    rotate_subarray(nums, k, len(nums)-1) 
    
    return nums
    
nums = [1,2,3,4,5,6,7] 
k = 3

nums = [-1,-100,3,99] 
k = 2

rotate(nums, k)

###############################################################################

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150    
# 121. Best Time to Buy and Sell Stock

def maxProfit(nums):
    if not nums: return
    
    mn = float("infinity") 
    result = float("-infinity")  
    
    for i in nums: 
        mn = min(mn, i) 
        result = max(result, i - mn) 
        
    return result 


prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]

maxProfit(prices)

###############################################################################

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150
# 122. Best Time to Buy and Sell Stock II 

# This is wrong, just change reverse loop to keep track of max of i+1 index and not i index
def maxProfit(prices): 
    profit = 0
    for i in range(1, len(prices)): 
       
        if prices[i]>prices[i-1]: 
            profit += prices[i]-prices[i-1]
        
    return profit


prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
prices = [6,2,5,7,10]

maxProfit(prices)

###############################################################################

# https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150 
# 55. jump Game

def canJump(nums): 
    if not nums: return -1 
    
    jumps = nums[0]
    
    for i in range(1, len(nums)): 
        
        if i == len(nums)-1: 
            return True 
        
        jumps = max(jumps-1, nums[i]) 
        
        if jumps <= 0: return False
    
    return False

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
nums = [3,3,1,0,1,2,0,1]

canJump(nums)

###############################################################################

# https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150

# 45. Jump Game II 

def jump(nums): 
    if not nums: return -1 
    
    dis, mx = nums[0], float("-inf")
    JUMPS = 1 
    
    for i in range(1, len(nums)-1): 
        
        dis -= 1 
        mx = max(mx-1, nums[i]) 
        
        if not dis: 
            JUMPS += 1 
            dis = mx 
        
    return JUMPS 


nums = [2,3,1,1,4]
nums = [2,3,0,1,4]
nums = [3,2,1,2,0,1,2]

jump(nums)
        

############################################################################### 

# https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150 
# 274. H-Index 

def hIndex(citations): 
    
    if not citations: return -1
    
    bucket = [0] * (len(citations) + 1) 
    
    for i in citations: 
        if i >= len(citations): 
            bucket[len(citations)] += 1 
        else: 
            bucket[i] += 1 
            
    count = 0 
    #print(bucket)
    
    for i in range(len(bucket)-1, -1, -1): 
        count += bucket[i] 
        if i <= count: return i  
    
citations = [3,0,6,1,5]
hIndex(citations)
citations = [1,3,1]
hIndex(citations)

###############################################################################

# 380. Insert Delete GetRandom O(1) 
# https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150 

import random
class RandomizedSet: 
    def __init__(self):
        
        
        self.Array = []
        self.Dict = {} 
        
    def insert(self, val): 
        if val in self.Dict: return False 
        self.Dict[val] = len(self.Array) 
        self.Array.append(val) 
        
        return True
    
    def remove(self, val): 
        if val in self.Dict: 
            n = len(self.Array)-1 
            
            self.Array[self.Dict[val]], self.Array[n] = self.Array[n], self.Array[self.Dict[val]] 
            self.Dict[self.Array[self.Dict[val]]] = self.Dict[val]
            self.Array.pop() 
            del self.Dict[val]
            return True
        else: 
            return False
    
    def getRandom(self): 
        
        if self.Array:
            return random.choice(self.Array)
        else: 
            return
            
rs = RandomizedSet()
rs.insert(1) 
rs.remove(2)
rs.insert(2) 
rs.getRandom()
rs.remove(1)
rs.insert(2)
rs.insert(3)
rs.getRandom()

###############################################################################

# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150
# 238. Product of Array Except Self 

def proudctExceptSelf(nums): 
    if not nums: return -1 
    
    temp = [1] * len(nums) 
    
    for i in range(1, len(nums)): 
        temp[i] = temp[i-1] * nums[i-1]
    
    print(temp)
    Sum = 1
    
    for i in range(len(nums)-2, -1, -1): 
        Sum = Sum * nums[i+1]
        temp[i] *= Sum 
        
    return temp
        

nums = [1,2,3,4]
proudctExceptSelf(nums)
nums = [-1,1,0,-3,3]
proudctExceptSelf(nums)

###############################################################################

# https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150
# 134. Gas Station 

def canCompleteCircuit(gas, cost): 
    if not gas or not cost or (len(gas) != len(cost)): return 
    
    SUM = 0  
    
    for i in range(len(gas)): 
        SUM += (gas[i] - cost[i]) 
        
    if SUM <0: return -1 
    
    mx = float("-inf")
    SUM = 0
    idx = None
    for i in range(len(gas)-1, -1, -1): 
        SUM += gas[i]-cost[i]
        
        if SUM>= mx: 
            mx = SUM 
            idx = i 
            
    return idx
    
gas = [1,2,3,4,5] 
cost = [3,4,5,1,2]
canCompleteCircuit(gas, cost)

gas = [2,3,4] 
cost = [3,4,3]
canCompleteCircuit(gas, cost)

gas = [5,4,3,2,1] 
cost = [1,2,3,4,5]
canCompleteCircuit(gas, cost)


###############################################################################

# https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150
# 135. Candy 

def candy(ratings): 
    if not ratings: return  
    
    temp = [1] * len(ratings)
    
    for i in range(1, len(ratings)): 
        if ratings[i] > ratings[i-1]: 
            temp[i] += temp[i-1]
    
    prev = 1
    for i in range(len(ratings)-2, -1, -1): 
        if ratings[i] > ratings[i+1]: 
            prev +=1
            temp[i] = max(prev, temp[i])
        else: 
            prev = 1
            
    return sum(temp)
            
    
ratings = [1,0,2]
candy(ratings)

ratings = [1,2,2]
candy(ratings)

ratings = [5,4,3,2,1,3,2,1,2,3,2]
candy(ratings)

###############################################################################

# https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150
# 42. Trapping Rain Water

def trap(height):
    if not height: return 
    
    temp = [0] * (len(height))
    mx = 0 
    
    for i in range(len(height)): 
        mx = max(mx, height[i]) 
        temp[i] = mx
    
    mx = 0 
    SUM = 0
    for i in range(len(height)-1, -1, -1): 
        mx = max(mx, height[i]) 
        SUM += max(0, min(temp[i], mx) - height[i])
        
    return SUM 

height = [0,1,0,2,1,0,1,3,2,1,2,1]
trap(height)

height = [4,2,0,3,2,5] 
trap(height)


###############################################################################

# https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150 
# 13. Roman to Integer 

def RomanToInt(s): 
    if not s: return -1 
    
    d = {
        "I": 1, 
        "V": 5, 
        "X": 10, 
        "L": 50, 
        "C": 100, 
        "D": 500, 
        "M": 1000
        }
    
    result = 0 
    
    i = len(s)-1
    while i >= 0:
        
        c = d[s[i]]
        
        if i-1>=0 and s[i-1] == "I" and (s[i]=="V" or s[i] == "X"): 
            result += (c-1) 
            i -= 1
        elif i-1>=0 and s[i-1]  == "X" and (s[i]=="L" or s[i] == "C"): 
            result += (c-10)  
            i -= 1
        elif i-1>=0 and s[i-1]  == "C" and (s[i]=="D" or s[i] == "M"): 
            result += (c-100)  
            i -= 1
        else: 
            result += c 
        
        i -= 1
    
    return result  

s = "III"
RomanToInt(s)

s = "LVIII"
RomanToInt(s)

s = "MCMXCIV"
RomanToInt(s)
###############################################################################

# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150
# 58. Length of Last Word 

def LengthOfLastWorld(s): 
    if not s: return
    
    i = len(s)-1
    while i >= 0 and not ((ord(s[i])>= 65 and ord(s[i])<= 90) or(ord(s[i])>= 97 and ord(s[i])<= 122)): 
        i -= 1 
        
    print(i)
    j = i
    while j>= 0 and ((ord(s[j])>= 65 and ord(s[j])<= 90) or(ord(s[j])>= 97 and ord(s[j])<= 122)):
        j -= 1  
    
    return i - j  

s = "Hello World"
LengthOfLastWorld(s)
s = "luffy is still joyboy"
LengthOfLastWorld(s)
s = "   fly me   to   the moon  "
s = " ok "
s = "ll"
LengthOfLastWorld(s)     

###############################################################################

# https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150

# 14. Longest Common Prefix

def longestCommonPrefix(strs): 
    if not strs: return 
    
    idx = 0
    mn = float("inf")
    while idx<mn:
        for i in strs: 
            mn = min(mn, len(i))
            if strs[0][idx] != i[idx]: 
                return strs[0][0:idx] 
        
        idx += 1 
    return strs[0][0:idx] 

strs = ["flower","flow","flight"] 
longestCommonPrefix(strs)

strs = ["dog","racecar","car"]
strs = ["dog","dog","dogq"]
longestCommonPrefix(strs)

###############################################################################

# 6. Zigzag Conversion

# https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150

def convert(s, numRows): 
    if numRows == 1: return s 
    
    _dict = {i: "" for i in range(numRows)} 
    cur = 0 
    flag = 1
    
    for i in range(len(s)): 
        _dict[cur] += s[i] 
        
        if flag:
            cur += 1 
        else: 
            cur -= 1
        
        if flag and cur == numRows: 
            flag = 0 
            cur -= 2
        elif not flag and cur == -1: 
            flag = 1 
            cur = 1  
    
    res = ""
    for i in range(numRows):  
        res += _dict[i] 
        
    return res
        

s = "PAYPALISHIRING" 
numRows = 3
convert(s, numRows)


s = "PAYPALISHIRING" 
numRows = 4
convert(s, numRows)

s = "abcbabcba"
numRows = 3 
convert(s, numRows)            

###############################################################################

# 28. Find the Index of the First Occurrence in a String 
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

def strStr(haystack, needle):
    if not haystack: return -1 
    
    for i in range(len(haystack) - len(needle)): 
        
        if haystack[i: i + len(needle)] == needle: return i 
    
    return -1 

haystack = "sadbutsad" 
needle = "sad" 
strStr(haystack, needle)

haystack = "leetcode" 
needle = "leeto"
strStr(haystack, needle)

haystack = "sjkjokkfjkjsl" 
needle = "okk" 
strStr(haystack, needle)

###############################################################################

# 68. Text Justification 
# https://leetcode.com/problems/text-justification/?envType=study-plan-v2&envId=top-interview-150 

def fullJustify(words, maxWidth): 
    
    l,r = 0, 0
    length = 0
    result = []
    
    while l<len(words): 
        
        if r < len(words) and length + len(words[r]) + r-l <= maxWidth: 
            length += len(words[r])
            r += 1 
        
        else: 
            tot_ws = r - l
            spaces = maxWidth - length
            Espaces = spaces // max(1, (tot_ws - 1))
            ResSpaces = spaces % max(1, (tot_ws - 1))
            
            ## if not last row 
            temp = ""
            if r < len(words): 
                for i in range(l, r): 
                    temp += words[i]  
                    
                    if not i or i < r-1:
                        temp += " " * Espaces 
                        
                        if ResSpaces: 
                            temp += " " 
                            ResSpaces -= 1 
                        
            ## Last Row 
            else:
                for i in range(l, r): 
                    temp += words[i] 
                    
                    if i < r-1:
                        temp += " "
                    
                    else: 
                        temp += " " * (maxWidth - len(temp))  
            
            l = r
            length = 0
            result.append(temp if len(temp) == maxWidth else temp + " " * (maxWidth - len(temp))) 
    
    return result
                        
words = ["This", "is", "an", "example", "of", "text", "justification."] 
maxWidth = 16
fullJustify(words, maxWidth)

words = ["What","must","be","acknowledgment","shall","be"] 
maxWidth = 16
fullJustify(words, maxWidth)

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"] 
maxWidth = 20
fullJustify(words, maxWidth)


############################################################################### 

# 12. Integer to Roman 
# https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150 

def intToRoman(num): 
    num = str(num)
    romanDict = {
        1: "I", 
        4: "IV", 
        5: "V", 
        9: "IX", 
        10: "X", 
        40: "XL", 
        50: "L", 
        90: "XC", 
        100: "C", 
        400: "CD", 
        500: "D", 
        900: "CM", 
        1000: "M", 
        }
    
    def getRoman(n, s):
        if n in romanDict: return (s + romanDict[n])[::-1]
        
        if n>= 1000: 
            return getRoman(n-1000, s + romanDict[1000])
        elif n>= 900: 
            return getRoman(n-900, s + romanDict[900])
        elif n>= 500: 
            return getRoman(n-500, s + romanDict[500])
        elif n>= 400: 
            return getRoman(n-400, s + romanDict[400])
        elif n>= 100: 
            return getRoman(n-100, s + romanDict[100])
        elif n>= 90: 
            return getRoman(n-90, s + romanDict[90])
        elif n>= 50: 
            return getRoman(n-50, s + romanDict[50])
        elif n>= 40: 
            return getRoman(n-40, s + romanDict[40])
        elif n>= 10: 
            return getRoman(n-10, s + romanDict[10])
        elif n>= 9: 
            return getRoman(n-9, s + romanDict[9])
        elif n>= 5: 
            return getRoman(n-5, s + romanDict[5])
        elif n>= 4: 
            return getRoman(n-4, s + romanDict[4])
        elif n>= 1: 
            return getRoman(n-1, s + romanDict[1])
        
    result = ""
    for i in range(len(num)-1, -1, -1): 
        n = int(num[i]) * (10 ** (len(num)-i -1)) 
        result += getRoman(n, "")

        
    return result[::-1]
        
num = 58 
intToRoman(num)

num = 1994
intToRoman(num)

num = 3749
intToRoman(num)           

###############################################################################

# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

def reverseWords(s):
    if not s: return 
    
    i = len(s)-1
    result = ""
    while i >=0:
        
        if s[i] == " ":
            while i>= 0 and s[i] == " ": 
                i -= 1
        else:
            j = i
            while i >= 0 and s[i] != " ": 
                i -= 1  
    
            if not result: 
                result += s[i+1: j+1]
            else:
                result += " " + s[i+1: j+1]
 
    return result
            
        

s = "the sky is blue"
reverseWords(s)
    
s = "  hello world  "
reverseWords(s)
    
s = "a good   example" 
reverseWords(s)
    
###############################################################################

## 125. Valid Palindrome 

## https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150

def isPalindrome(s):
    if len(s) == 1: return True
    l = 0
    r = len(s)-1
    while l<r:

        while l<r and not (ord(s[l].lower())>= 97 and ord(s[l].lower())<= 122): 
            l += 1
            
        while l<r and not (ord(s[r].lower())>= 97 and ord(s[r].lower())<= 122): 
            r -= 1
            
        if s[l].lower() != s[r].lower(): 
            return False 
        
        l += 1 
        r -= 1 
    
    return True
    

s = "A man, a plan, a canal: Panama"
isPalindrome(s) 

s = "race a car"
isPalindrome(s) 

s = "  "
isPalindrome(s)  


###############################################################################

# 392. Is Subsequence 
# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150 

def isSubsequence(s, t) :
    
    if not s and not t: return 
    
    l = 0 
    r = 0 
    
    while l < len(s) and r < len(t): 
        if s[l] == t[r]: l += 1 
        r += 1 
    
    return len(s) == l 


s = "abc" 
t = "ahbgdc" 
isSubsequence(s, t)

s = "axc" 
t = "ahbgdc"
isSubsequence(s, t)


###############################################################################

# 167. Two Sum II - Input Array Is Sorted 

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150 

def twoSum(numbers, target):
    
    l = 0 
    r = len(numbers) -1  
    
    while l<r: 
        if numbers[l] + numbers[r] == target: return [l, r]
        elif numbers[l] + numbers[r] < target: l += 1 
        else : r -= 1
        
    return False

numbers = [2,7,11,15] 
target = 9
twoSum(numbers, target)

numbers = [2,3,4] 
target = 6
twoSum(numbers, target)

numbers = [-1,0] 
target = -1
twoSum(numbers, target)

###############################################################################

# 11. Container With Most Water 

# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150 

def maxArea(height):
    
    l = 0 
    r = len(height) - 1 
    lmax, rmax = height[l], height[r]
    result = float("-inf")
    
    while l<r: 
        
        lmax = max(lmax, height[l]) 
        rmax = max(rmax, height[r])  
        
        result = max(result, min(lmax, rmax) * (r - l)) 
        
        if height[l] > height[r]: r -= 1 
        else: l += 1 
        
    return result 
        
height = [1,8,6,2,5,4,8,3,7] 
maxArea(height)


height = [1,1]
maxArea(height)

height = [1,8,6,2,66, 66, 5,4,8,3,7]
maxArea(height)

############################################################################### 

# 15. 3Sum 

# https://leetcode.com/problems/3sum/?envType=study-plan-v2&envId=top-interview-150 

def threeSum(nums):
    
    nums = sorted(nums) 
    result = []
    
    i = 0
    while i < len(nums)-2: 
        
        while i and i < len(nums)-2 and nums[i] == nums[i-1]: 
            i += 1
            continue
        
        l = i + 1 
        r = len(nums)-1 
        
        while l < r and nums[l] <= 0: 
            if nums[i] + nums[l] + nums[r] == 0:
                result.append((nums[i], nums[l], nums[r])) 
                l += 1
            elif nums[i] + nums[l] + nums[r] > 0: r -= 1 
            else: l += 1  
        
        i += 1
    
    return result 
            
    
    
nums = [-1,0,1,2,-1,-4] 
threeSum(nums)

nums = [0,1,1]
threeSum(nums)

nums = [0,0,0]
threeSum(nums)

nums = [-1,1,-2,2,-3,3,0] 
threeSum(nums)

############################################################################### 

# 209. Minimum Size Subarray Sum 
# https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150

def minSubArrayLen(target, nums):
    
    l = 0 
    r = 0 
    temp = 0 
    result = float("inf") 
    
    while r < len(nums): 
        temp += nums[r]
        
        while l<=r and temp >= target: 
            if temp == target: 
                result = min(result, r - l + 1)
            
            temp -= nums[l] 
            l += 1
            
        r += 1

    return result if result != float("inf") else 0


target = 7 
nums = [2,3,1,2,4,3]
minSubArrayLen(target, nums)

target = 4 
nums = [1,4,4]
minSubArrayLen(target, nums)

target = 11 
nums = [1,1,1,1,1,1,1,1]
minSubArrayLen(target, nums)

target = 10 
nums = [1,2,3,5,2,8]
minSubArrayLen(target, nums)

############################################################################### 

# 3. Longest Substring Without Repeating Characters 
# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-interview-150 


def lengthOfLongestSubstring(s): 
    
    d = set() 
    l, r = 0, 0
    result = 0
    
    while r < len(s): 
        if s[r] not in d: 
            d.add(s[r]) 
            result = max(result, r-l + 1)
        else: 
            while l<= r and s[r] in d: 
                d.remove(s[l]) 
                l += 1  
            
            d.add(s[r])
        
        r += 1  
        
    return result


s = "abcabcbb"
lengthOfLongestSubstring(s)

s = "bbbbb"
lengthOfLongestSubstring(s)

s = "pwwkew"
lengthOfLongestSubstring(s)

s = "pwwkewlarmipkk"
lengthOfLongestSubstring(s)




###############################################################################

# 30. Substring with Concatenation of All Words 
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/?envType=study-plan-v2&envId=top-interview-150 


def findSubstring(s, words): 
    D = {}
    d = {}
    
    for word in words: 
        if word in D: 
            D[word] += 1 
            d[word] = 0
        else: 
            D[word] = 1

    n = len(words[0])
    counter = 0
    l, r = 0, 0 
    result = []
    
    while r < len(s): 
        w = s[r:r+n] 

        
        if w in D:
            if d.get(w, 0) < D[w]: 
                if w in d: 
                    d[w] += 1 
                else: 
                    d[w] = 1 
            
                counter += 1
                r += n 
            else: 
                d = {} 
                d[w] = 1 
                counter = 1 
                l = r  
                r += n
        
        else: 
            d = {} 
            counter = 0 
            r += n 
            l = r 
        
        if counter == len(words): 
            result.append(l) 
            
            d[s[l:l+n]] -= 1 
            l += n 
            counter -= 1 
            
    
    return result
            
                    
            
s = "barfoothefoobarman" 
words = ["foo","bar"]
findSubstring(s, words)

s = "wordgoodgoodgoodbestword" 
words = ["word","good","best","word"]
findSubstring(s, words)

s = "barfoofoobarthefoobarman" 
words = ["bar","foo","the"]
findSubstring(s, words)
            

s = "abbcdcabbcbcabcd"
words = ["ab", "bc", "cd"]    
findSubstring(s, words)    

###############################################################################

# 76. Minimum Window Substring 
# https://leetcode.com/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-interview-150 

def minWindow(s, t):
    if len(t)>len(s): return 
    
    D, d = {}, {}
    for c in t: 
        if c in D: 
            D[c] += 1 
        else: 
            D[c] = 1 
    
    counter = 0 
    result = None
    l, r = 0, 0
    
    while r < len(s):
        w = s[r]
        
        if w in D:
            if d.get(w, 0) < D[w]: 
                counter += 1 
                
            if w in d: 
                d[w] += 1 
            else: 
                d[w] = 1
        
        if counter == len(t): 
            
            while l<=r and (counter>=len(t) or s[l] not in D): 
                if counter == len(t): 
                    if result:
                        if len(s[l:r+1])<len(result): 
                            result = s[l:r+1]  
                    else: 
                        result = s[l:r+1]
                        
                if d.get(s[l], 0):
                    d[s[l]] -= 1 
                    if d[s[l]] < D[s[l]]: 
                        counter -= 1 
                l += 1
 
        
        r += 1 

    return result
                
                
                
                
s = "ADOBECODEBANC" 
t = "ABC" 
minWindow(s, t)

s = "a" 
t = "a"
minWindow(s, t)

s = "a" 
t = "aa"
minWindow(s, t)
                

s = "abcdoitoda" 
t = "adot" 
minWindow(s, t)            
                
###############################################################################

# 36. Valid Sudoku

# https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150 

def isValidSudoku(board):
    Row, Col = {r:set() for r in range(9)}, {c:set() for c in range(9)}
    Cell = {}
    
    for r in range(3): 
        for c in range(3): 
            Cell[(r,c)] = set() 
        
    for r in range(9): 
        for c in range(9): 
            e = board[r][c] 
            if e == ".": continue
        
            if e in Row[r] or e in Col[c] or e in Cell: 
                return False  
            
            Row[r].add(e) 
            Col[c].add(e) 
            Cell[(r//3, c//3)].add(e) 
            
    return True
            
                
                
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
isValidSudoku(board)

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
isValidSudoku(board)


board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","2",".",".",".",".","6","."]
,["5",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
isValidSudoku(board)


###############################################################################

# 54. Spiral Matrix 

# https://leetcode.com/problems/spiral-matrix/?envType=study-plan-v2&envId=top-interview-150 

def spiralOrder(matrix): 
    
    R = len(matrix)
    C = len(matrix[0])
    
    r, c = 0, 0
    
    k = 0
    n = 1 
    result = []
    
    while R and C: 
        
        if k == 0: 
            for i in range(C):
                
                result.append(matrix[r][c])
                c+=1
            c-=1
            r += 1
            
        elif k == 1: 
            for i in range(R):
                
                result.append(matrix[r][c]) 
                r+=1 
            r -= 1 
            c-=1
        
        elif k == 2: 
            for i in range(C):
                
                result.append(matrix[r][c]) 
                c -= 1 
            c+=1 
            r-=1
        
        elif k == 3: 
            for i in range(R):
                
                result.append(matrix[r][c]) 
                r -= 1 
            r += 1 
            c+=1
        
        n += 1 
        k += 1 
        k %= 4
        
        if n == 2: 
            n = 0 
            R -= 1 
            C -= 1 

    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]] 
spiralOrder(matrix)

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
spiralOrder(matrix)

matrix = [[1,2,3,4],[10,11,12,5],[9,8,7,6]]
spiralOrder(matrix)


############################################################################### 

# 48. Rotate Image 

# https://leetcode.com/problems/rotate-image/description/?envType=study-plan-v2&envId=top-interview-150 

def rotate(matrix): 

    l,r = 0, len(matrix)-1 
    n = (r-l) 
    
    while l<r: 
        
        for i in range(n): 
            
            # i, C
            temp = matrix[l+i][r]
            matrix[l+i][r] = matrix[l][l+i]  
            

            # R, (N-i)
            temp2 = matrix[r][l+n-i] 
            matrix[r][l+n-i] = temp

            
            # N-i, l
            temp = matrix[l+n-i][l] 
            matrix[l+n-i][l] = temp2 

            
            # l, i
            matrix[l][l+i] = temp 

            
            
        l += 1 
        r -= 1 
        n = (r-l)
    
    print(matrix)
        

    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix)   


############################################################################### 

# 73. Set Matrix Zeroes 
# https://leetcode.com/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-interview-150 

def setZeroes(matrix):
    m = len(matrix) 
    n = len(matrix[0])
    
    for r in range(m): 
        for c in range(n): 
            if not matrix[r][c]: 
                matrix[r][0] = 0 
                matrix[0][c] = 0 
    
    for r in range(m-1, -1, -1): 
        for c in range(n-1, -1, -1): 
            if not matrix[r][0] or not matrix[0][c]: 
                matrix[r][c] = 0 
    
    print(matrix)
               

matrix = [[1,1,1],[1,0,1],[1,1,1]] 
setZeroes(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)


matrix = [[0,1,2,0,3],[3,4,0,2,1],[1,3,1,5,0],[1,3,1,5,1]]
setZeroes(matrix)

############################################################################### 

# 289. Game of Life 
# https://leetcode.com/problems/game-of-life/?envType=study-plan-v2&envId=top-interview-150 

def gameOfLife(board): 
    
    D = {0: 0, 1: 1, -1: 1, 2: 0}
    RD = {0:0, 1:1, -1:0, 2:1}
    
    r = len(board) 
    c = len(board[0]) 
    
    for i in range(r): 
        for j in range(c):
            
            aa = board[i-1][j-1] if i-1>=0 and j-1>=0 else 0
            bb = board[i-1][j] if i-1>=0 else 0
            cc = board[i-1][j+1] if i-1>=0 and j+1<c else 0
            
            dd = board[i][j-1] if j-1>=0 else 0
            ee = board[i][j+1] if j+1<c else 0 
            
            ff = board[i+1][j-1] if i+1<r and j-1>=0 else 0
            gg = board[i+1][j] if i+1<r else 0
            hh = board[i+1][j+1] if i+1<r and j+1<c else 0
            
            SUM = D[aa] + D[bb] + D[cc] + D[dd] + D[ee] + D[ff] + D[gg] + D[hh] 
            
            if D[board[i][j]] == 0: 
                if SUM == 3: 
                    board[i][j] = 2 
            elif D[board[i][j]] == 1:
                if SUM >= 2 and SUM<=3: 
                    board[i][j] = 1  
                elif SUM <2 or SUM>3: 
                    board[i][j] = -1  
    
    for i in range(r): 
        for j in range(c):
            
            board[i][j] = RD[board[i][j]]
            
    print(board)
                    
    
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]] 
gameOfLife(board)

board = [[1,1],[1,0]]
gameOfLife(board)              

board = [[0,0,1,0],[1,1,1,0], [1,0,1,1], [1,1,0,1]]
gameOfLife(board) 


###############################################################################

# 383. Ransom Note

# https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150 

def canConstruct(ransomNote, magazine):
    
    if len(ransomNote) > len(magazine): return False 
    
    D = {} 
    for i in magazine: 
        if i in D: 
            D[i] += 1 
        else: 
            D[i] = 1 
    
    d = {} 
    
    for i in ransomNote: 
        if i not in D or (i in d and d[i]==D[i]): 
            return False 
        if i in d: 
            d[i] += 1 
        else: 
            d[i] = 1 
            
    return True 

ransomNote = "a" 
magazine = "b"
canConstruct(ransomNote, magazine)

ransomNote = "aa" 
magazine = "ab"
canConstruct(ransomNote, magazine)

ransomNote = "aa" 
magazine = "aab"
canConstruct(ransomNote, magazine)
    
###############################################################################

# 205. Isomorphic Strings

# https://leetcode.com/problems/isomorphic-strings/?envType=study-plan-v2&envId=top-interview-150 

def isIsomorphic(s, t):
    if len(s) != len(t): return False
    
    d = {} 
    
    for i in range(len(s)): 
        if s[i] not in d: 
            d[s[i]] = t[i] 
        else: 
            if d[s[i]] != t[i]: return False 
    
    return True

s = "egg" 
t = "add" 
isIsomorphic(s, t)

s = "foo" 
t = "bar" 
isIsomorphic(s, t)

s = "paper" 
t = "title"
isIsomorphic(s, t)

s = "kalla" 
t = "meppk"
isIsomorphic(s, t)


###############################################################################

# 290. Word Pattern

# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150 

def wordPattern(pattern, s): 
    
    d = {} 
    l, r = 0, 0 
    
    while l<len(pattern) and r < len(s): 
        k = r
        while k < len(s) and s[k] != " ": 
            k += 1 
            
        if pattern[l] not in d: 
            d[pattern[l]] = s[r:k] 
        else: 
            if d[pattern[l]] != s[r:k]: return False 
        
        l += 1 
        r = k + 1 
    
    return True 


pattern = "abba" 
s = "dog cat cat dog" 
wordPattern(pattern, s)

pattern = "abba" 
s = "dog cat cat fish" 
wordPattern(pattern, s)

pattern = "aaaa" 
s = "dog cat cat dog"
wordPattern(pattern, s)


############################################################################### 

# 242. Valid Anagram 

# https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150 

def isAnagram(s, t): 
    
    D = {} 
    
    for i in s: 
        if i not in D: 
            D[i] = 1 
        else: 
            D[i] += 1 
            
    for i in t: 
        
        if i not in D: return False 
        else:  
            D[i] -= 1 
    
    for i in D: 
        if D[i] != 0: return False 
    
    return True

s = "anagram" 
t = "nagaram"
isAnagram(s, t)

s = "rat" 
t = "car"
isAnagram(s, t)


###############################################################################

# 49. Group Anagrams

# https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150 


def groupAnagrams(strs): 
    
    D = {}
    
    for i in strs: 
        d = [0 for i in range(26)]
        
        for e in i:
            d[ord(e)-97] += 1 
        d = tuple(d)
        
        if d in D: 
            D[d].append(i) 
        else: 
            D[d] = [i] 
    
    
    return [i for i in D.values()]
    


strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)

strs = [""] 
groupAnagrams(strs)

strs = ["a"]
groupAnagrams(strs)

#########3##################################################################### 

# 1. Two Sum

# https://leetcode.com/problems/two-sum/?envType=study-plan-v2&envId=top-interview-150

def twoSum(nums, target):
    
    for i in range(len(nums)-1): 
        for j in range(i+1, len(nums)): 
            if nums[i] + nums[j] == target: 
                return [i,j]  

nums = [2,7,11,15] 
target = 9 
twoSum(nums, target)

nums = [3,2,4] 
target = 6 
twoSum(nums, target)

nums = [3,3] 
target = 6
twoSum(nums, target)
            
############################################################################### 

# 202. Happy Number 

# https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150 

def isHappy(n):
    
    n = str(n) 
    d = set()
    
    while True:
        t = 0
        for v in n: 
            t += (int(v))**2 
        
        if t in d: return False 
        elif t == 1: return True 
        
        d.add(t)  
        n = str(t)

n = 19 
isHappy(n)

n = 2
isHappy(n)

n = 1048674346939070979894794179274884403 
isHappy(n)

############################################################################### 

# 219. Contains Duplicate II 

# https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150 

def containsNearbyDuplicate(nums, k): 
    
    D = {}
    d = set() 
    
    for i in range(len(nums)): 
        
        if nums[i] in d: return True

        D[i] = nums[i] 
        d.add(nums[i]) 
        
        if len(d) == k+1: 
            d.remove(D[i-k])
            del D[i-k] 
        
    return False
    

nums = [1,2,3,1] 
k = 3
containsNearbyDuplicate(nums, k)

nums = [1,0,1,1] 
k = 1 
containsNearbyDuplicate(nums, k)

nums = [1,2,3,1,2,3] 
k = 2
containsNearbyDuplicate(nums, k) 

############################################################################### 

# 128. Longest Consecutive Sequence 

# https://leetcode.com/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-interview-150 

def longestConsecutive(nums):
    
    d = set()
    D = {} 
    
    for i in range(len(nums)): 
        d.add(nums[i])  
        
    result = 0
    
    for i in d: 
        k = i
        temp = 0 
        
        if k-1 in D:
            D[i] = D[k-1] + 1  
        else:
            while k-1 in d: 
                temp += 1 
                k-=1 
            
            D[i] = temp + 1 
            
        result = max(result, D[i])  
    
    return result
        

nums = [100,4,200,1,3,2] 
longestConsecutive(nums)

nums = [0,3,7,2,5,8,4,6,0,1]
longestConsecutive(nums)

nums = [1,0,1,2]
longestConsecutive(nums)

###############################################################################

# 228. Summary Ranges

# https://leetcode.com/problems/summary-ranges/?envType=study-plan-v2&envId=top-interview-150 

def summaryRanges(nums): 
    
    l = nums[0] 
    r = nums[0] 
    i = 1 
    result = []
    
    while i<len(nums):
        
        if nums[i]-1 == r: 
            r = nums[i] 
            
        else: 
            if l == r: 
                result.append(str(int(l)))
            else:
                result.append(f"{l}->{r}")  
            
            l,r = nums[i], nums[i]  
        
        i += 1
        
    if l == r: 
        result.append(str(int(l)))
    else:
        result.append(f"{l}->{r}")  
            
    return result
                
            
nums = [0,1,2,4,5,7] 
summaryRanges(nums)

nums = [0,2,3,4,6,8,9]
summaryRanges(nums)


nums = [1,2,3,4,7,8, 13]
summaryRanges(nums)


############################################################################### 

# 56. Merge Intervals 

# https://leetcode.com/problems/merge-intervals/?envType=study-plan-v2&envId=top-interview-150 

def merge(intervals): 
    
    intervals = sorted(intervals) 
    l = intervals[0][0]
    r = intervals[0][1] 
    result = []
    
    for i in range(1, len(intervals)): 
        
        if intervals[i][0]<=r: 
            r = max(intervals[i][1], r) 
        else: 
            result.append([l, r]) 
            
            l = intervals[i][0]
            r = intervals[i][1]  
    
    result.append([l,r])
            
    return result


intervals = [[1,3],[2,6],[8,10],[15,18]]
merge(intervals)

intervals = [[1,4],[4,5]] 
merge(intervals)

intervals = [[4,7],[1,4]]
merge(intervals)           

intervals = [[4,7],[1,4], [6,12],[14,15], [13,21], [10,12]]
merge(intervals) 

############################################################################### 

# 57. Insert Interval

# https://leetcode.com/problems/insert-interval/?envType=study-plan-v2&envId=top-interview-150 

def insert(intervals, newInterval):
    
    if newInterval[1]<intervals[0][0]: 
        temp = [newInterval] 
        for i in intervals: 
            temp.append(i) 
        return temp 
    
    elif newInterval[0]>intervals[-1][1]: 
        temp = [i for i in intervals] 
        temp.append(newInterval)  
        return temp 
    
    else: 
        result = []
        i = 0
        while i < len(intervals) and (
                newInterval[1] < intervals[i][0] or 
                newInterval[0] > intervals[i][1] ):
            result.append(intervals[i])
            i += 1 
        
        l = min(newInterval[0], intervals[i][0])
        r = max(newInterval[1], intervals[i][1]) 
        i += 1 
        
        while i < len(intervals) and intervals[i][0] <= r: 
            r = max(r, intervals[i][1]) 
            i += 1
        
        result.append([l, r]) 
        
        for i in range(i, len(intervals)): 
            result.append(intervals[i]) 
    
    return result
        
        
intervals = [[1,3],[6,9]] 
newInterval = [2,5] 
insert(intervals, newInterval)

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] 
newInterval = [4,8]
insert(intervals, newInterval)

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] 
newInterval = [0,1]
insert(intervals, newInterval)
        
###############################################################################

# 452. Minimum Number of Arrows to Burst Balloons

# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/?envType=study-plan-v2&envId=top-interview-150

def findMinArrowShots(points):
    
    points = sorted(points) 
    
    l = points[0][0]
    r = points[0][1]
    result = 0
    i = 1 
    
    for i in range(1, len(points)): 
        
        if points[i][0]<=r: 
            l = max(l, points[i][0]) 
            r = min(r, points[i][1]) 
        else: 
            result += 1
            l = points[i][0]
            r = points[i][1] 
    
    return result + 1


points = [[10,16],[2,8],[1,6],[7,12]]
findMinArrowShots(points)
points = [[1,2],[3,4],[5,6],[7,8]]
findMinArrowShots(points)
points = [[1,2],[2,3],[3,4],[4,5]]
findMinArrowShots(points)


###############################################################################

# 20. Valid Parentheses 

# https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150 
s = "([)]" 
 
def isValid(s):
    
    d = {
        "(": ")", 
        "[": "]", 
        "{": "}"
        } 
    
    dRev = {
        ")": "(", 
        "]": "[", 
        "}": "{"
        } 
    stack = []
    
    for i in s: 
        if i in d: 
            stack.append(i) 
        else: 
            if stack and stack[-1] == dRev[i]: 
                stack.pop() 
            else: 
                return False
    return not stack


s = "()" 
isValid(s)

s = "()[]{}" 
isValid(s)

s = "(]"
isValid(s)

s = "([])" 
isValid(s)

s = "([)]"
isValid(s)


############################################################################### 

# 71. Simplify Path 

# https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150 

def simplifyPath(path):
    
    stack = []
    
    i = 0 
    
    while i < len(path): 
        
        if path[i] =="/" and stack and stack[-1] == "/": 
            pass  
        elif path[i] == "." and i+2 < len(path) and path[i+2] == "." and path[i+1] == ".": 
            stack.append('.')
            stack.append('.') 
            stack.append('.') 
            i += 2 
        
        elif path[i] == "." and i+1 < len(path) and path[i+1] == ".": 
            i+=1
            if stack:
                stack.pop() 
                while stack and stack[-1] != "/": 
                    stack.pop() 
            
        elif path[i] == ".":  
            i+=1
        
        else: 
            stack.append(path[i]) 
            
        i += 1 
    
    while stack and stack[-1] == "/": 
        stack.pop() 
        
    if not stack: 
        stack.append("/")
        
    return "".join(stack)
                
            
path = "/home/" 
simplifyPath(path)

path = "/home//foo/"
simplifyPath(path)

path = "/home/user/Documents/../Pictures"
simplifyPath(path)

path = "/../"
simplifyPath(path)

path = "/.../a/../b/c/../d/./"
simplifyPath(path)


############################################################################### 

# 155. Min Stack 

# https://leetcode.com/problems/min-stack/?envType=study-plan-v2&envId=top-interview-150 

class MinStack:

    def __init__(self):
        self.list = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.list.append(val) 
        
        if not self.min: 
            self.min.append(val) 
        else: 
            if val<self.min[-1]: 
                self.min.append(val)


    def pop(self) -> None:
        self.min.pop() 
        self.list.pop()
        

    def top(self) -> int:
        return self.list[-1]
        

    def getMin(self) -> int: 
        return self.min[-1] 
    

ms = MinStack()
ms.push(-2) 
ms.push(0) 
ms.push(-3)
ms.getMin() 
ms.pop() 
ms.top() 
ms.getMin() 

############################################################################### 

# 150. Evaluate Reverse Polish Notation

# https://leetcode.com/problems/evaluate-reverse-polish-notation/?envType=study-plan-v2&envId=top-interview-150 
tokens = ["2","1","+","3","*"] 

def evalRPN(tokens):
    if not tokens: return 0
    
    stack = [] 
    
    s = {"+", "-", "/", "*"}
    
    def DoMath(l, r, op): 
        l, r = int(l), int(r)
        
        if op == "+": 
            return l + r
        elif op == "-": 
            return l - r
        elif op == "/": 
            return round(l / r)
        elif op == "*": 
            return l * r
    
    for i in tokens: 
        if i in s: 
            r = stack.pop() 
            l = stack.pop() 
            
            stack.append(DoMath(l,r,i)) 
            
        else: 
            stack.append(i) 
    
    return stack[0]



tokens = ["2","1","+","3","*"] 
evalRPN(tokens)

tokens = ["4","13","5","/","+"]
evalRPN(tokens)

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
evalRPN(tokens)


############################################################################### 

# 224. Basic Calculator 

# https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150 

def calculate(s):
    
    d = {1: [0, "+"]} 
    idx = 0
    
    while idx < len(s):
        i = s[idx]
        
        if i == " ": 
            idx+=1 
            
        elif i in {"+", "-"}: 
            d[len(d)][1] = i 
            idx += 1
        
        elif i == "(": 
            d[len(d)+1] = [0, "+"]  
            idx+=1 
        
        elif i == ")": 
            temp = d[len(d)][0]
            del d[len(d)]
            
            if d[len(d)][1] == "+":
                d[len(d)][0] += temp 
            else: 
                d[len(d)][0] -= temp
            idx+=1 
            
        else: 
            r = idx
            while r<len(s) and ord(s[r])>= 48 and ord(s[r])<=57:
                r += 1 
            if d[len(d)][1] == "+":
                d[len(d)][0] += int(s[idx:r])  
            else: 
                d[len(d)][0] -= int(s[idx:r])
            idx = r  
            
    return d[1][0]


s = "1 + 1"
calculate(s)

s = " 2-1 + 2 "
calculate(s)

s = "(1+(4+5+2)-3)+(6+8)"
calculate(s)

s = "-20+(-4-3-2+9)-(-10-10)"
calculate(s)

############################################################################### 

class ListNode: 
    def __init__(self, val): 
        self.val = val
        self.next = None
        

# 141. Linked List Cycle

# https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150 

def hasCycle(head): 
    
    l = head 
    r = head
    
    while l and r: 
        if r.next != None and r.next.next != None: 
            r = r.next.next 
        else: 
            return False 
        
        l = l.next 
        if l == r: 
            return True 


def createCyclinLL(head, pos):  
    dummy = ListNode(0)
    ll = dummy
    for idx,i in enumerate(head): 
        node = ListNode(i)
        if idx == pos: 
            save = node
        ll.next = node 
        ll = ll.next 
    
    if pos>=0: 
        ll.next = save 
    
    return dummy.next
    
head = [3,2,0,-4] 
pos = 1 
head = createCyclinLL(head, pos)
hasCycle(head)

head.val
head.next.val 
head.next.next.val 
head.next.next.next.val 
head.next.next.next.next.val 
head.next.next.next.next.next.val


head = [1,2] 
pos = 0
head = createCyclinLL(head, pos)
hasCycle(head)

head = [1]
pos = -1 
head = createCyclinLL(head, pos)
hasCycle(head)


############################################################################### 

def CreateLL(vals): 
    dummy = ListNode(0)
    cur = dummy
    
    for val in vals: 
        cur.next = ListNode(val) 
        cur = cur.next 
    
    return dummy.next

def LL_Iter(l): 
    cur = l
    while cur: 
        print(cur.val) 
        cur = cur.next

# 2. Add Two Numbers 

# https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150 

def addTwoNumbers(l1, l2):
    
    dummy = ListNode(0) 
    cur = dummy
    carry = 0 
    
    while l1 or l2: 
        a, b = l1.val if l1 != None else 0 ,  l2.val if l2 != None else 0
        c = (a + b)
        c += carry 
        
        carry = c // 10 
        c = c % 10 

        cur.next = ListNode(c) 
        l1= l1.next if l1 else None
        l2 = l2.next if l2 else None
        cur = cur.next 
        
    if carry: 
        cur.next = ListNode(carry)
    
    return dummy.next
    
l1 = [2,4,3] 
l2 = [5,6,4]
l1 = CreateLL(l1) 
l2 = CreateLL(l2) 

l3 = addTwoNumbers(l1, l2) 
LL_Iter(l3)

l1 = [0] 
l2 = [0]

l1 = CreateLL(l1) 
l2 = CreateLL(l2) 

l3 = addTwoNumbers(l1, l2) 
LL_Iter(l3)

l1 = [9,9,9,9,9,9,9] 
l2 = [9,9,9,9]

l1 = CreateLL(l1) 
l2 = CreateLL(l2) 

l3 = addTwoNumbers(l1, l2) 
LL_Iter(l3)
        
###############################################################################

# 21. Merge Two Sorted Lists

# https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan-v2&envId=top-interview-150 

def mergeTwoLists(list1, list2):
    
    dummy = ListNode(0)
    cur = dummy 
    
    while list1 or list2: 
        
        a = list1.val if list1 != None else 101 
        b = list2.val if list2 != None else 101
        
        if a<b: 
            cur.next = ListNode(a)  
            list1 = list1.next 
        else: 
            cur.next = ListNode(b) 
            list2 = list2.next 
        
        cur = cur.next 
    
    return dummy.next
            

list1 = [1,2,4] 
list2 = [1,3,4] 
list1 = CreateLL(list1)
list2 = CreateLL(list2)
l3 = mergeTwoLists(list1, list2)
LL_Iter(l3)


list1 = [] 
list2 = []
list1 = CreateLL(list1)
list2 = CreateLL(list2)
l3 = mergeTwoLists(list1, list2)
LL_Iter(l3)


## our function is correct, it
list1 = [] 
list2 = [0]

list1 = CreateLL(list1)
list2 = CreateLL(list2)
l3 = mergeTwoLists(list1, list2)
LL_Iter(l3)


############################################################################### 

# 138. Copy List with Random Pointer

# https://leetcode.com/problems/copy-list-with-random-pointer/?envType=study-plan-v2&envId=top-interview-150 

class RandomNode: 
    def __init__(self, val=0, random=None): 
        self.val = val 
        self.random = random
        self.next = None
        
# This is not for this problem, I misunderstood
# def createRandomLL(vals): 
#     d = {} 
    
#     for i, v in enumerate(vals): 
#         d[i] = RandomNode(v[0]) 
        
#     for i, v in enumerate(vals): 
#         d[i].random = d[v[1]] if v[1] != -1 else None
        
#     dummy = RandomNode() 
#     cur = dummy 
    
#     for i in range(len(d)): 
#         cur.next = d[i] 
#         cur = cur.next 
    
#     return dummy.next

def copyRandomLL(head): 
    new = RandomNode() 
    cur = new
    for i in head: 
        cur.next = RandomNode(i[0], i[1])
        cur = cur.next 
    
    return new.next
    

def copyRandomList(head):
    
    d = {} 
    i = 0 
    dummy = head 
    
    while dummy: 
        d[i] = RandomNode(dummy.val, dummy.random) 
        i += 1 
        dummy = dummy.next 
    
    new = RandomNode()
    cur = new 
    
    i = 0
    while i<len(d): 
        cur.next = d[i]
        i += 1 
        cur = cur.next 
        
    return new.next


head = [[7,-1],[13,0],[11,4],[10,2],[1,0]]
head = copyRandomLL(head)
head = copyRandomList(head)

head.val
head.next.random 
head.next.next.val
head.next.next.next.random 
head.next.next.next.next.random
head.next.next.next.next.next.random

head = [[1,1],[2,1]]


head = [[3,null],[3,0],[3,null]]

############################################################################### 

# 92. Reverse Linked List II 

# https://leetcode.com/problems/reverse-linked-list-ii/?envType=study-plan-v2&envId=top-interview-150 

def reverseBetween(head, left, right):
    if left == right: return head 
    
    cur = head
    i = 1 
    
    while i and i < left: 
        i += 1 
        prev = cur
        cur = cur.next 
    
    if left>1: 
        start = prev 
    end = cur 
    
    prev = cur 
    cur = cur.next
    i += 1 
    
    while i <= right: 
        next_ = cur.next 
        cur.next = prev 
        prev = cur 
        cur = next_ 
        i += 1
    
    if left == 1: 
        head = prev 
    else: 
        start.next = prev
    end.next = cur 
    
    return head
        
    
    
head = [1,2,3,4,5] 
left = 2 
right = 4
head = CreateLL(head)
head = reverseBetween(head, left, right)
LL_Iter(head)

head = [5] 
left = 1 
right = 1
head = CreateLL(head)
head = reverseBetween(head, left, right)      
LL_Iter(head)

head = [1,2,3,4,5,6,7,8,9,10] 
left = 1 
right = 8
head = CreateLL(head)
head = reverseBetween(head, left, right)      
LL_Iter(head)


############################################################################### 

# 25. Reverse Nodes in k-Group

# https://leetcode.com/problems/reverse-nodes-in-k-group/?envType=study-plan-v2&envId=top-interview-150  

def reverseKGroup(head, k):
    cur = head 
    K = 0
    while cur: 
        K += 1 
        cur = cur.next 
    
    K = K//k 
    cur = head
    lastPrev = head
    
    while K: 
        i = 1
        
        save = cur 
        prev = cur 
        cur = cur.next
        i+=1
        
        while i <= k: 
            nxt = cur.next 
            cur.next = prev 
            prev = cur 
            cur = nxt
            i += 1
        
        if save == head: 
            head = prev 
        else: 
            lastPrev.next = prev 
            
        lastPrev = save
        
        K-=1  
    lastPrev.next = cur
    
    return head
        
head = [1,2,3,4,5] 
k = 3
head = CreateLL(head) 
head = reverseKGroup(head, k)
LL_Iter(head)

head = [1,2,3,4,5,6,7] 
k = 2
head = CreateLL(head) 
head = reverseKGroup(head, k)
LL_Iter(head)


############################################################################### 

# 19. Remove Nth Node From End of ListNode 

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=study-plan-v2&envId=top-interview-150 

def removeNthFromEnd(head, n):
    
    N = 0 
    cur = head 
    while cur: 
        cur = cur.next 
        N+=1 
        
    if not (N-n): 
        head = head.next 
        return head
    
    cur = head 
    i = 0 
    while i<(N-n): 
        i+=1 
        prev = cur
        cur = cur.next  
    
    prev.next = cur.next 
    
    return head 

head = [1,2,3,4,5] 
n = 2 
head = CreateLL(head) 
head = removeNthFromEnd(head, n) 
LL_Iter(head)

head = [1] 
n = 1 
head = CreateLL(head) 
head = removeNthFromEnd(head, n) 
LL_Iter(head)


head = [1,2] 
n = 1
head = CreateLL(head) 
head = removeNthFromEnd(head, n) 
LL_Iter(head)

############################################################################### 

# 82. Remove Duplicates from Sorted List II 

# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/?envType=study-plan-v2&envId=top-interview-150 

def deleteDuplicates(head): 
    
    cur = head
    left= head
    temp = left
    val = left.val 
    cur = cur.next 
    
    while cur: 
        while cur and cur.val == val: 
            cur = cur.next 
        
        if cur: 
            temp.next = cur 
            temp = temp.next 
            val = cur.val 
            cur = cur.next 
    
    temp.next = None 
    return left

head = [1,2,3,3,4,4,5] 
head = CreateLL(head)
head = deleteDuplicates(head)
LL_Iter(head)

head = [1,1,1,2,3]
head = CreateLL(head)
head = deleteDuplicates(head)
LL_Iter(head)


############################################################################### 

# 61. Rotate List

# https://leetcode.com/problems/rotate-list/?envType=study-plan-v2&envId=top-interview-150 

def rotateRight(head, k):
    
    def reverse(cur, start, end): 
        i = start
        temp = cur 
        i+= 1 
        prev = temp 
        temp = temp.next
        
        while i <= end:
            nxt = temp.next
            temp.next = prev 
            prev = temp
            temp = nxt 
            i += 1 
        
        cur.next = None
        
        return prev, cur, temp # head, tail, next 
    
    K = 0 
    cur = head
    while cur: 
        K += 1 
        cur = cur.next 
    
    head, _, _ = reverse(head, 1, K)  
    
    k = k % K 
    
    left, left_tail, nxt = reverse(head, 1, k) 
    right, right_tail, _ = reverse(nxt, k+1, K) 
    
    left_tail.next = right  
     
    return left
    
    
head = [1,2,3,4,5] 
k = 2 
head = CreateLL(head)
head = rotateRight(head, k)
LL_Iter(head)


head = [0,1,2] 
k = 4
head = CreateLL(head)
head = rotateRight(head, k)
LL_Iter(head)

head = [1,2,3,4,5,6,7] 
k = 10
head = CreateLL(head)
head = rotateRight(head, k)
LL_Iter(head)

############################################################################### 

# 86. Partition List

# https://leetcode.com/problems/partition-list/?envType=study-plan-v2&envId=top-interview-150 

def partition(head, x):
    
    l = ListNode(0) 
    lc = l
    r = ListNode(0)
    rc = r 
    
    cur = head
    while cur: 
        if cur.val<x: 
            lc.next = cur 
            lc = lc.next 
        else: 
            rc.next = cur 
            rc = rc.next 
            
        cur = cur.next 
    
    lc.next = r.next
    rc.next = None 
    
    return l.next


head = [1,4,3,2,5,2]
x = 3

head = CreateLL(head)
head = partition(head, x)
LL_Iter(head)


head = [2,1] 
x = 2
 
head = CreateLL(head)
head = partition(head, x)
LL_Iter(head)


############################################################################### 
# 146. LRU Cache

# https://leetcode.com/problems/lru-cache/?envType=study-plan-v2&envId=top-interview-150  

class DLL: 
    def __init__(self, val = 0, prev = None, next_ = None): 
        
        self.val = val 
        self.next = next_ 
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.DLL = DLL()  
        self.cur = self.DLL
        self.dict = {}
        self.nodeDict = {}
        

    def get(self, key: int):
        if key in self.dict: 
            node = self.dict[key]  
            if node == self.cur: return self.cur.val
            node.prev.next = node.next 
            node.next.prev = node.prev
            node.prev = self.cur
            node.next = None
            self.cur.next = node 
            self.cur = self.cur.next
            return self.dict[key].val
            
        else: 
            return -1
        

    def put(self, key: int, value: int): 
        
        if len(self.dict)<self.capacity:
            node = DLL(value, self.cur) 
            self.nodeDict[node] = key
            self.dict[key] = node
            self.cur.next = node 
            self.cur = self.cur.next 
        
        else: 
            node = self.DLL.next 
            print(node.val)
            idx = self.nodeDict[node] 
            del self.nodeDict[node] 
            del self.dict[idx]  
            node.next.prev = node.prev
            node.prev.next = node.next 
            
            node = DLL(value, self.cur) 
            self.cur.next = node 
            self.cur = self.cur.next 
            
            self.nodeDict[node] = key  
            self.dict[key] = node
            

lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)

lRUCache.DLL.next.val

############################################################################### 

# 104. Maximum Depth of Binary Tree

# https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=top-interview-150

class TreeNode: 
    def __init__(self, val): 
        self.val = val 
        self.left = None 
        self.right = None 
null = None

def createBST(vals): 
    if not vals: return None
    i = 0 
    tree = TreeNode(vals[0])
    temp = [tree]
    
    while i < len(vals): 
        t = []
        
        for v in temp: 
            if v != null:
                if i*2 + 1 < len(vals):
                    
                    if vals[i*2 + 1] != null:
                        left = TreeNode(vals[i*2 + 1]) 
                    else: 
                        left = vals[i*2 + 1]
                    t.append(left)  
                    v.left = left
                    
                    if i*2 + 2 < len(vals):
                        if vals[i*2 + 2] != null: 
                            right = TreeNode(vals[i*2 + 2]) 
                        else: 
                            right = vals[i*2 + 2]
                        t.append(right) 
                        v.right = right 
            else: 
                t.append(null) 
                t.append(null)
                    
            i += 1 
        
        temp = t 
        
    return tree



def maxDepth(root):
    
    def rec(node): 
        if not node: return 0 
        
        l = rec(node.left) 
        r = rec(node.right) 
        
        return 1 + max(l, r) 
    
    return rec(root)
            
root = [3,9,20,null,null,15,7] 
maxDepth(root) 

root = [1,null,2] 
maxDepth(root)  


###############################################################################

# 100. Same Tree

# https://leetcode.com/problems/same-tree/description/?envType=study-plan-v2&envId=top-interview-150

def isSameTree(p, q):
    
    def rec(p, q): 
        if not p and not q: return True
        elif not p and q: return False 
        elif p and not q: return False 
        
        if p.val == q.val: 
            left = rec(p.left, q.left) 
            right = rec(p.right, q.right)  
        else: 
            return False  
    
        return True and left and right
    
    return rec(p, q)



###############################################################################

# 226. Invert Binary Tree

# https://leetcode.com/problems/invert-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150 

def invertTree(root): 
    
    def rec(node): 
        if not node: return None 
        
        left = rec(node.left) 
        right = rec(node.right) 
        
        node.right = left 
        node.left = right 
        
        return node
        
    return rec(root)

root = [4,2,7,1,3,6,9]
invertTree(root)

root = [2,1,3]
invertTree(root)

root = []
invertTree(root)

############################################################################### 

# 101. Symmetric Tree 

# https://leetcode.com/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150
          
# recursive approach  
def isSymmetric(root): 
    if not root: return False 
    
    def rec(left, right):
        if not left and not right: return True 
        elif not left and right: return False 
        elif left and not right: return False 
        
        if left.val == right.val:
            left = rec(left.left, right.right) 
            right = rec(left.right, right.left)  
        else: 
            return False 
        
        return True and left and right 
    
    return rec(root.left, root.right) 

def isSymmetric(root): 
    if not root: return False 
    
    left = [root.left] 
    right = [root.right] 
    
    while left and right: 
        
        if len(left) != len(right): return False 
        
        templ, tempr = [], [0]*len(left)
        
        for i in range(len(left)):  
            r = len(left) - i - 1
            if left[i].val != right[r].val: 
                return False 
            else: 
                if left[i].left:
                    templ.append(left[i].left)
                if left[i].right:
                    templ.append(left[i].right) 
                
                j = r*2
                if right[r].left:
                    tempr[j] = right[r].left
                if right[r].right:
                    tempr[j+1] = right[r].right  
                
        left = templ 
        right = tempr
                 
    return True
                
            
    
    

root = [1,2,2,3,4,4,3] 
isSymmetric(root)

root = [1,2,2,null,3,null,3] 
isSymmetric(root) 

############################################################################### 

# 105. Construct Binary Tree from Preorder and Inorder Traversal

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?envType=study-plan-v2&envId=top-interview-150 

def buildTree(preorder, inorder):
    
    def find(li, v): 
        for i in range(len(li)): 
            if li[i] == v: 
                return i 
    
    def createTree(pre, ino): 
        if not pre:
            return None
        elif len(pre) == 1: 
            return TreeNode(pre[0])
       
        node = TreeNode(pre[0])
        m = find(ino, pre[0])
        
        if m:
            n = find(pre, ino[m-1]) 
        
        if m:
            left = createTree(pre[1: n+1], ino[:m])  
        else: left = None 
        
        if m + 1 == len(preorder): 
            right = None 
        else:
            right = createTree(pre[n+1:], ino[m+1:])
        
        node.left = left 
        node.right = right 
        
        return node
    
    return createTree(preorder, inorder)
        

preorder = [3,9,20,15,7] 
inorder = [9,3,15,20,7] 
node = buildTree(preorder, inorder)

preorder = [-1] 
inorder = [-1]
node = buildTree(preorder, inorder)
        

node.val
node.left.val 
node.right.val 
node.right.left.val 
node.right.right.val        
 
###############################################################################

# 114. Flatten Binary Tree to Linked List

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/?envType=study-plan-v2&envId=top-interview-150 

# inplace
def flatten(root):
    
    if not root: return None 
    
    def rec(node): 
        if not node: return None 
        
        left =  rec(node.left)
        right = rec(node.right) 
        
        if left:
            left.right = right
            left.left = None 
        
        if right:
            right.left = None 
        
        node.right = node.left
        node.left = None 
        
        return right or left or node 

    return root 


# needs dummy LL 

def flatten(root): 
    if not root: return 
    dummy = ListNode(0)
    cur = dummy
    def rec(node): 
        if not node: return None 
        nonlocal cur
        cur.next = ListNode(node.val) 
        cur = cur.next
        
        rec(node.left) 
        rec(node.right)  
         
    rec(root)
    return dummy.next
        
        
        
        
        


root = [1,2,5,3,4,null,6] 
root = flatten(root)

root = [] 
root = flatten(root)

root = [0]
root = flatten(root)

        
############################################################################### 

# 112. Path Sum 

# https://leetcode.com/problems/path-sum/?envType=study-plan-v2&envId=top-interview-150 

def hasPathSum(root, targetSum): 
    if not root: return  
    
    def rec(node, s): 
        if not node:
            if s == targetSum: 
                return True  
            else: 
                return False 
            
        
        left = rec(node.left, s + node.val) 
        right = rec(node.right, s + node.val) 
        
        return left or right 
    
    return rec(root, 0)
    
root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
targetSum = 22 
hasPathSum(root, targetSum)

root = [1,2,3] 
targetSum = 5
hasPathSum(root, targetSum)
 
root = [] 
targetSum = 0
hasPathSum(root, targetSum) 


############################################################################### 

# 129. Sum Root to Leaf Numbers

# https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150 

def sumNumbers(root):
    
    result = 0 
    
    def rec(node, s): 
        if not node:
            nonlocal result
            result += int(s) 
        
        rec(node.left, s + str(node.val))
        rec(node.right, s + str(node.val)) 
        
    
    rec(root, "") 
    return result 

root = [1,2,3] 
sumNumbers(root)


root = [4,9,0,5,1]
sumNumbers(root) 


############################################################################### 

# 124. Binary Tree Maximum Path Sum

# https://leetcode.com/problems/binary-tree-maximum-path-sum/?envType=study-plan-v2&envId=top-interview-150 

def maxPathSum(root):
    if not root: return None
    
    result = 0 
    
    def rec(node): 
        
        if not node: return 0
        
        left = rec(node.left) 
        right = rec(node.right) 
        
        nonlocal result 
        result = max(result, node.val + left + right) 
        
        return node.val + max(left, right) 
     
    rec(root) 
    
    return result

root = [1,2,3] 
maxPathSum(root)

root = [-10,9,20,null,null,15,7] 
maxPathSum(root) 


############################################################################### 

# 173. Binary Search Tree Iterator

# https://leetcode.com/problems/binary-search-tree-iterator/?envType=study-plan-v2&envId=top-interview-150 
            

class BSTIterator:

    def __init__(self, root):
        
        self.bst = createBST(root) 
        self.list = self.getLeft(self.bst) 
        self.list.append(TreeNode(null))
        
        

    def _next(self) -> int:
        if self.list: 
            popped = self.list.pop() 
            if popped.right: 
                temp = self.getLeft(popped.right) 

                self.list.extend(temp)
                return temp[-1].val  
            else: 
                if self.list: 
                    return self.list[-1].val 
                else:
                    return None
        else: 
            return None
    

    def hasNext(self) -> bool: 
        if self.list: 
            if len(self.list)>1:
                return True  
            else: 
                if self.list[-1].right: 
                    return True 
                else: 
                    return False
        else: 
            return False 
        
    def getLeft(self, node): 
        li = []
        while node: 
            li.append(node) 
            node = node.left 
        return li
    
    
bSTIterator = BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator._next()
bSTIterator._next()
bSTIterator.hasNext()
bSTIterator._next()
bSTIterator.hasNext()
bSTIterator._next()
bSTIterator.hasNext()
bSTIterator._next()
bSTIterator.hasNext()

bSTIterator.list

bSTIterator.list[0].val

bSTIterator.bst.val
bSTIterator.bst.left.val
bSTIterator.bst.right.val
bSTIterator.bst.left.left
bSTIterator.bst.left.right
bSTIterator.bst.right.left.val
bSTIterator.bst.right.right.val

############################################################################### 

# 222. Count Complete Tree Nodes

# https://leetcode.com/problems/count-complete-tree-nodes/?envType=study-plan-v2&envId=top-interview-150 

def countNodes(root): 
    if not root: return 0
    lastFlag = 0 
    node = root
    c = 0
    while node: 
        c += 1 
        
        if not node.right: 
            if node.left: 
                c += 1 
                lastFlag = 1 
        
        node = node.right 
    
    return 2**c - lastFlag - 1 

root = [1,2,3,4,5,6] 
root = createBST(root) 
countNodes(root)

root = [] 
root = createBST(root) 
countNodes(root)

root = [1]
root = createBST(root) 
countNodes(root)

############################################################################### 

# 236. Lowest Common Ancestor of a Binary Tree

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/?envType=study-plan-v2&envId=top-interview-150 

def lowestCommonAncestor(root, p, q):
    
    result = None
    def rec(node, l, r): 
        if not node: 
            return l,r

        ll,lr = rec(node.left, l, r) 
        rl,rr = rec(node.right, l, l) 
        
        l = ll or rl or node.val == p 
        r = lr or rr or node.val == q 
        

        nonlocal result
        if result == None:
            if l and r: 
                result = node.val
            
        return l,r
    
    _,__ = rec(root, False, False) 
    return result

root = [3,5,1,6,2,0,8,null,null,7,4] 
root = createBST(root)
p = 5 
q = 1 
lowestCommonAncestor(root, p, q)

root.val 
root.left.val 
root.right.val 

root.left.left.val 
root.left.right.val 
root.right.left.val 
root.right.right.val 
root.left.left.left 
root.left.left.right 
root.left.right.left.val 
root.left.right.right.val


root = [3,5,1,6,2,0,8,null,null,7,4] 
root = createBST(root)
p = 5 
q = 4 
lowestCommonAncestor(root, p, q)


root = [1,2] 
root = createBST(root)
p = 1 
q = 2
lowestCommonAncestor(root, p, q)

############################################################################### 

# 117. Populating Next Right Pointers in Each Node II

# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=study-plan-v2&envId=top-interview-150 

class ListNodeL: 
    def __init__(self, val=None): 
        self.val = val 
        self.nextl = None
        
        
class TreeNode: 
    def __init__(self, val = None): 
        self.val = val 
        self.right = None 
        self.left = None 
        self.next = None
    

def connect(root):
    if not root: return root 
    
    dummy = ListNodeL() 
    dummy.nextl = ListNodeL(root)
    head = dummy.nextl
    
    while head: 
        tail = head 
        prev = None 
        
        dummy1 = ListNodeL()
        temp = dummy1 
        
        while tail: 
            
            if tail.val.left: 
                temp.nextl = ListNodeL(tail.val.left)
                temp = temp.nextl 
            
            if tail.val.right: 
                temp.nextl = ListNodeL(tail.val.right)
                temp = temp.nextl 
            
            if prev: 
                prev.val.next = tail.val
            prev = tail 
            tail = tail.nextl 
        
        head = dummy1.nextl
    
    return root

root = [1,2,3,4,5,null,7]
root = createBST(root)
root = connect(root)

root = []
root = createBST(root)
root = connect(root)

root.next

root.left.next.val
root.right.right.next

############################################################################### 

# 106. Construct Binary Tree from Inorder and Postorder Traversal 

# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/?envType=study-plan-v2&envId=top-interview-150 

def buildTree(inorder, postorder):
    
    if not inorder: return
    
    def find(li, v): 
        for i, val in enumerate(li): 
            if val == v: 
                return i
    
    def rec(ino, po): 
        if not len(ino): return None 
        elif len(ino) == 1:  
            return TreeNode(ino[0])  
        
        node = TreeNode(po[-1])
        I = find(ino, po[-1])  
        
        if I: 
            J = find(po, ino[I-1])  
            left = rec(ino[:I], po[:J+1]) 
            if I == len(ino)-1: 
                right = None  
            else: 
                right = rec(ino[I+1:], po[J+1:-1]) 
            
        else: 
            left = None
            right = rec(ino[I+1:], po[:-1]) 
 
        node.left = left 
        node.right = right 
        
        return node 
    
    return rec(inorder, postorder)
            
        
inorder = [9,3,15,20,7] 
postorder = [9,15,7,20,3] 
root = buildTree(inorder, postorder)

root.val 
root.left.val 
root.right.val 
root.left.left 
root.left.right 
root.right.left.val 
root.right.right.val 
root.right.right.left 

inorder = [-1] 
postorder = [-1] 
root = buildTree(inorder, postorder)
      
############################################################################### 

# 199. Binary Tree Right Side View

# https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=top-interview-150 

def rightSideView(root): 
    if not root: return 
    
    def Iter(nodes): 
        temp = [] 
        for n in nodes: 
            if n.left: 
                temp.append(n.left) 
            if n.right: 
                temp.append(n.right)

    
        return temp 
    
    if root.left:
        left = [root.left] 
    else: 
        left = []  
        
    if root.right:
        right = [root.right] 
    else: 
        right = []  
    
    result = [root.val] 
    
    while left or right: 
        
        templ = Iter(left) 
        tempr = Iter(right) 
  
        if right: 
            result.append(right[-1].val) 
        else: 
            result.append(left[-1].val) 

            
        left = templ 
        right = tempr 

    
    return result

# bfs
def rightSideView(root): 
    if not root: return 
    
    li = [root] 
    result = []
    
    while li: 
        temp = []
        result.append(li[-1].val) 
        
        for n in li: 
            if n.left:
                temp.append(n.left) 
            if n.right:
                temp.append(n.right) 
        
        li = temp 
    
    return result  


        
    

root = [1,2,3,null,5,null,4]
root = createBST(root)
rightSideView(root)

root = [1,2,3,4,null,null,null,5]
root = createBST(root)
rightSideView(root)

root = [1,null,3]
root = createBST(root)
rightSideView(root)       


############################################################################### 

# 637. Average of Levels in Binary Tree

# https://leetcode.com/problems/average-of-levels-in-binary-tree/?envType=study-plan-v2&envId=top-interview-150 

def averageOfLevels(root): 
    if not root: return  
    
    li = [root]  
    liv = [root.val]
    result = []
    
    while li: 
        temp, tempv = [], [] 
        
        for i in li: 
            if i.left: 
                temp.append(i.left) 
                tempv.append(i.left.val)
            if i.right: 
                temp.append(i.right) 
                tempv.append(i.right.val)
        
        result.append(sum(liv)/len(liv)) 
        li = temp 
        liv = tempv 
    
    return result 

root = [3,9,20,null,null,15,7] 
root = createBST(root)
averageOfLevels(root)

root = [3,9,20,15,7]
root = createBST(root)
averageOfLevels(root)        
        
############################################################################### 

# 102. Binary Tree Level Order Traversal

# https://leetcode.com/problems/binary-tree-level-order-traversal/?envType=study-plan-v2&envId=top-interview-150 

def levelOrder(root):
    if not root: return []
    result = [] 

    li = [root] 
    
    while li: 
        liv = []
        temp = [] 
        
        for i in li: 
            liv.append(i.val) 
            
            if i.left: 
                temp.append(i.left) 
                
            if i.right: 
                temp.append(i.right) 
                
        result.append(liv)
        li = temp 
    
    return result 


root = [3,9,20,null,null,15,7]
root = createBST(root)
levelOrder(root) 

root = [1] 
root = createBST(root)
levelOrder(root) 

root = []
root = createBST(root)
levelOrder(root) 


###############################################################################

# 103. Binary Tree Zigzag Level Order Traversal

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/?envType=study-plan-v2&envId=top-interview-150 
    
def zigzagLevelOrder(root): 
    if not root: return [] 
    flag = 0 
    
    result = [] 
    li = [root] 
    
    while li: 
        
        liv = [] 
        temp = [] 
        
        for i in li: 
            liv.append(i.val) 
            
            if i.left: temp.append(i.left) 
            if i.right: temp.append(i.right) 
            
        
        if flag: 
            result.append(liv[-1::-1])  
            flag = 0
        else: 
            result.append(liv)  
            flag = 1 
            
        li = temp 
    
    return result 

root = [3,9,20,null,null,15,7] 
root = createBST(root)
zigzagLevelOrder(root)

root = [1] 
root = createBST(root)
zigzagLevelOrder(root)


root = []
root = createBST(root)
zigzagLevelOrder(root)

            
############################################################################### 

# 230. Kth Smallest Element in a BST
 
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/?envType=study-plan-v2&envId=top-interview-150 

def kthSmallest(root, k):
    
    if not root: return 
    
    result = None 
    
    def rec(node, r): 
        
        if not node: return r
        
        left = rec(node.left, r) 
        left += 1 
        nonlocal result
        if left == k: result = node.val 
        right = rec(node.right, left)  
        
        return right  
    rec(root,0)
    return result 

root = [3,1,4,null,2] 
k = 1
root = createBST(root)
kthSmallest(root, k)

root = [5,3,6,2,4,null,null,1] 
k = 5
root = createBST(root)
kthSmallest(root, k)

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations)
#  and you need to find the kth smallest frequently, how would you optimize?  

############################################################################### 

# 98. Validate Binary Search Tree

# https://leetcode.com/problems/validate-binary-search-tree/?envType=study-plan-v2&envId=top-interview-150 

def isValidBST(root): 
    
    if not root: return False 
    
    def rec(node, start, end): 
        if not node: return True 
        
        left = rec(node.left, start, node.val) 
        right = rec(node.right, node.val, end) 
        
        return left and right and start<node.val<end 
    
    return rec(root, float("-inf"), float("inf")) 


root = [2,1,3] 
root = createBST(root)
isValidBST(root)

root = [5,1,4,null,null,3,6]
root = createBST(root)
isValidBST(root)

############################################################################### 

# 530. Minimum Absolute Difference in BST 

# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/?envType=study-plan-v2&envId=top-interview-150 

def getMinimumDifference(root):
    
    result = float("inf") 
    
    def rec(node, prev): 
        if not node: return prev 
        
        prev = rec(node.left, prev) 
        if prev: 
            nonlocal result
            result = min(result, node.val-prev.val)
        
        right = rec(node.right, node)  
        
        return right
         
    rec(root, None) 
    
    return result

root = [4,2,6,1,3] 
root = createBST(root)
getMinimumDifference(root)

root = [1,0,48,null,null,12,49]
root = createBST(root)
getMinimumDifference(root)


root = [50, 25, 75, 15, 35, 52, 78]
root = createBST(root)
getMinimumDifference(root)


############################################################################### 

# 17. Letter Combinations of a Phone Number

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=top-interview-150 

def letterCombinations(digits):
    if not digits: return [] 
    
    di = {
        "2": ["a", "b", "c"], 
        "3": ["d", "e", "f"], 
        "4": ["g", "h", "i"], 
        "5": ["j", "k", "l"], 
        "6": ["m", "n", "o"], 
        "7": ["p", "q", "r","s"], 
        "8": ["t", "u", "v"], 
        "9": ["w", "x", "y", "z"], 
        } 
    
    result = []
    
    def rec(dig, s): 
        if not dig:
            nonlocal result
            result.append(s) 
            return
            
        for i in di[dig[0]]: 
            rec(dig[1:], s + i) 
    rec(digits, "")
    return result 

digits = "23" 
letterCombinations(digits)

digits = "2"
letterCombinations(digits)

############################################################################### 

# 77. Combinations

# https://leetcode.com/problems/combinations/description/?envType=study-plan-v2&envId=top-interview-150 

def combine(n, k):
    result = []
    def rec(li, st): 
        if len(li) == k:
            nonlocal result 
            result.append(li) 
        
        for i in range(st, n+1): 
            rec(li + [i], i + 1) 
    rec([], 1)
    return result

n = 4 
k = 2
combine(n, k)

n = 1 
k = 1
combine(n, k)

############################################################################### 
# Not SOlved 
# 46. Permutations

# https://leetcode.com/problems/permutations/?envType=study-plan-v2&envId=top-interview-150  

def permute(nums):
    if len(nums) <=1: return [nums]
    result = set()
    li = nums.copy()
    
    def rec(i, li): 
        if i == len(nums)-1: 
            nonlocal result 
            print(li)
            result.add(tuple(li))
            return
        lii = li.copy()
        for _ in range(i, len(nums)):
            #if (tuple(li)) in result: continue
            rec(i+1, lii)  
            if _ < (len(nums)-1):
                lii = li.copy()
                lii[i], lii[_+1] = lii[_+1], lii[i] 
        
    rec(0, li)
    return [i for i in result]
        
nums = [1,2,3] 
permute(nums)

nums = [0,1] 
permute(nums)

nums = [1]
permute(nums)

nums = [1,2,3,4] 
permute(nums)


############################################################################### 

# 39. Combination Sum

# https://leetcode.com/problems/combination-sum/?envType=study-plan-v2&envId=top-interview-150

def combinationSum(candidates, target): 
    result = []
    def rec(i, li, s): 
        
        if s > target: return 
        elif s == target: 
            nonlocal result
            result.append(li.copy()) 
            return
        
        for ii in range(i, len(candidates)): 
            li.append(candidates[ii]) 
            rec(ii, li, s + candidates[ii] )
            li.pop() 
    rec(0, [], 0)
    return result 

candidates = [2,3,6,7]
target = 7 
combinationSum(candidates, target)

candidates = [2,3,5] 
target = 8 
combinationSum(candidates, target)

candidates = [2] 
target = 1
combinationSum(candidates, target)
  
###############################################################################

# 52. N-Queens II

# https://leetcode.com/problems/n-queens-ii/description/?envType=study-plan-v2&envId=top-interview-150 

def totalNQueens(n) -> int:
    
    temp = [[0]*n for i in range(n)] 

    
    def setAttacking(r, c, flag): 
        nonlocal temp, n
        
        for i in range(0, n): 
            if i == c: continue
            temp[r][i] += flag  
        
        for i in range(0, n): 
            temp[i][c] += flag 
            
        rr, cc = r-1, c-1
        while rr>=0 and cc>=0: 
            temp[rr][cc] += flag 
            rr -= 1 
            cc -= 1 
            
        rr, cc = r+1, c+1
        while rr<n and cc<n: 
            temp[rr][cc] += flag 
            rr += 1 
            cc += 1 
            
        rr, cc = r+1, c-1
        while rr<n and cc>=0: 
            temp[rr][cc] += flag 
            rr += 1 
            cc -= 1  
            
        rr, cc = r-1, c+1
        while rr>=0 and cc<n: 
            temp[rr][cc] += flag 
            rr -= 1 
            cc += 1 
            
    result = 0
    def rec(st): 
        if st == n: 
            nonlocal result
            result += 1
            return  
    
        for i in range(n):
            nonlocal temp
            if not temp[st][i]:
                setAttacking(st, i, 1)
                rec(st + 1) 
                setAttacking(st, i,-1)
    
    rec(0) 
    
    return result


n = 4
totalNQueens(n)

n=5
totalNQueens(n)

############################################################################### 

# 22. Generate Parentheses

# https://leetcode.com/problems/generate-parentheses/?envType=study-plan-v2&envId=top-interview-150 

def generateParenthesis(n):
    result = [] 
    
    def rec(o,c,s): 
        if o == n and c == n: 
            nonlocal result 
            result.append(s) 
            return 
        if o>n or c>o: return
        
        rec(o+1, c, s + '(') 
        rec(o, c+1, s + ')')  
    
    rec(0,0,'') 
    return result 

n = 3
generateParenthesis(n)

n = 2
generateParenthesis(n) 

n = 1 
generateParenthesis(n)

n = 4 
generateParenthesis(n)    

############################################################################### 

# 79. Word Search 

# https://leetcode.com/problems/word-search/description/?envType=study-plan-v2&envId=top-interview-150 

def exist(board, word):
    result = False
    def rec(r, c, i, s): 
        if i == len(word) and s == word: 
            nonlocal result 
            result = True
            return  
        elif r <0 or c <0 or r>=len(board) or c>=len(board[0]): 
            return
        
        nonlocal di
                
        if board[r][c] == word[i]: 
            
            if (r+1, c) not in di:
                di.add((r+1,c))
                rec(r+1,c, i+1, s + board[r][c]) 
                di.remove((r+1, c))
                
            if (r, c+1) not in di:
                di.add((r,c+1))
                rec(r,c+1, i+1, s + board[r][c])
                di.remove((r, c+1))
            
            if (r-1, c) not in di:
                di.add((r-1,c))
                rec(r-1,c, i+1, s + board[r][c])
                di.remove((r-1, c))
            
            if (r, c-1) not in di:
                di.add((r,c-1))
                rec(r,c-1, i+1, s + board[r][c])
                di.remove((r, c-1))
                
    for r in range(len(board)): 
        for c in range(len(board[0])):
            di = set()
            rec(r,c, 0, "") 
    return result 

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
word = "ABCCED"
exist(board, word)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
word = "SEE"
exist(board, word)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
word = "ABCB"
exist(board, word)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
word = "EECCBESE"
exist(board, word)


###############################################################################

# 108. Convert Sorted Array to Binary Search Tree

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/?envType=study-plan-v2&envId=top-interview-150

def sortedArrayToBST(nums):
    
    def findMid(li): 
        return len(li)//2
    def rec(li): 
        if li == []: 
            return None 
        elif len(li) == 1: 
            return TreeNode(li[0]) 
        
        m = findMid(li) 
        
        if m:
            left = rec(li[:m])  
        else: 
            left = None
        right = rec(li[m+1:]) 
        
        node = TreeNode(li[m]) 
        node.left = left 
        node.right = right 
        
        return node 
    
    return rec(nums)

nums = [-10,-3,0,5,9] 
root = sortedArrayToBST(nums) 
root.val 
root.left.val 
root.right.val 
root.left.left.val 
root.right.left.val

nums = [1,3]
root = sortedArrayToBST(nums)      

############################################################################### 

# 148. Sort List

# https://leetcode.com/problems/sort-list/?envType=study-plan-v2&envId=top-interview-150 

def sortList(head):
    
    def findMid(ll, n):  
        m = n//2 
        dummy = ListNode(0) 
        temp = dummy 
        i = 0
        while i <m: 
            i+=1 
            temp.next = ll 
            ll = ll.next 
            temp = temp.next 
            
        temp.next = None 
        return dummy.next, ll, m, n-m
    
    def rec(ll, n):  
        if not ll: 
            return None 
        if not ll.next: 
            return ListNode(ll.val) 
        
        l,r,ln,rn = findMid(ll, n)
        left = rec(l,ln) 
        right = rec(r, rn) 
        
        dummy = ListNode(0) 
        temp = dummy 
        
        while left or right: 
            lv = left.val if left else float('inf') 
            rv = right.val if right else float('inf')
            
            if lv < rv: 
                temp.next = left 
                temp = temp.next 
                left = left.next  
            else: 
                temp.next = right 
                temp = temp.next 
                right = right.next 
                
        return dummy.next 
    
    i = 0 
    temp = head
    while temp: 
        temp = temp.next
        i += 1 
    return rec(head, i)
                
        
head = [4,2,1,3] 
head = CreateLL(head)
head = sortList(head) 
LL_Iter(head)


head = [-1,5,3,4,0] 
head = CreateLL(head)
head = sortList(head) 
LL_Iter(head)

head = [] 
head = CreateLL(head)
head = sortList(head) 
LL_Iter(head)

############################################################################### 

# 23. Merge k Sorted Lists

# https://leetcode.com/problems/merge-k-sorted-lists/?envType=study-plan-v2&envId=top-interview-150

def mergeKLists(lists):

    if lists == [] or lists[0] == []: return []
    
    def findMid(li): 
        return len(li)//2
    
    def rec(li): 
        if li == []: return None 
        elif len(li) == 1: return li[0]   
        
        m = findMid(li) 
        
        left = rec(li[:m])
        right = rec(li[m:]) 
        
        dummy = ListNode(0) 
        temp = dummy
        while left or right: 
            lv = left.val if left else float("inf") 
            rv = right.val if right else float('inf') 
            
            if lv < rv : 
                temp.next = left 
                left = left.next 
                temp = temp.next
            else: 
                temp.next = right 
                right = right.next 
                temp = temp.next 
        
        return dummy.next 
    
    return rec(lists)

def createListedLL(lists): 
    temp = [] 
    for i in lists: 
        temp.append(CreateLL(i)) 
    return temp
        
lists = [[1,4,5],[1,3,4],[2,6]] 
lists = createListedLL(lists)
head = mergeKLists(lists) 
LL_Iter(head) 

lists = [] 
lists = createListedLL(lists)

lists = [[]]
lists = createListedLL(lists)  
    

############################################################################### 

# 53. Maximum Subarray

# https://leetcode.com/problems/maximum-subarray/?envType=study-plan-v2&envId=top-interview-150 

def maxSubArray(nums):
    
    temp = float("-inf") 
    result = float("-inf")
    
    for i in nums:
        if i > temp: 
            temp = i  
        else: 
            temp += i 
    
        result = max(result, temp) 
    
    return result
         

nums = [-2,1,-3,4,-1,2,1,-5,4] 
maxSubArray(nums)

nums = [1] 
maxSubArray(nums)

nums = [5,4,-1,7,8]
maxSubArray(nums)

############################################################################### 

# 918. Maximum Sum Circular Subarray

# https://leetcode.com/problems/maximum-sum-circular-subarray/?envType=study-plan-v2&envId=top-interview-150 

def maxSubarraySumCircular(nums):      
    total = 0 
    mxSum, curMx = nums[0], 0 
    mnSum, curMn = nums[0], 0 
    for ele in nums: 
        total += ele
        
        curMx = max(curMx+ele, ele) 
        mxSum = max(mxSum, curMx) 
        curMn = min(curMn + ele, ele) 
        mnSum = min(mnSum, curMn) 
    
    return max(mxSum, total - mnSum) if mxSum>0 else mxSum 

nums = [1,-2,3,-2]
maxSubarraySumCircular(nums)
nums = [5,-3,5]
maxSubarraySumCircular(nums)
nums = [-3,-2,-3]
maxSubarraySumCircular(nums)
nums = [2, -2, 3, 4, -8, 5, 6]
maxSubarraySumCircular(nums)
        
############################################################################### 

# 35. Search Insert Position 

# https://leetcode.com/problems/search-insert-position/description/?envType=study-plan-v2&envId=top-interview-150 

def searchInsert(nums, target): 
    
    def findMid(st, end): 
        return st + ((end-st+1)//2 )
    
    def rec(st, end): 
        if st>end: 
            return st  
        
        m = findMid(st, end) 
        if nums[m] == target: return m 
        return rec(m+1, end) if nums[m]<target else rec(st, m-1) 
        
    return rec(0, len(nums)-1) 

nums = [1,3,5,6] 
target = 5 
searchInsert(nums, target)

nums = [1,3,5,6] 
target = 2 
searchInsert(nums, target)

nums = [1,3,5,6] 
target = 7
searchInsert(nums, target)       

############################################################################### 

# 74. Search a 2D Matrix 

# https://leetcode.com/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=top-interview-150 

def searchMatrix(matrix, target):
    r = len(matrix) 
    c = len(matrix[0])
    
    def FindMid(st, end): 
        m = end-st
        m = st + m // 2 
        row = m//c 
        col = m - (row*c) 
        return row,col
    
    def rec(st, end): 
        if st>end: return False  
        
        row, col = FindMid(st, end)  
        if matrix[row][col] == target: return True 
        
        return rec(row*c + col + 1, end) if matrix[row][col] < target else rec(st, row*c + col - 1)  
    
    return rec(0, r * c - 1)
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 3 
searchMatrix(matrix, target)

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 13
searchMatrix(matrix, target)       
        
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 16
searchMatrix(matrix, target)   

###############################################################################

# 162. Find Peak Element

# https://leetcode.com/problems/find-peak-element/?envType=study-plan-v2&envId=top-interview-150

def findPeakElement(nums):
    
    def findMid(st, end): 
        return st + (end-st)//2
    
    def rec(st, end): 
        m = findMid(st, end) 
        
        l = nums[m-1] if m-1>=0 else float("-inf")
        r = nums[m+1] if m+1<len(nums) else float("-inf")
        if l<nums[m] and nums[m]>r: return m 
        
        return rec(m+1, end) if nums[m]>l else rec(st, m-1) 
    
    return rec(0, len(nums)-1) 

nums = [1,2,3,1] 
findPeakElement(nums)

nums = [1,2,1,3,5,6,4]
findPeakElement(nums)

nums = [1,2]
findPeakElement(nums)

nums = [7,5,4,3,9,8]
findPeakElement(nums)
 

############################################################################### 

# 33. Search in Rotated Sorted Array

# https://leetcode.com/problems/search-in-rotated-sorted-array/?envType=study-plan-v2&envId=top-interview-150 

def search(nums, target):  
    
    def findMid(st, end): 
        return st + (end-st)//2 
    
    def rec(st, end): 
        if st>end: return -1 
        
        m = findMid(st, end) 
        
        if nums[m] == target: return m 
        
        if nums[st]> nums[m]:
            if m+1<len(nums) and nums[m+1]<=target<=nums[end]: 
                return rec(m+1, end)  
            else: 
                return rec(st, m-1)
        else: 
            if m-1>=0 and nums[st]<= target <= nums[m-1]: 
                return rec(st, m-1) 
            else: 
                return rec(m+1, end)
            
            
    return rec(0, len(nums)-1) 


nums = [4,5,6,7,0,1,2] 
target = 0 
search(nums, target)

nums = [4,5,6,7,0,1,2] 
target = 3 
search(nums, target)

nums = [1] 
target = 0
search(nums, target)

nums = [7,0,1,2,3,4,5] 
target = 4 
search(nums, target)


############################################################################### 

# 34. Find First and Last Position of Element in Sorted Array 

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=study-plan-v2&envId=top-interview-150

def searchRange(nums, target):
    if not nums: return [-1,-1]
    
    def findMid(st, end): 
        return st + (end-st)//2 
    
    _min = float('inf')
    _max = float("-inf")
    
    def rec(st, end): 
        if st > end: return 
        
        m = findMid(st, end)
        if nums[m] == target:
            nonlocal _min, _max
            _min = min(_min, m) 
            _max = max(_max, m)
            
            rec(st, m-1) 
            rec(m+1, end) 
        else: 
            if nums[m]>target: return rec(st, m-1) 
            else: return rec(m+1, end)
            
    rec(0, len(nums)-1)
    return[_min if _min != float("inf") else -1, _max if _max != float("-inf") else -1]


nums = [5,7,7,8,8,10] 
target = 8 
searchRange(nums, target)

nums = [5,7,7,8,8,10] 
target = 6 
searchRange(nums, target)

nums = [] 
target = 0
searchRange(nums, target)

nums = [5,8,8,8,10] 
target = 10
searchRange(nums, target)

############################################################################### 

# 153. Find Minimum in Rotated Sorted Array

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/?envType=study-plan-v2&envId=top-interview-150 

def findMin(nums):
      
    def findMid(st, end): 
        return st + (end-st)//2 
    
    _min = float("inf")
    def rec(st, end): 
        if st>end: return 
        
        m = findMid(st, end) 
        
        nonlocal _min
        _min = min(_min, nums[m])
        if nums[st]<=nums[m]: 
            _min = min(_min, nums[st])
            rec(m + 1, end) 
        else: 
            rec(st, m-1)
            
    rec(0, len(nums)-1) 
    return _min 

nums = [3,4,5,1,2] 
findMin(nums)

nums = [4,5,6,7,0,1,2] 
findMin(nums)

nums = [11,13,15,17]
findMin(nums)       

nums = [7,9,10,1]
findMin(nums)  

nums = [7,8,9,0,1,2,3,4]
findMin(nums)  

############################################################################### 

# 4. Median of Two Sorted Arrays 

# https://leetcode.com/problems/median-of-two-sorted-arrays/?envType=study-plan-v2&envId=top-interview-150 

def findMedianSortedArrays(nums1, nums2): 
    
    def findMid(li): 
        return (len(li)-1)//2
    K = len(nums1) + len(nums2)
    k = (len(nums1) + len(nums2)-1)//2
    
    def rec(m):
        nonlocal k, K
        n = k-m-1
        
        ll, lr = nums1[m] if m>=0 else float("-inf"), nums1[m+1] if m+1 < len(nums1) else float("inf")
        rl, rr = nums2[n] if n>=0 else float("-inf"), nums2[n+1] if n+1 < len(nums2) else float("inf")
        
        if ll <= rr and rl <= lr: 
            if not K%2: 
                return (max(ll,rl) + min(lr, rr))/2 
            else: 
                return max(ll, rl) 
            
        else: 
            if ll<rr: 
                return rec(m+1)
            else: 
                return rec(m-1) 
   
    if len(nums1)>len(nums2): 
        m = findMid(nums2) 
        nums1, nums2 = nums2, nums1
    else: 
        m = findMid(nums1) 
        
    return rec(m)
        
nums1 = [1,3] 
nums2 = [2] 
findMedianSortedArrays(nums1, nums2)


nums1 = [1,2] 
nums2 = [3,4]
findMedianSortedArrays(nums1, nums2)

nums1 = [1,2,3,4] 
nums2 = [7,8,9]
findMedianSortedArrays(nums1, nums2)

nums1 = [1,2,3,4,5,6] 
nums2 = [7,8,9]
findMedianSortedArrays(nums1, nums2)

###############################################################################

# 215. Kth Largest Element in an Array

# https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=study-plan-v2&envId=top-interview-150

# space comp = N, Time comp = nlogk
def findKthLargest(nums, k): 
    
    import heapq 
    nums = [-i for i in nums]
    heapq.heapify(nums) 
    
    for i in range(k): 
        pop = heapq.heappop(nums) 
    
    return -pop

#space comp = K, TIme Comp = nlogk
def findKthLargest(nums, k): 
    
    import heapq 
    heap = nums[:k]
    heapq.heapify(heap) 
    
    for i in nums[k:]: 
        if i > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,i) 
    
    return heap[0]

nums = [3,2,1,5,6,4] 
k = 2
findKthLargest(nums, k)

nums = [3,2,3,1,2,4,5,5,6]
k = 4
findKthLargest(nums, k)

## exercise, Quickselect Implementation

############################################################################### 

# 502. IPO

# https://leetcode.com/problems/ipo/description/?envType=study-plan-v2&envId=top-interview-150

# N Space, kN Time
def findMaximizedCapital(k, w, profits, capital):
    import heapq
    heap = [] 
    heapq.heapify(heap)
    result = 0
    Cap = w
    s = set()
    
    for i in range(k): 
        for idx,c in enumerate(capital): 
            if Cap>=c and idx not in s: 
                heapq.heappush(heap, -profits[idx]) 
                s.add(idx)
        
        pop = heapq.heappop(heap)
        Cap += (-pop) 
        result += (-pop)
        
    
    return result


# space = N, Time = N
def findMaximizedCapital(k, w, profits, capital):
    import heapq
    heap = [[capital[i],-profits[i]] for i in range(len(profits))]
    heapq.heapify(heap)
    prof = [] 
    heapq.heapify(prof)
    cap = w 
    result = 0
    
    for i in range(k): 
        n = len(heap)
        j =0
        while j<n:
            if heap[0][0]<=cap: 
                pop = heapq.heappop(heap)
                heapq.heappush(prof, pop[1])   
            j+=1
        
        pop = heapq.heappop(prof) 
        cap += (-pop) 
        result += (-pop) 
    
    return result 



k = 2 
w = 0 
profits = [1,2,3] 
capital = [0,1,1] 
findMaximizedCapital(k, w, profits, capital)


k = 3 
w = 0 
profits = [1,2,3] 
capital = [0,1,2]
findMaximizedCapital(k, w, profits, capital)

############################################################################### 

# 373. Find K Pairs with Smallest Sums 

# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/?envType=study-plan-v2&envId=top-interview-150 

def kSmallestPairs(nums1, nums2, k):
    if k > len(nums1)*len(nums2): return "Pagal Vagal ho kya?"
    import heapq
    result = [] 
    heap = [] 
    heapq.heapify(heap) 
    heapq.heappush(heap, [(nums1[0]+nums2[0]),0,0])
    Set = set() 
    Set.add((0,0))
    
    for i in range(k) :
        pop = heapq.heappop(heap)
        result.append([nums1[pop[1]],nums2[pop[2]]]) 
        
        m, n = pop[1], pop[2]
        
        if m+1<len(nums1) and n+1<len(nums2): 
            if (m+1, n) not in Set: 
                Set.add((m+1, n)) 
                heapq.heappush(heap, [(nums1[m+1]+nums2[n]), m+1, n]) 
            
            if (m, n+1) not in Set:
                Set.add((m, n+1)) 
                heapq.heappush(heap, [(nums1[m]+nums2[n+1]), m, n+1]) 
        
        else: 
            
            if m+1 < len(nums1): 
                if (m+1, n) not in Set: 
                    Set.add((m+1, n)) 
                    heapq.heappush(heap, [(nums1[m+1]+nums2[n]), m+1, n])  
            elif n+1 < len(nums2): 
                if (m, n+1) not in Set:
                    Set.add((m, n+1)) 
                    heapq.heappush(heap, [(nums1[m]+nums2[n+1]), m, n+1])  

    return result
        
                    
                    
nums1 = [1,7,11] 
nums2 = [2,4,6] 
k = 3 
kSmallestPairs(nums1, nums2, k)

nums1 = [1,1,2] 
nums2 = [1,2,3] 
k = 10
kSmallestPairs(nums1, nums2, k)        

############################################################################### 

# 295. Find Median from Data Stream

# https://leetcode.com/problems/find-median-from-data-stream/?envType=study-plan-v2&envId=top-interview-150

import heapq
class MedianFinder:
    
    def __init__(self):
        
        
        self.l1 = [] 
        self.l2 = [] 
        
        

    def addNum(self, num: int) -> None:
        
        
        if len(self.l2)<len(self.l1): 
            if -num<self.l1[0]: 
                heapq.heappush(self.l2, num) 
            else: 
                pop = heapq.heappop(self.l1) 
                heapq.heappush(self.l1, -num) 
                heapq.heappush(self.l2, -pop) 
        else: 
            
            if self.l2 and num>self.l2[0]: 
                pop = heapq.heappop(self.l2) 
                heapq.heappush(self.l2, num) 
                heapq.heappush(self.l1, -pop) 
            else: 
                heapq.heappush(self.l1, -num) 
                


    def findMedian(self) -> float:
        
        if not (len(self.l1) + len(self.l2))%2: 
            return ((-self.l1[0]) + self.l2[0])/2 
        else: 
            return -self.l1[0] 

medianFinder = MedianFinder()
medianFinder.addNum(1) # arr = [1]
medianFinder.addNum(2)#    // arr = [1, 2]
medianFinder.findMedian()# // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)#    // arr[1, 2, 3]
medianFinder.findMedian()# // return 2.0

############################################################################### 

# 70. Climbing Stairs

# https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=top-interview-150 

def climbStairs(n):
    if n<=2: return n 
    a = 1 
    b = 2 
    
    for i in range(2, n): 
        a, b = b, a+b 
    return b 

n = 2 
climbStairs(n)

n = 3 
climbStairs(n)

n = 5
climbStairs(n)

############################################################################### 

# 198. House Robber

# https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=top-interview-150 

def rob(nums):
    if len(nums)<=2: return max(nums)
    
    for i in range(2,len(nums)): 
        if nums[i]+nums[i-2]>nums[i-1]: 
            nums[i] = nums[i] + nums[i-2] 
        else: 
            nums[i] = nums[i-1] 
    return nums[-1]

nums = [1,2,3,1] 
rob(nums)

nums = [2,7,9,3,1]
rob(nums)

nums = [1,2,5,6,8,1,3]
rob(nums)

############################################################################### 

# 139. Word Break 

# https://leetcode.com/problems/word-break/?envType=study-plan-v2&envId=top-interview-150 

def wordBreak(s, wordDict): 
    A = [0]*len(s) 
    
    for i in range(len(s)-1, -1, -1): 
        for w in wordDict: 
            if s[i-len(w)+1:i+1] == w: 
                if i + 1< len(s) and A[i+1]: 
                    A[i-len(w)+1] = 1 
                elif i+1>=len(s): 
                    A[i-len(w)+1] = 1  
    
    return A[0] == 1

s = "leetcode" 
wordDict = ["leet","code"]
wordBreak(s, wordDict)

s = "applepenapple" 
wordDict = ["apple","pen"]
wordBreak(s, wordDict)

s = "catsandog" 
wordDict = ["cats","dog","sand","and","cat"]
wordBreak(s, wordDict)

s = "noknotokshok" 
wordDict = ["ok","no","tokshok"]
wordBreak(s, wordDict)

############################################################################### 

# 322. Coin Change

# https://leetcode.com/problems/coin-change/description/?envType=study-plan-v2&envId=top-interview-150 

def coinChange(coins, amount):
    
    A = [amount]*(amount+1) 
    A[0] = 0 
    Set = set() 
    Set.add(0)
    
    for k in range(1,amount+1): 
        for i in coins: 
            
            if i<=k: 
                m = k//i 
                rem = k%i
                if rem==0 or rem in Set: 
                    A[k] = min(A[k], m + A[rem]) 
                    Set.add(k)
    
    return A[amount] if amount in Set else -1

coins = [1,2,5] 
amount = 11
coinChange(coins, amount)

coins = [2] 
amount = 3
coinChange(coins, amount)

coins = [1] 
amount = 0
coinChange(coins, amount)

coins = [1,2,6,7] 
amount = 20
coinChange(coins, amount)

# exercise 
# do it with some other method

############################################################################### 

# 300. Longest Increasing Subsequence

# https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=study-plan-v2&envId=top-interview-150 

def lengthOfLIS(nums):
    
    def search(li, v):
        def mid(st, end): 
            return st + (end-st)//2
        def rec(st, end, v):
            if st>end:return st
            
            m = mid(st, end) 
            nonlocal li 
            
            if li[m]>v: return rec(st, m-1, v) 
            else: return rec(m+1, end, v) 
            
        return rec(0, len(li)-1, v)  
    
    result = []
    for i in nums: 
        if not result: result.append(i) 
        elif i>result[-1]: result.append(i) 
        
        else:
            m = search(result,i) 
            result[min(m, len(result)-1)] = i 
    
    return len(result)

nums = [10,9,2,5,3,7,101,18]
lengthOfLIS(nums)

nums = [0,1,0,3,2,3] 
lengthOfLIS(nums)

nums = [7,7,7,7,7,7,7]
lengthOfLIS(nums)   
    
            
############################################################################### 

# 120. Triangle

# https://leetcode.com/problems/triangle/?envType=study-plan-v2&envId=top-interview-150 

def minimumTotal(triangle):
    temp = triangle[-1] 
    
    for i in range(len(triangle)-2, -1, -1): 
        for idx in range(len(triangle[i])) :
            temp[idx] = min(temp[idx+1],temp[idx]) + triangle[i][idx]
    
    return temp[0]

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]] 
minimumTotal(triangle)

triangle = [[-10]]
minimumTotal(triangle)      
        
############################################################################### 

# 64. Minimum Path Sum

# https://leetcode.com/problems/minimum-path-sum/?envType=study-plan-v2&envId=top-interview-150 

def minPathSum(grid): 
    
    temp = [0] * len(grid[0]) 
    
    for r in range(len(grid)-1, -1, -1): 
        for c in range(len(grid[r])-1, -1, -1): 
            
            down, right = temp[c] if r<len(grid)-1 else float("inf"), temp[c+1] if c+1<len(grid[r]) else float("inf") 
            
            temp[c] = grid[r][c] + (min(down,right) if min(down,right)!=float("inf") else 0)
    
    return temp[0]


grid = [[1,3,1],[1,5,1],[4,2,1]] 
minPathSum(grid)

grid = [[1,2,3],[4,5,6]]
minPathSum(grid)

     
############################################################################### 

# 63. Unique Paths II

# https://leetcode.com/problems/unique-paths-ii/?envType=study-plan-v2&envId=top-interview-150 

def uniquePathsWithObstacles(obstacleGrid):
    
    row = len(obstacleGrid) 
    col = len(obstacleGrid[0]) 
    temp = [0] * col 
    temp[-1] = 1 if obstacleGrid[-1][-1]==0 else 0
    
    for r in range(row-1, -1, -1): 
        for c in range(col-1, -1, -1): 
            if r == row-1 and c == col-1: continue
            
            down = temp[c] if r+1< row else 0 
            right = temp[c+1] if c+1<col else 0 
            
            if not obstacleGrid[r][c]:
                temp[c] = down+right
            else: 
                temp[c] = 0 
                
    return temp[0] 

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]] 
uniquePathsWithObstacles(obstacleGrid)

obstacleGrid = [[0,1],[0,0]]
uniquePathsWithObstacles(obstacleGrid)

obstacleGrid = [[0,0,0],[0,0,0],[0,0,0]] 
uniquePathsWithObstacles(obstacleGrid)

obstacleGrid = [[0,0,0,0],[0,1,0,0],[0,0,0,0], [0,0,0,0]] 
uniquePathsWithObstacles(obstacleGrid)

###############################################################################

# 97. Interleaving String

# https://leetcode.com/problems/interleaving-string/?envType=study-plan-v2&envId=top-interview-150 

def isInterleave(s1, s2, s3): 
    if len(s1)>len(s2): 
        s1,s2 = s2, s1
        
    A1 = [False] * (len(s1)+1)
    A1[0] = True 
    
    for i in range(len(s1)): 
        if s1[i] == s3[i] and A1[i]: 
            A1[i+1] = True 
            
    temp = [False] * (len(s1) + 1) 
    A2 = temp.copy()
    
    for r in range(len(s2)): 
        for c in range(len(s1)):
            if c==0:
                if A1[0] and s2[r] == s3[r]: 
                    A2[0] = True 
            
            # up is True
            if A1[c+1] and s2[r] == s3[r+c+1]:
                A2[c+1] = True
            
            # left is True
            elif A2[c] and s1[c] == s3[r+c+1]: 
                A2[c+1] = True 
                 
        
        A1 = A2.copy() 
        A2 = temp.copy() 
    
    return A1[-1] 

s1 = "aabcc" 
s2 = "dbbca" 
s3 = "aadbbcbcac" 
isInterleave(s1, s2, s3)

s1 = "aabcc" 
s2 = "dbbca" 
s3 = "aadbbbaccc" 
isInterleave(s1, s2, s3)

s1 = "" 
s2 = "" 
s3 = ""
isInterleave(s1, s2, s3)

s1 = "1357" 
s2 = "246" 
s3 = "1234567" 
isInterleave(s1, s2, s3)

############################################################################### 

# 72. Edit Distance

# https://leetcode.com/problems/edit-distance/?envType=study-plan-v2&envId=top-interview-150

def minDistance(word1, word2): 
    
    A1 = [i for i in  range(len(word1))]
    temp = [0] * len(word1)  
    A2 = temp.copy()
    
    for r in range(len(word2)) :
        for c in range(len(word1)): 
            
            up = A1[c] if r>0 else c+1
            left = A2[c-1] if c>0 else r+1
            upleft = A1[c-1] if c>0 and r>0 else r+c
            
            cur = 0 if word1[c] == word2[r] else 1
            A2[c] = min(up, left, upleft) + cur 
            
        A1 = A2.copy() 
        print(A1)
        A2 = temp.copy()
    
    return A1[-1]

word1 = "horse" 
word2 = "ros"
minDistance(word1, word2)

word1 = "intention" 
word2 = "execution"
minDistance(word1, word2)   

############################################################################### 

# 123. Best Time to Buy and Sell Stock III 

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/?envType=study-plan-v2&envId=top-interview-150 

def maxProfit(prices):
    k = 2
    temp = [0] * len(prices) 
    A, R = temp.copy(), temp.copy()
    
    
    for i in range(k): 
        diff = float("-inf")
        for j in range(len(A)): 
            
            diff = max(diff, A[j] - prices[j]) 
            R[j] = max(R[j-1] if j-1>=0 else float("-inf"), prices[j] + diff) 
        
        A = R.copy() 
        R = temp.copy()
      
    
    return A[-1]

prices = [3,3,5,0,0,3,1,4] 
maxProfit(prices)

prices = [1,2,3,4,5] 
maxProfit(prices)

prices = [7,6,4,3,1]
maxProfit(prices)


############################################################################### 

# 221. Maximal Square

# https://leetcode.com/problems/maximal-square/?envType=study-plan-v2&envId=top-interview-150 

def maximalSquare(matrix):
    
    A = [0] * len(matrix[0]) 
    mx = 0
    for r in range(len(matrix)): 
        prev = 0
        this = 0
        for c in range(len(matrix[0])): 
            
            up = A[c] if r>0 else 0
            left = A[c-1] if c>0 else 0
            
            if r>0:
                prev = this
                this = A[c] 
            else: 
                prev = 0
            upleft = prev 

            A[c] = min(up,left,upleft) + 1 if int(matrix[r][c]) else 0 
            mx = max(A[c], mx)

    return mx

matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
    ]
maximalSquare(matrix)

matrix = [["0","1"],["1","0"]]
maximalSquare(matrix)

matrix = [
    ["1","1","1","1","1"],
    ["1","1","1","1","1"],
    ["1","1","1","1","1"],
    ["1","1","1","1","1"],
    ["1","1","1","1","0"]
    ]
maximalSquare(matrix)

############################################################################### 

# 5. Longest Palindromic Substring 

# https://leetcode.com/problems/longest-palindromic-substring/?envType=study-plan-v2&envId=top-interview-150 

def longestPalindrome(s):
    
    def find(l,r): 
        mx = 0
        while l>=0 and r<len(s) and s[l]==s[r]: 
            mx = r-l
            l -= 1 
            r += 1
        
        return mx+1 
    
    mx = 0
    for i in range(len(s)): 
        even = find(i,i) 
        odd = find(i, i+1) 
        
        mx = max(even, odd, mx) 
    
    return mx

s = "babad" 
longestPalindrome(s)

s = "cbbd"
longestPalindrome(s)  
        
s = "oddo" 
longestPalindrome(s)

############################################################################### 

# 9. Palindrome Number

# https://leetcode.com/problems/palindrome-number/?envType=study-plan-v2&envId=top-interview-150 

def isPalindrome(x): 
    orig = x
    if x < 0: return False 
    
    rev = 0  
    
    while x: 
        Mod = x % 10 
        x = x // 10 
        rev = (rev * 10) + Mod 
    
    return orig == rev 

x = 121 
isPalindrome(x)

x = -121 
isPalindrome(x)

x = 10
isPalindrome(x)

x = 1441 
isPalindrome(x)

x = 123221 
isPalindrome(x)

###############################################################################

# 66. Plus One 

# https://leetcode.com/problems/plus-one/?envType=study-plan-v2&envId=top-interview-150 

def plusOne(digits):
    c = 0 
    add = 1
    n = len(digits)-1 
    
    while n>=0: 
        e = digits[n] 
        e = e + add + c 
        add = 0
        
        if e>9: 
            e = 0 
            c = 1 
        else: 
            c = 0
        digits[n] = e 
        
        n-=1  
    
    if c: 
        return [1] + digits 
    return digits 

digits = [1,2,3] 
plusOne(digits)

digits = [4,3,2,1] 
plusOne(digits)

digits = [9]
plusOne(digits)       

############################################################################### 

# 69. Sqrt(x) 

# https://leetcode.com/problems/sqrtx/?envType=study-plan-v2&envId=top-interview-150 

def mySqrt(x):
    
    def mid(st, end): 
        return st + (end-st)//2 
    
    def binarySearch(st, end): 
        if st>end: return 
        
        m = mid(st, end) 
        
        if m*m>x: 
            binarySearch(st, m-1) 
        else: 
            nonlocal result 
            result = m 
            binarySearch(m+1, end) 
            
    result = 0 
    
    binarySearch(0, x//2) 
    return result 

x = 4 
mySqrt(x)

x = 14 
mySqrt(x)

x = 17
mySqrt(x)

x = 55 
mySqrt(x)

x = 2 
mySqrt(x)

############################################################################### 

# 50. Pow(x, n)

# https://leetcode.com/problems/powx-n/?envType=study-plan-v2&envId=top-interview-150 

def myPow(x, n):
    def rec(x, n): 
        if x == 0: return 0
        if n == 0: return 1  
        
        r = rec(x, n//2) 
        r *= r 
        
        if n%2: 
            r *= x
        
        return r  
    
    result = rec(x, n if n>=0 else -n)  
    
    return result if n>= 0 else 1/result

x = 2.00000 
n = 10 
myPow(x, n)

x = 2.10000 
n = 3 
myPow(x, n)

x = 2.00000 
n = -2 
myPow(x, n) 


############################################################################### 
math.factorial(24)
# 172. Factorial Trailing Zeroes 

# https://leetcode.com/problems/factorial-trailing-zeroes/description/?envType=study-plan-v2&envId=top-interview-150 

def trailingZeroes(n): 
    if n<5: return 0
    
    count = 0 
    i = 5
    while n //i>0: 
        count += n//i 
        i*=5  
    
    return count 

n = 3 
trailingZeroes(n) 

n = 5 
trailingZeroes(n) 

n = 24 
trailingZeroes(n)
 
n = 124 
trailingZeroes(n)

###############################################################################

# 67. Add Binary

# https://leetcode.com/problems/add-binary/?envType=study-plan-v2&envId=top-interview-150 

## can be solved with // and mod also, less verbose
def addBinary(a, b):
    c = 0 
    if len(b)>len(a): a, b= b, a
    
    i, j = len(a)-1, len(b)-1 
    result = []
    
    while i>=0 or j>=0: 
        aa = a[i] 
        bb = b[j] if j>=0 else 0
        k = int(aa) + int(bb) 
        
        if k+c>2: 
            c = 1 
            result.append("1")
            
        elif k+c>1: 
            c = 1 
            result.append("0")
        else: 
            result.append(str(k+c))
            c = 0 
        i-=1 
        j-=1 
        
    if c: 
        r = "1"
        r += "".join(result[::-1])
        return r
    return "".join(result[::-1])


a = "11" 
b = "1" 
addBinary(a, b)

a = "1010" 
b = "1011"
addBinary(a, b)       

a = "1111" 
b = "1" 
addBinary(a,b)

###############################################################################

# 190. Reverse Bits 

# https://leetcode.com/problems/reverse-bits/description/?envType=study-plan-v2&envId=top-interview-150 

def reverseBits(n): 
    
    res = 0 
    i = 32
    while i: 
        res = res<<1
        res |= (n&1) 
        #res = res<<1 
        n = n>>1 
        i -=1
    
    return res 

n = 43261596 
reverseBits(n)
n = 2147483644
reverseBits(n)

############################################################################### 

# 191. Number of 1 Bits

# https://leetcode.com/problems/number-of-1-bits/description/?envType=study-plan-v2&envId=top-interview-150 

def hammingWeight(n):
    c = 0 
    while n: 
        c += (n&1) 
        n >>= 1 
    
    return c
    

n = 11 
hammingWeight(n)

n = 128
hammingWeight(n)

n = 7 
hammingWeight(n)

###############################################################################

# 136. Single Number

# https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=top-interview-150 

def singleNumber(nums):
    
    a = nums[0] 
    for i in range(1, len(nums)): 
        a ^= nums[i] 
    
    return a

    
nums = [2,2,1] 
singleNumber(nums)

nums = [4,1,2,1,2] 
singleNumber(nums)

nums = [1] 
singleNumber(nums)

############################################################################### 

# 137. Single Number II

# https://leetcode.com/problems/single-number-ii/description/?envType=study-plan-v2&envId=top-interview-150

def singleNumber(nums):
    
    res = 0 
    
    for i in range(32):
        c = 0
        for n in range(len(nums)): 
            if n<0: 
                n = n & (2**32-1)
            c += ((nums[n]>>i)&1) 
        
        res |= (c%3) << i
    
    return res - 2 ** 32 if res>=2**31 else res

nums = [2,2,-3,2] 
singleNumber(nums)

nums = [0,1,0,1,0,1,99]
singleNumber(nums) 

############################################################################### 

# 201. Bitwise AND of Numbers Range 

# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/?envType=study-plan-v2&envId=top-interview-150 

def rangeBitwiseAnd(left, right):
    
    diff = right - left
    a = 0 
    res = 0 
    
    for bit in range(32):
        
        if ((left>>bit) & 1):
            a |= (((left>>bit) & 1))<<bit 
            
            if diff < ((1<<bit+1) - a):
                res |= (1<<bit) 
    
    return res

# O(32)
def rangeBitwiseAnd(left, right): 
    i = 0 
    while left != right: 
        left >>= 1 
        right >>= 1 
        i += 1 
        
    return left<<i
        
left = 5 
right = 7 
rangeBitwiseAnd(left, right)

left = 0 
right = 0 
rangeBitwiseAnd(left, right)

left = 1 
right = 2147483647
rangeBitwiseAnd(left, right)

left = 18 
right = 25 
rangeBitwiseAnd(left, right)

left = 32 
right = 64 
rangeBitwiseAnd(left, right) 

############################################################################### 

# 149. Max Points on a Line

# https://leetcode.com/problems/max-points-on-a-line/description/?envType=study-plan-v2&envId=top-interview-150 

def maxPoints(points): 
    
    def findSlope(p1, p2): 
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1] 
        
        return float("inf") if x1-x2 == 0 else (y1-y2)/(x1-x2)
    
     
    result = 0
    
    for i, p1 in enumerate(points[:-1]): 
        slopes = {}
        for p2 in points[i+1:]: 
            slope = findSlope(p1, p2) 
            if slope in slopes: 
                slopes[slope] += 1 
            else: 
                slopes[slope] = 1 
                
            result = max(result, slopes[slope])  
    
    return result+1
            
points = [[1,1],[2,2],[3,3]] 
maxPoints(points)

points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
maxPoints(points)   


