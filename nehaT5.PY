#Assignment NO 5
#Task 1
a=input("enter the student name:")
D={"neha":83,"sanika":80,"rutuja":75,"jayshree":70}
if a in D:
    print(f"{a}'s marks:{D[a]}")
else:
    print ("student not found")

#Task 2
list=[1,2,3,4,5,6,7,8,9,10]
print(f"original list:{list}")

Extracted_list=list[0:5]
print(f"Extracted first five elements:{Extracted_list}")

Reversed_list=Extracted_list[::-1]
print(f"Reversed extracted elemnets:{Reversed_list}")