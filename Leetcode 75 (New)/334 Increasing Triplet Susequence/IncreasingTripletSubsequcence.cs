public class Solution
{
	public bool IncreasingTriplet(int[] nums)
	{

		// edge case where length of nums < 3
		if (nums.Length < 3)
		{
			return false;
		}

		int a = int.MaxValue;
		int b = int.MaxValue;

		for (int i = 0; i < nums.Length; i++)
		{
			if (nums[i] <= a)
			{
				a = nums[i];
			}
			else if (nums[i] <= b)
			{
				b = nums[i];
			}
			else
			{
				return true;
			}
		}
		return false;
	}
}