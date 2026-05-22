class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter=0
        majorityelement=-1
        for num in nums:
            if counter==0:
                majorityelement=num
                counter+=1
            else:
                if majorityelement==num:
                    counter+=1
                else:
                    counter-=1
        return majorityelement

        