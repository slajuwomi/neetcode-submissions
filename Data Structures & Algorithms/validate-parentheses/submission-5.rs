impl Solution {
    pub fn is_valid(s: String) -> bool {
        let symbolMapping = HashMap::from([
            ('}', '{'),
            (')', '('),
            (']', '['),
        ]);
        let mut stack = Vec::new();
        for symbol in s.chars() {
            //                                      
            if let Some(&open) = symbolMapping.get(&symbol) {
                if stack.len() == 0 {
                    return false;
                } 
                if stack.last() == Some(&open) {
                    stack.pop(); 
                } else {
                    return false;
                }
            } else {
                stack.push(symbol);
            }
        }
        return stack.len() == 0;
    }
}
