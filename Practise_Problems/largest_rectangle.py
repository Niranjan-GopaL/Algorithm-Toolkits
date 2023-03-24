# O(n) and O(n) 
_ = input()
input_list = list(map(int , input().split(' ')))

max_area = 0
st = [] # each element is a tuple of index(not necessarily it's own) ,height
for i,h in enumerate(input_list):
    start = i
    while st and h < st[-1][1]: #whenever the height reached is less than the last element in st
        index , height = st.pop()
        max_area = max(max_area, height*(i - index))
        start = index
    st.append((start,h))

# computing the max_area of the elements which didn't pop off
for i,h in st:
    max_area = max(max_area, h* (len(input_list) - i))

print(max_area)