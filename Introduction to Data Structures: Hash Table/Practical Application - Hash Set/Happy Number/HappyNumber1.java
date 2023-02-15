class Solution {
    public boolean isHappy(int n) {
        
        HashSet <Integer> set = new HashSet <> (); 
        
        int total; 
        int val;
        
        while (!set.contains(n)) {
            
            set.add(n);
            
            total = 0;
            
            String num = String.valueOf(n);
            
            System.out.println("num: " + num);
            
            for (int i = 0; i < num.length(); i++) {
                val = Integer.parseInt(String.valueOf(num.charAt(i)));
                
                System.out.println("val " + val);
                
                total = total + (val * val) ;
            }
            
            n = total;
            
            System.out.println("Set: " + set.toString());
            
            if (n == 1) {
                return true;
            }
        }
        
        return false;
        
    }
}