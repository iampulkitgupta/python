file = open('youtube.txt', 'w')

try:
    file.write('Pulkit Gupta')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('Advik Garg')