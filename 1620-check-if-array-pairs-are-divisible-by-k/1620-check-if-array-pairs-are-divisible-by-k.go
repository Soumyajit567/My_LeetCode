func canArrange(arr []int, k int) bool {
    remainderCount := make(map[int]int)

	// Count the frequency of each remainder
	for _, num := range arr {
		remainder := ((num % k) + k) % k// Handle negative numbers correctly
		remainderCount[remainder]++
	}

	// Check if the array can be arranged into pairs
	for remainder, count := range remainderCount {
		if remainder == 0 {
			// For remainder 0, the count must be even
			if count%2 != 0 {
				return false
			}
        // else if 2*remainder == k {
		// 	// For cases where k is even and remainder is k/2
		// 	if count%2 != 0 {
		// 		return false
		// 	}
		} else {
			// The count of a remainder must equal the count of its complement
			complement := k - remainder
			if remainderCount[complement] != count {
				return false
			}
		}
	}

	return true
}