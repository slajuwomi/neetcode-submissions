impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let mut cnt = 0;
        let mut running_cnt = 0;
        for n in nums {
            if n == 0 {
               cnt = std::cmp::max(running_cnt, cnt); 
               running_cnt = 0;
            } else {
                running_cnt += 1;
            } 
        }
        cnt = std::cmp::max(running_cnt, cnt); 
        cnt
    }
}


/*
think we need to keep track of a cnt variable and basically just update max

for n in nums:
    if n == 0:
        cnt = max(running_count, cnt)
        running_count = 0
    else:
        running_count += 1
cnt = max(rc, cnt)
return cnt

 
[1, 1, 0, 1, 1, 1]
rc = 3
cnt = 2
*/
