# Part3 구현 문제 4: 자물쇠와 열쇠

# 자물쇠의 돌기와 열쇠의 돌기가 만나서는 안된다.
# 자물쇠의 모든 홈이 열쇠와 맞아야한다.

# [풀이 방법 1]
# 모든 회전을 검사한다.
# 모든 칸을 이동해서 검사한다.

# TODO: key 방향 변경 함수
def change_direction(direction):
		# TODO: direction에 따라 방향을 바꾼다.
		return direction

# TODO: 유효성 검사 함수
def validation_check(key, lock, idx):
		# TODO: 자물쇠의 돌기와 열쇠의 돌기가 만나서는 안된다.
		if 1 == 2: return False
		# TODO: 자물쇠의 모든 홈이 열쇠와 맞아야 한다.
		if 1 == 2: return True
		return False

def solution(key, lock):
		lock_row = len(lock)
		lock_col = len(lock[0])

		# 검사 할 회전 수 : (3 * 5) + (2 * 5)
		turns = lock_row * (lock_col * 2 - 1) + (lock_col - 1) * (lock_col * 2 - 1)

		# 네 방향 모두 검사
		direction = 4

		while direction > 0:
				if direction != 4: change_direction(direction)

				for idx in range(turns):
						if validation_check(key, lock, idx): return True

				direction -= 1

		return False

solution([[0,0,0], [1,0,0], [0,1,1]], [[1,1,1], [1,1,0], [1,0,1]])