impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec::new();
        let closeToOpen = HashMap::from([
            (']', '['),
            ('}', '{'),
            (')', '('),
        ]);
        for c in s.chars() {
            if let Some(&open) = closeToOpen.get(&c) {
                if !stack.is_empty() && *stack.last().unwrap() == open {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        stack.is_empty()
    }
}
/*
create a mutable stack variable
create a closeToOpen hash map that has the close versions of the characters as keys and the open versions as values
loop through the characters of the given string
check first if the current character is a close version by getting the current character from the loop and checking if it returns a valid value from the hash map
if the current char is a close version then we need to check two things
    1 if the stack is empty. if the stack is empty then the close char does not have a matching open and we should return false
    2 if the open version is equal to what is currently on top of the stack. if it is we can pop the stack as this is a valid match
    if one or both of these return false that the input string is invalid and we can return false, so use && here
otherwise, if the current char is an open version just push it to the stack
at the end return whether the stack is empty after going through the full string, that will tell us if the input string was valid

*/