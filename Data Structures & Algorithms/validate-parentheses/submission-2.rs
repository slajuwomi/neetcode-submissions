impl Solution {
    pub fn is_valid(s: String) -> bool {
        let symbolMapping = HashMap::from([
            ('}', '{'),
            (')', '('),
            (']', '[')
        ]);
        let mut stack = Vec::new();
        for symbol in s.chars() {
            if symbolMapping.values().any(|&v| v == symbol) {
                stack.push(symbol);
            } else {
                if stack.len() == 0 {
                    return false
                } else if stack[stack.len() - 1] == symbolMapping[&symbol] {
                    stack.pop();
                } else {
                    return false
                }
            }
        }
        return stack.len() == 0;
    }
}
/* push each opening symbol to the stack, pop from top of if the top of stack is the correct matching end symbol

"[(])"

staack = [(

{
"]": "[",
")": "("
"}": "{"
}
for symbol in s
    if symbol in dict.keys:
        stack.push(symbol)
    else:
        if stack[-1] == dict[symbol]:
            stack.pop()
        else:
            return false
return stack.len() == 0

        
*/
