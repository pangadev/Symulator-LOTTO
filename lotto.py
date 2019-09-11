from random import shuffle

START_NUMBER = 1
END_NUMBER = 49

def draw_lotto(n=6):
    numbers = [x for x in range(START_NUMBER, END_NUMBER+1)]
    shuffle(numbers)
    return sorted(numbers[:n])

def user_lotto(n=6):
    numbers = []
    while len(numbers) < n:
        number = input("Input number: ")
        try:
            number = int(number)
        except ValueError:
            print("[This is not the correct number!]")
            continue
        if START_NUMBER <= number <= END_NUMBER:
            if number in numbers:
                print("[You've already used this number!]")
            else:
                numbers.append(number)
        else:
            print(f"[Ta liczba musi być z zakresu {START_NUMBER} - {END_NUMBER}]")
    numbers.sort()
    return(numbers)


def lotto(drawn, submitted):
    return [x for x in submitted if x in drawn]

drawn = draw_lotto()
submitted = user_lotto()
matches = lotto(drawn, submitted)

print(f"Drawn: {drawn}")
print(f"Submitted:  {submitted}")
print(f"Matched:  {matches} ({len(matches)})")