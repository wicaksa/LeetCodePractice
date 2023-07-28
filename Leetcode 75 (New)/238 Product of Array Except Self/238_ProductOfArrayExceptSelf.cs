public class Solution
{
	public int[] ProductExceptSelf(int[] nums)
	{

		// Length of nums
		int L = nums.Length;

		// Result array
		int[] result = new int[L];

		int factor = 1;

		for (int i = 0; i < L; i++)
		{

			result[i] = factor;

			factor *= nums[i];
		}

		factor = 1;

		for (int i = L - 1; i > -1; i--)
		{

			result[i] *= factor;

			factor *= nums[i];
		}

		// Return
		return result;
	}
}