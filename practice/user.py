def weather_condition(temperature):
    if temperature > 7:
        return 'Warm'
    else:
        return 'Cold'

user_input = int(input('Enter some input:'))


print(type(user_input), user_input)