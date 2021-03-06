# pointer
res, n = [], len(nums)
        if not nums or n < 4: return []
        nums.sort() 
        for i in range(n - 3):
            if(nums[i] + nums[i + 1] + nums[i + 2] + nums[ i + 3] > target): break
            if(nums[i] + nums[-1] + nums[-2] + nums[-3] < target): continue
            if(i > 0 and nums[i] == nums[i - 1]): continue
            for j in range(i + 1, n - 2):
                if(nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target): break
                if(nums[i] + nums[j]+ nums[-1] + nums[-2] < target): continue
                if(j - i > 1 and nums[j] == nums[j - 1]): continue
                L=j+1
                R=n-1
                while(L<R):
                    if(nums[i] + nums[j] + nums[L] + nums[R] == target):
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        while(L < R and nums[L] == nums[L + 1]): L = L + 1
                        while(L < R and nums[R] == nums[R - 1]): R = R - 1
                        L = L + 1
                        R = R - 1
                    elif(nums[i] + nums[j] + nums[L] + nums[R] > target): R = R - 1
                    else: L = L + 1
        return res