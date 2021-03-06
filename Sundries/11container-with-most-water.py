# base Time O(n), Memory O(1)
start, end, water = 0, len(height) - 1, 0
while start < end:
    if height[start] < height[end]:
        water = max(water, (end - start) * height[start])
        start += 1
    else:
        water = max(water, (end - start) * height[end])
        end -= 1
return water

# batter Time O(n), Memory O(1)
start, end, water = 0, len(height) - 1, 0
while start < end:
    water = max(water,min(height[start], height[end]) * (end - start))
    if height[start] < height[end]: start += 1
    else: end -= 1
return water