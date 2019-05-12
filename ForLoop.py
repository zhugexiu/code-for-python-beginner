
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

for letter in "Giraffe Academy":
    print(letter)

for index in range(len(friends)):
    print(index)


def raise_to_power(base_num, pow_num):
    result = 1
    for index2 in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3, 2))
