'''
/*********************************************************************
*Title : 1로 만들기
*Number : <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" class="solvedac-tier">&nbsp;1463번
*Author : ro1864
*Description : 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.X가 3으로 나누어 떨어지면, 3으로 나눈다.X가 2로 나누어 떨어지면, 2로 나눈다.1을 뺀다.정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오. 
*Input : 첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.
*Output : 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
*Start Time : 2023년 0월 29일 3시 29분 7초
*End Time : 2023년 0월 29일 시 분 초
*comments program : https://chrome.google.com/webstore/detail/boj-blog-post/ehhcjhfkaiohgflkjifmageahncijacd?hl=ko
*********************************************************************/

이 방법은 다른 사람들에 비해 많이 느린 편이라 수정이 필요할 것 같음.
'''

import sys
input = sys.stdin.readline

x = int(input())

dp = [0] * (x + 1)

for i in range(2, x+1):
    dp[i] = dp[i - 1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
print(dp[x])