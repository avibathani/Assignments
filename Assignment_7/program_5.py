def filter_odd_numbers(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]  
    return even_numbers

def main():

    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20]
    filtered_list = filter_odd_numbers(test_numbers)  
    print(f"Original list: {test_numbers}")
    print(f"Filtered list (even numbers only): {filtered_list}")

if __name__ == "__main__":
    main()
