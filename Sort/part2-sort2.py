# 정렬 문제 2 : 성적이 낮은 순서로 학생 출력하기

# N명의 학생 정보가 있다.
# 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하라.

students = [
	('홍길동', 95),
	('이순신', 77),
]

def my_solution(students):
		sortList = sorted(students, key=lambda student: student[1])
		return list(map(lambda student: student[0], sortList))

print(my_solution(students))