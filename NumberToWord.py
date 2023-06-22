number_word = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}

input_number = input('Phone: ')
output_word = ''

for num in input_number:
    output_word += number_word.get(int(num)) + ' '

print(output_word)
