from itertools import permutations
word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
result = input("Enter result word: ").upper()

letters = list(set(word1 + word2 + result))

if len(letters) > 10:
    print("Too many unique letters! Cannot solve.")
else:
    first_letters = {word1[0], word2[0], result[0]}

    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        if any(mapping[ch] == 0 for ch in first_letters):
            continue

        n1 = int("".join(str(mapping[ch]) for ch in word1))
        n2 = int("".join(str(mapping[ch]) for ch in word2))
        res = int("".join(str(mapping[ch]) for ch in result))

        if n1 + n2 == res:
            print("\nSolution Found!")
            print("Letter Mapping:")
            for k, v in mapping.items():
                print(k, "=", v)

            print(f"\n{n1} + {n2} = {res}")
            break
    else:
        print("No solution found.")
