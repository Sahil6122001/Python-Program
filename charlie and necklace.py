def count_necklaces(max_pearls, min_coeff, max_coeff):
    # Initialize count to 0
    count = 0
    
    # Iterate over all possible number of pearls
    for num_pearls in range(1, max_pearls+1):
        # Iterate over all possible magnificence coefficients
        for coeff in range(min_coeff, max_coeff+1):
            # Generate all possible combinations of pearls with this coefficient
            for comb in comb(range(min_coeff, coeff+1), num_pearls):
                # Check if the combination is sorted in non-decreasing order
                if all(comb[i] <= comb[i+1] for i in range(num_pearls-1)):
                    count += 1
    
    return count
count_necklaces(1, 4, 5)

