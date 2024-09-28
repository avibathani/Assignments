def calculate_sum(numbers_list):
    total_sum = sum(numbers_list)  
    return total_sum

def main():
    sample_numbers = [3,54,34,13,78,65,434,3456]  
    result = calculate_sum(sample_numbers) 
    print(f"The total of the numbers in the list is: {result}")

if __name__ == "__main__":
    main()
