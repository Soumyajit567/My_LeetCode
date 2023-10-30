#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool primeSubOperation(vector<int>& nums) {
        // Sieve of Eratosthenes
        vector<int> primes = {2};
        for(int i = 2; i <= 1000; i++) {
            bool is_prime = true;
            for(int j = 2; j <= sqrt(i); j++) {
                if(i % j == 0) {
                    is_prime = false;
                    break;
                }
            }
            if(is_prime) primes.push_back(i);
        }

        // Traversing from back and using binary search to find a suitable prime no. to subtract
        for(int i = nums.size() - 2; i >= 0; i--) {
            if(nums[i] == 2 && nums[i + 1] <= 2) return false;
            if(nums[i] >= nums[i + 1]) {
                int n = nums[i] - nums[i + 1] + 1;
                auto indx = lower_bound(primes.begin(), primes.end(), n) - primes.begin();
                if(indx >= primes.size()) return false;
                if(primes[indx] >= nums[i]) return false;
                nums[i] -= primes[indx];
                if(nums[i] >= nums[i + 1]) return false;
            }
        }
        return true;
    }
};
