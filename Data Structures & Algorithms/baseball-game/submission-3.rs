impl Solution {
    pub fn cal_points(operations: Vec<String>) -> i32 {
        let mut stack = Vec::new();
        for op in operations {
            if op == "+" {
                stack.push(stack[stack.len()-1] + stack[stack.len()-2]);
            } else if op == "D" {
                stack.push(stack[stack.len()-1] * 2);
            } else if op == "C" {
                stack.pop();
            } else {
                stack.push(op.parse().unwrap());
            }
        }
        return stack.iter().sum();
    }
}
/*  
["1","2","+","C","5","D"]
[1, 2]

go through array, add each number to the stack
if operation
+ - get sum of stack[-1] and stack[-2]
D - get double of stack[-1]
C - stack pop

for op in operations
    if op == +
        stack.push(stack[-1] + stack[-2])
    elif op == D
        stack.push(stack[-1] * 2)
    elif op == C
        stack.pop
    else
        stack.push(op)
return sum(stack)
 */
