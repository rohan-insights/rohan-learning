a='asdfg'
s=list(a)
left_index = 0
right_index = len(s)-1

def rivers(s, left_index,right_index):

  if  left_index>right_index:
    return
  s[left_index],s[right_index] = s[right_index],s[left_index]
  rivers(s,left_index+1,right_index-1)
rivers(s,left_index,right_index)
print("".join(s))

