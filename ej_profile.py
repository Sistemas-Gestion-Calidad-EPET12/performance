import time
import random


def slow_sum(nums):
    """
    Realiza una suma extremadamente lenta de una lista de números.

    Parámetros:
        nums (list): Lista de números enteros.

    Retorna:
        int: La suma de los números en la lista.
    """
    total = 0
    for num in nums:
        # Simulamos un cálculo extremadamente lento
        time.sleep(0.01)
        total += num
    return total


def inefficient_sort(nums):
    """
    Realiza una ordenación ineficiente usando el método burbuja.

    Parámetros:
        nums (list): Lista de números enteros.

    Retorna:
        list: Lista ordenada.
    """
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def repeated_computation(nums):
    """
    Calcula la suma al cuadrado de cada número de la lista de forma ineficiente

    Parámetros:
        nums (list): Lista de números enteros.

    Retorna:
        list: Lista con los números al cuadrado.
    """
    results = []
    for num in nums:
        sum_of_squares = 0
        for _ in range(1000):
            sum_of_squares += num * num
        results.append(sum_of_squares)
    return results


def main():
    """
    Función principal que genera una lista de números aleatorios y ejecuta
    funciones ineficientes sobre ellos.
    """
    nums = [random.randint(1, 100) for _ in range(100)]

    print("Sumando números lentamente...")
    slow_sum(nums)

    print("Ordenando números de forma ineficiente...")
    inefficient_sort(nums)

    print("Calculando suma al cuadrado repetidamente...")
    repeated_computation(nums)


if __name__ == "__main__":
    main()

