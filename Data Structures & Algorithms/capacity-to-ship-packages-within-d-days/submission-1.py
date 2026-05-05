class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, h = max(weights), sum(weights)
        
        def try_weight(w):
            i = 0
            cur_w = 0
            cur_d = 0
            while i < len(weights):
                if cur_w + weights[i] > w:
                    cur_d += 1
                    cur_w = 0
                cur_w += weights[i]
                if cur_d > days:
                    return cur_d
                i += 1
            cur_d += 1
            return cur_d
        
        while l < h:
            mid = l + (h - l) // 2

            try_d = try_weight(mid)
            if try_d > days:
                l = mid + 1
            else:
                h = mid
        
        return l
