monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Spe": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}


print(monthConversions["Nov"])
print(monthConversions.get("Dec", "Not a valid key"))

i = 1
while i <= 10:
    print(i)
    i += 1


print("done with loop")


secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, You Lose!")
else:
    print("You Win!")

