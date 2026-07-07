#def paper_doll(text):
    #result = ""
    #for char in text:
        #result += char * 3  # Multiplies the character by 3 and adds it to the result
    #return result

#def has_33(nums):
    # Loop from 0 up to the second-to-last index
    #for i in range(len(nums) - 1):
        # Check if the current number and the next number are both 3
       # if nums[i] == 3 and nums[i + 1] == 3:
            #return True
            
    # If the loop finishes without finding two 3s, return False
    #return False

#def both_samee(text):
    #a = text.split()
   
    #return a[0][0].lower()==a[1][0].lower()
#print(both_samee("yooo man"))
#print(both_samee("yooo yooo"))
#print(both_samee("yooo Yan"))

#def twenchy(num1,num2):
    #if num1==20 or num2== 20:
     #   return True
    #elif num1 + num2 == 20:
   #     return True
  #  else:
 #       return False

#print(twenchy(800,90))
#print(twenchy(80,90))

#def cap_name(text):
    #if len(text) >= 3:
   #     return text[:3].capitalize() + text[3:].capitalize()
  #  else:
 #       return 'wrong input'
    
#print(cap_name("yes"))


#def reversetxt(text):
 #   return text[::-1]

#print(reversetxt("hello"))

#def reversetxt(text):
 #   return '-'.join(text.split()[::-1])

#print(reversetxt("hello I am back"))


print(' sirrr '.join('yessssss goooooo'.split()))

def numbers(n):
    return ((abs(100-n)<=10) or (abs(200-n)<=10))

print(numbers(66))
