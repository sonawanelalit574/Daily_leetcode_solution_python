class Solution {
public:
    int sortableIntegers(vector<int>& nums) {
        int n = nums.size(), an = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i != 0) continue;

            int k = n / i;
            bool could = true;
            vector<vector<int>> checkList;
            for (int j = 0; j < n; j += k) {
                vector<int> c = check(nums, j, j + k);
                if (c[0] > 1) {
                    could = false;
                    break;
                }
                checkList.push_back(c);
            }
            if (could) {
                for (int j = 0; j < checkList.size() - 1; j++) {
                    if (checkList[j][1] > checkList[j + 1][2]) {
                        could = false;
                        break;
                    }
                }
            }
            cout << i << " " << could << endl;
            if (could) an += k;
        }
        return an;
    }

private:
    vector<int> check(vector<int>& nums, int l, int r) {
        int count = 0, high = nums[r - 1], low = nums[r - 1];
        for (int i = l; i < r - 1; i++) {
            if (nums[i] > nums[i + 1]) count++;
            high = max(high, nums[i]);
            low = min(low, nums[i]);
        }
        if (count == 1 && nums[r - 1] > nums[l]) count++;
        return {count, high, low};
    }
};