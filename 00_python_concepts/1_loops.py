def fibonacci():
    fibonaccArray = []
    print("Inserte cantidad de fibonaccis a obtener: ")
    n = int(input('>'))

    # Handle small cases
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    # Start Fibonacci with 0, 1
    fibonaccArray = [0, 1]

    # Build the rest
    for i in range(2, n):
        next_value = fibonaccArray[-1] + fibonaccArray[-2]
        fibonaccArray.append(next_value)

    return fibonaccArray

print(fibonacci())
