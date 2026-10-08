class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder sb = new StringBuilder();
        int balance = 0;
        for (int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if (ch == '(')
            {
                if (balance > 0)
                {
                    sb.append(ch);
                }
                balance++;
            }else{
                balance--;
                if (balance > 0)
                {
                    sb.append(ch);
                }
            }
        }
     return sb.toString(); 
    }
}