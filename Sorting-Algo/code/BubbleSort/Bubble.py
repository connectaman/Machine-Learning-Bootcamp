def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


# Generate List of Numbers to be Sorted
random_list_of_nums = [5,2,1,8,4,6,5,8,2,-8,5,2,6,8]
# Call the bubble_sort method
bubble_sort(random_list_of_nums)
# print the final sorted list
print(random_list_of_nums)