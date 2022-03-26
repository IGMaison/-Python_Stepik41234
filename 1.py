s = input()
brackets_arr = list()
brackets = {"(": ")", "[": "]", "{": "}"}
for i in range(len(s)):

    symb = s[i]

    if symb in brackets:

        brackets_arr.append([symb, i + 1])
    else:

        if symb in brackets.values():
            if brackets_arr:
                if brackets_arr[-1][0] + symb in ['()', '[]', '{}']:

                    brackets_arr.pop()
                else:

                    brackets_arr.append([symb, i + 1])
                    break
            else:
                brackets_arr.append([symb, i + 1])
                break

if brackets_arr:

    print(brackets_arr[-1][1])
else:

    print("Success")
