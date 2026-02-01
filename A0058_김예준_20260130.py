class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            # 1. 다음 노드를 미리 저장 (길을 잃지 않게)
            next_node = curr.next
            # 2. 현재 노드의 방향을 뒤로 돌림
            curr.next = prev
            # 3. prev와 curr를 한 칸씩 앞으로 이동
            prev = curr
            curr = next_node
            
        return prev