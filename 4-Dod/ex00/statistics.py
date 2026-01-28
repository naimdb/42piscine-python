def ft_statistics(*args, **kwargs):
    numbers = sorted(args)
    n_num = len(numbers)

    for operation in kwargs.values():
        if n_num == 0:
            print("ERROR")
            continue

        if operation == "mean":
            resultat = sum(numbers) / n_num
            print(f"mean : {resultat}")

        elif operation == "median":
            if n_num % 2 == 0:
                resultat = (numbers[n_num//2-1] + numbers[n_num//2]) / 2
            else:
                resultat = numbers[n_num//2]
            print(f"median : {resultat}")

        elif operation == "quartile":
            if n_num < 2:
                print("ERROR")
                continue
            q1_index = n_num // 4
            q3_index = (3 * n_num) // 4
            if n_num % 4 == 0:
                q1 = float((numbers[q1_index - 1] + numbers[q1_index]) / 2)
                q3 = float((numbers[q3_index - 1] + numbers[q3_index]) / 2)
            else:
                q1 = float(numbers[q1_index])
                q3 = float(numbers[q3_index])
            print(f"quartile : [{q1}, {q3}]")

        elif operation == "std":
            if n_num < 2:
                print("ERROR")
                continue
            mean = sum(numbers) / n_num
            variance = sum((x - mean) ** 2 for x in numbers) / n_num
            resultat = variance ** 0.5
            print(f"std : {resultat}")

        elif operation == "var":
            if n_num < 2:
                print("ERROR")
                continue
            mean = sum(numbers) / n_num
            resultat = sum((x - mean) ** 2 for x in numbers) / n_num
            print(f"var : {resultat}")
