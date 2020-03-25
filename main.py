from decimal import Decimal


def temperature_rising_energy():
    temperature_1 = get_numeric_input('Please enter the starting temperature: ')
    temperature_2 = get_numeric_input('Please enter the end temperature: ')
    calorific_value = get_numeric_input('Please enter the Calorific Value(J/kg*t): ')
    mass = get_numeric_input('Please enter the mass(kg): ')

    energy_usage = calorific_value * mass * (temperature_1 - temperature_2)
    return print(f'{ energy_usage }J')


def staying_energy():
    specific_heat = get_numeric_input('Please enter the specific heat of the element: ')
    mass = get_numeric_input('Please enter the mass: ')

    energy_usage = mass * specific_heat
    return print(f'{ energy_usage }kJ')


def get_numeric_input(input_text):
    result = input(input_text)
    try:
        return Decimal(result)
    except:
        return get_numeric_input('Please make sure that you are entering a number: ')


def run_app(choice):
    print(choice)
    if choice != 'RISE' and choice != 'STAY':
        return run_app(input('Please choose what to do(Staying at a temperature(boiling, etc)(STAY) or rising to a temperature(RISE): '))
    continue_running = True
    while continue_running:
        if input('Do you want to calculate?(Y/N): ') != 'Y':
            return continue_running
        if choice == 'RISE':
            temperature_rising_energy()
        elif choice == 'STAY':
            staying_energy()


run_app(input('Please choose what to do(Staying at a temperature(boiling, etc)(STAY) or rising to a temperature(RISE): '))
