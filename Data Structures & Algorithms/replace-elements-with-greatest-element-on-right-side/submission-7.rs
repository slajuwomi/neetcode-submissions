impl Solution {
    pub fn replace_elements(arr: Vec<i32>) -> Vec<i32> {
        let mut maxSoFar = -1;
        let mut res = vec![0; arr.len()];
        for i in (0..arr.len()).rev() {
            res[i] = maxSoFar;
            maxSoFar = max(arr[i], maxSoFar);
        }
        res 
    }
}
/* 
[5,5,3,2,2,-1]



gesf = -1 -> 2 -> 3 -> 5
[5,5,3,2,2,-1]
   i
n = len(arr)
max = -1
for i in range(n - 1, -1)
    arr[i] = max
    max = max(arr[i], max)
return arr 
 */
