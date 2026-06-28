class Solution {
    public String minWindow(String s, String t) {
        if (t.isEmpty() || s.isEmpty()) return "";

        Map<Character, Integer> need = new HashMap<>();
        for (char c : t.toCharArray()) {
            need.merge(c, 1, Integer::sum);
        }

        int required = need.size();   // distinct chars to satisfy
        int have = 0;

        Map<Character, Integer> window = new HashMap<>();
        int start = 0;
        int minLength = Integer.MAX_VALUE;
        int resStart = 0;             // remember where the best window began

        for (int end = 0; end < s.length(); end++) {
            char c = s.charAt(end);
            window.merge(c, 1, Integer::sum);

            if (need.containsKey(c) && window.get(c).intValue() == need.get(c).intValue()) {
                have++;
            }

            while (have == required) {
                if (end - start + 1 < minLength) {
                    minLength = end - start + 1;
                    resStart = start;
                }

                char left = s.charAt(start);
                window.merge(left, -1, Integer::sum);
                if (need.containsKey(left) && window.get(left) < need.get(left)) {
                    have--;
                }
                start++;
            }
        }

        return minLength == Integer.MAX_VALUE ? "" : s.substring(resStart, resStart + minLength);
    }
}