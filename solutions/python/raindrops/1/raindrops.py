""" RainDrops Function - convert number into its corresponding
raindrop sound. 3 divisible = Pling
5 divisible= Plang 
7 divisible = Plong
"""

def convert(number):
    answer = ''
    if number % 3 == 0:
        answer += 'Pling'
    if number % 5 == 0:
        answer += 'Plang'
    if number % 7 == 0:
        answer+= 'Plong'
    if answer == '':
        return str(number)
    else:
        return answer
    