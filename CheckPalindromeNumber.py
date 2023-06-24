def is_palindrome(num):
    num_digits_list = [str(n) for n in str(num)]
    num_digits_list_reverse = num_digits_list.copy()
    num_digits_list_reverse.reverse()
    if (num_digits_list == num_digits_list_reverse):
        return True
    else:
        return False

num = 242
print(is_palindrome(num))