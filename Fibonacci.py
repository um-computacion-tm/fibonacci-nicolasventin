def fibonacci (number):
    if number <= 1:
        return number
    return fibonacci(number - 2) + fibonacci(number - 1) #Aplico la ecuacion de la teoria de fibonacci Fn = (Fn - 1) + (Fn - 2)