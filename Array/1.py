# 두 수의 합
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

nums = [15, 11, 7, 6, 4, 2]
target = 9

# 무차별 대입 방식인 브루트 포스말고 다른 방법으로 풀기
# 투 포인터 이용하기 (O(n)) -> 그런데 정렬해야함 -> 그러면 인덱스를 구할 수가 없다...
# 투 포인터란: 왼쪽 포인터와 오른쪽 포인터의 합이 
# 타겟보다 크면 오른쪽 포인터를 왼쪽으로,
# 탸겟보다 작다면 왼쪽 포인터를 오른쪽으로 옮기면서 값을 조정하는 방식이다.
def twoSum1(nums, target):
		nums.sort()
		left, right = 0, len(nums) - 1
  
		while not left == right:
				# 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
				if nums[left] + nums[right] < target: left += 1
				# 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
				elif nums[left] + nums[right] > target: right -= 1
				else: return [left, right]
    
# 첫 번째 수를 뺀 결과 키 조회
def twoSum2(nums, target):
		nums_map = {}
  
		# 키와 값을 바꿔서 딕셔너리로 저장
		for i, num in enumerate(nums): nums_map[num] = i
		print(nums_map)
  
		# 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
		for i, num in enumerate(nums):
				if target - num in nums_map and i != nums_map[target - num]:
						return [i, nums_map[target - num]]
  
print(twoSum2(nums, target))