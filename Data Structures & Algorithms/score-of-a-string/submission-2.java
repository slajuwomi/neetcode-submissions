class Solution {
    public int scoreOfString(String s) {
        int res = 0;
        for (int i = s.length()-1; i > 0; i-- ) {
            System.out.println(i);
            res += Math.abs((int) s.charAt(i) - (int) s.charAt(i-1));
        }
        return res;
    }
}