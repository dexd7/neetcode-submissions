class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # #First approach I got on own. 
        # #-Use set() to evade duplicates in the answer
        # #Time Complexity: "O(n)"
        # #Space Complexity: "O(n)"
        # dictionary = {}
        # for num in nums:
        #     dictionary[num] = 1+dictionary.get(num, 0)
        # result = set()
        # majority_qualifier = (len(nums)//3)+1
        # for i in nums:
        #     if dictionary[i]>=majority_qualifier:
        #         result.add(i)
        # return list(result)
        
        # Now the optimal approach, Boyer-Moore Voting Algorithm extended to 2 cnadidated overall:
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            if num == cand1:
                count1+=1
            elif num == cand2:
                count2+=1
            elif count1==0:
                cand1, count1 = num, 1
            elif count2==0:
                cand2, count2 = num, 1
            else:
                count1-=1
                count2-=1
        result = []
        for candidate in (cand1, cand2):
            if candidate is not None and nums.count(candidate)>len(nums)//3:
                result.append(candidate)
        return result
        
        #makes it Overall O(1) space with O(n) time.