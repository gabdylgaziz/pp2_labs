def spy_game(nums) -> bool:
    s = ''
    for i in range(len(nums)):
        if nums[i] == 0 or nums[i] == 7:
            s+=str(nums[i])
    if '007' in s:
        return True
    else:
        return False
            

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))