impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        for (i, n) in nums.iter().enumerate() {
            for (j, m) in nums.iter().enumerate().skip(i + 1) {
                if n + m == target {
                    return vec![i as i32, j as i32];
                }
            }
        }

        unreachable!("every input has a pair that satisfy the condition");
    }
}
