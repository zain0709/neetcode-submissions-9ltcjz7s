class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res =  r
        while l <= r:
            mid = (l+ r) // 2
            total = 0
            
            curr_days = 1  

            for w in weights:
                if (total + w) > mid:      
                    curr_days += 1
                    total = w   
                else:
                    total += w
            
            if curr_days <= days:
                res = min(mid, res)
                r = mid - 1
            else:
                l = mid  + 1 
        return res


                
                
                