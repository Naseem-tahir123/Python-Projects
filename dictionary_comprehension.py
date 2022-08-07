# my_dict = {num:num**2 for num in range(1,11)}
# print(my_dict)
# for a,b in my_dict.items():
#     print(f"square of {a} is : {b}")

# name = "Naseem Shargoo Baltistani"
# alphabet_counter = {alphbt:name.count(alphbt) for alphbt in name}
# for i,j in alphabet_counter.items():
#     print(f"{i}:{j}")

odd_even = {num:("even" if num%2==0 else "odd") for num in range(1,11) }
print("even numbers are")
for a,b in odd_even.items():
    if a%2==0:
        print(f"{a} : {b}")
print("odd number are :")
for j,k in odd_even.items():
    if j%2!=0:
        print(f"{j}:{k}")

