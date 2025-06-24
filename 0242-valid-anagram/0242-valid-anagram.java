class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        int[] c_count = new int[26];
        for(int i=0; i< s.length(); i++){
            c_count[s.charAt(i)-'a']++;
            c_count[t.charAt(i)-'a']--;
        }
        for (int count: c_count){
            if (count!=0){
                return false;
            }
        }
        return true;
    }
}