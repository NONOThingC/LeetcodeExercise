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

use disjoint set  (inspired by comments), this looks like more of dfs.

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

this version has a better and comprehensive of union and find

To apply UF to this problem, we have to determine which elements should be united together, in this problem, we can define that consecutive numbers belong to the same group, thus they can be united.

```java
class Solution {
    HashMap<Integer, Integer> map  = new HashMap<Integer, Integer>();

    int maxSize = 1;
    int[] size; // the size of the each component.
    int[] parent; // the parent of each element.
    public int longestConsecutive(int[] nums) {
        int len = nums.length;
        if(len == 0) return 0;
        parent = new int[len];
        size = new int[len];
        Arrays.fill(size,1);
        for(int i = 0;i < len;i++) {
           if(map.containsKey(nums[i])){
                continue;
            }
            map.put(nums[i], i);
            parent[i] = i;
            if(map.containsKey(nums[i] - 1)){
                unite(i, map.get(nums[i] - 1));
            }
            if(map.containsKey(nums[i] + 1)){
                unite(i, map.get(nums[i] + 1));
            }
        }
        return maxSize;
    }

    public int find(int x) {
        int par = parent[x], grandPar = parent[par];
        if(par == x) return x;
        parent[x] = grandPar; 
        return find(grandPar);
    }

    public void unite(int a, int b) {
        int rootA = find(a), rootB = find(b);
        if(rootA == rootB) return ;
        int small = rootA, big = rootB;
        if(size[rootA] > size[rootB]){
            small = rootB;
            big = rootA;
        }
        
        // unite two trees;
        parent[small] = big;
        size[big] += size[small];

        if(size[big] > maxSize) maxSize = size[big];
    }
    
}
```

