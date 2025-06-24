class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        # 최종 상태만 중요함

        # 같은 버튼 짝수번 누르면 상태가 돌아옴 -> 각 버튼은 눌리거나 안눌리거나
        
        # 1 + 2 -> 3 , 1 + 3 -> 2, 2 + 3 -> 1 but 4는 어떻게 해도 만들 수 없음

        # 버튼을 누르는 순서는 상관이 없음 

        # 3k+1만 따로 생각하자


        # 0일때 -> 그대로 1
        # 1일대 -> 3k+1 누르면 0인 것과 곱해짐 / 3k+1인것 안누르면 3 (1인 것)
        # 2일때 -> 3k+1 누르면 1인것과 곱해짐 / 3k+1 안누르면 0인것과 1인것
        # 3일때 -> 3k+1 누르면 2인것과 곱해짐 / 3k+1 안누르면 

        if presses == 0:
            return 1

        if n == 1: 
            return 2

        if n == 2:
            if presses % 2 ==0:
                return 4
            else:
                return 3
        
        if n > 2:
            if presses == 1:
                return 4
            if presses == 2:
                return 3 + 4
            if presses > 2:
                return 3 + 1 + 3 + 1