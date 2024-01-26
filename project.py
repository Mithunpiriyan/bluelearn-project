def max_subarray_sum(arr):
    n = len(arr)

    # Initialize variables
    max_sum = float('-inf')
    current_sum = 0
    start_index = 0
    end_index = 0

    # Iterate through the array
    for i in range(n):
        current_sum = max(arr[i], current_sum + arr[i])

        if current_sum < 0:
            current_sum = 0
            start_index = i + 1

        if current_sum > max_sum:
            max_sum = current_sum
            end_index = i

    # The contiguous subarray with the largest sum is arr[start_index:end_index+1]
    return arr[start_index:end_index+1]

# Example usage:
input_array_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_1 = max_subarray_sum(input_array_1)

print("Input Array:", input_array_1)
print("Maximum Subarray Sum:", sum(result_1))
print("Subarray with the Maximum Sum:", result_1)

input_array_2 = [1, -2, 3, -4, 5]
result_2 = max_subarray_sum(input_array_2)

print("\nInput Array:", input_array_2)
print("Maximum Subarray Sum:", sum(result_2))
print("Subarray with the Maximum Sum:", result_2)

