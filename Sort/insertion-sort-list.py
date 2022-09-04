# 삽입 정렬 리스트

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
		def insertionSortList(self, head: ListNode):
        # 초기값 변경
				cur = parent = ListNode(0)

				while head:
						# 처음엔 무조건 건너띔
						while cur.next and cur.next.val < head.val: cur = cur.next
						# step 1
						# 1: cur.next(None)는 head[4, 2, 1, 3]를 넣어서 [0, 4, 2, 1, 3] 변경됨
						# 2: head.next[2, 1, 3]는 cur.next(None)으로 변경됨
								# cur.next.next가 head.next와 주소가 같다.
						# 3: head[4, 2, 1, 3]는 head.next[2, 1, 3]로 변경됨 => 이 친구는 아직 검사안함 것
						cur.next, head.next, head = head, cur.next, head.next

						# 필요한 경우에만 cur 포인터가 되돌아가도록 처리
						if head and cur.val > head.val: cur = parent

				return parent.next

listNode = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
test = Solution()
print(test.insertionSortList(listNode))

# 뫼비우스의 띠이다... 동시에 한번에 빡 처리되니까 헷갈리는 것이다.
# step 0. cur.next 가 [None]
# step 1. cur.next 가 [4 None] <-- head <-- head.next(그럼 나는 날라가...? 아니 head) <-- cur.next
# step 2. cur.next 가 [2 4 None] <-- head(1, 3) <-- head.next(4 None) <-- cur.next
