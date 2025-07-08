def solution(numbers, target):
    answer = 0
    def dfs(idx, total):
        nonlocal answer # 바깥쪽 변수 answer 에 접근
        if idx == len(numbers): # 모든 number 다 탐색했으면 종료조건
            if total == target:
                answer += 1 # total = target이면 answer +1 추가
            return

        # 5) 현재 숫자(numbers[idx])를 ‘더해서’ 다음 단계로
        dfs(idx + 1, total + numbers[idx])
        # 6) 현재 숫자를 ‘빼서’ 다음 단계로
        dfs(idx + 1, total - numbers[idx])

    # 7) 탐색 시작: 인덱스 0, 누적 합 0
    dfs(0, 0)

    # 8) 모든 경우의 수를 확인한 뒤 결과 반환
    return answer
