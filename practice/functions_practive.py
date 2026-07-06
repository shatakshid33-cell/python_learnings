def paper_doll(text):
    result = ""
    for char in text:
        result += char * 3  # Multiplies the character by 3 and adds it to the result
    return result

def has_33(nums):
    # Loop from 0 up to the second-to-last index
    for i in range(len(nums) - 1):
        # Check if the current number and the next number are both 3
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
            
    # If the loop finishes without finding two 3s, return False
    return False