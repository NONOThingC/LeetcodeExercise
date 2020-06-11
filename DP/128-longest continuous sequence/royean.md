use array directly cost too much space, use treemap:

```java
import java.util.Map.Entry;

class Solution {
    public int longestConsecutive(int[] nums) {
        int len = nums.length;
        TreeMap<Integer, Integer> map = new TreeMap<Integer, Integer>();
        int max = 0;
        if(len != 0) max = 1;
        // store the elements in a hashmap
        for(int i = 0;i < len;i++){
            map.put(nums[i],1);
        }

        // iterate the map and use dp
        // use treemap to ensure the order.
        for(Entry<Integer,Integer> entry : map.entrySet()) {
            int key = entry.getKey(), val = entry.getValue();
            if(key > -2147483648){
                Integer tmp = map.get(key - 1);
                if(tmp != null) {
                    map.put(key, tmp + 1);
                    if(tmp + 1 > max) max = tmp + 1;
                }
            }
        }
        return max;
    }
}
```

use set instead of treemap: (the official answer)

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> num_set = new HashSet<Integer>();
        for (int num : nums) {
            num_set.add(num);
        }

        int longestStreak = 0;

        for (int num : num_set) {
            // to ensure that the iteration begins from the smallest elememt of a 
            // consecutive subarray.
            if (!num_set.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;

                while (num_set.contains(currentNum + 1)) {
                    currentNum += 1;
                    currentStreak += 1;
                }

                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
}
```

use disjoint set  (inspired by comments)

```java
class Solution {
    HashMap<Integer, Integer> map  = new HashMap<Integer, Integer>();

    public int find(int x) {
        Integer par = map.get(x), grandpar = map.get(par);
        /*
        * path compression method 1, 6ms
        * if(grandpar !=null) {
        *   map.put(x, grandpar);
        * }
        * return par != null ? find(par) : x;
        */

        
        // path compression method 2, 6ms
        int ans = x;
        if(par != null) {
            ans = find(par);
            map.put(x, ans);
        }
        return ans;
    }

    public int longestConsecutive(int[] nums) {
        int len = nums.length;

        for(int i = 0;i < len;i++) {
            map.put(nums[i], nums[i] + 1);
        }
        int ans = 0;
        for(int i = 0;i < len;i++) {
            // prune, start from the smallest
            int y = find(nums[i]+1);
            ans = Math.max(ans, y - nums[i]);
        }
        return ans;
    }
}
```

