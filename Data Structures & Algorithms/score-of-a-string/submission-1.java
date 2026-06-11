class Solution {
    public int scoreOfString(String s) {
        int[] ascii = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
            ascii[i] = (int) s.charAt(i);
        }
        int res = 0;
        for (int i = 0; i < ascii.length - 1; i++) {
            res += Math.abs(ascii[i+1] - ascii[i]);
        }
        return res;
    }
}