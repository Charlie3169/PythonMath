def binary_search(input_list, low, high, target):
    if low > high:
        return -1  # Not found
    else:
        mid = (low + high) // 2
        if target == input_list[mid]:
            return mid  # Found the target
        elif target < input_list[mid]:
            return binary_search(input_list, low, mid - 1, target)  # Search lower half
        else:
            return binary_search(input_list, mid + 1, high, target)  # Search upper half

def omnary_search(input_list, complex_input_signature, target):
    pass  # Add your implementation here

def main():
    test_list = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]
    test_target = 140
    print("Index:", binary_search(test_list, 0, len(test_list) - 1, test_target))

if __name__ == "__main__":
    main()
