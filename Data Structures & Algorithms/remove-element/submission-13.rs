impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut k = 0;
        for i in 0..nums.len() {
            if nums[i] != val {
                nums[k] = nums[i];
                k += 1;
            }
        }
        k as i32
    }
}
/*
go through the array and when we see a value that is not the desired val we swap it with the pointer at the front of the array (k)
k = 0
for i in range(len(nums))
    if nums[i] != val
        nums[k] = nums[i]
        k += 1
return k
*/
