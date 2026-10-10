use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut theMap = HashMap::new();
        for (i, &n) in nums.iter().enumerate() {
            let diff = target - n;
            if theMap.contains_key(&diff) {
                if let Some(&j) = theMap.get(&diff) {
                    return vec![j, i as i32];
                }
            }
            theMap.insert(n, i as i32);
        }
        return vec![]
    }
}

/* 
we need to go through each value and get the diff while going thourgh and check with things in hash map

for i, num in nums:
    diff = target - num
    if diff in hashmap:
        return [i, hashmap[diff]]
    hashmap[num] = i


*/