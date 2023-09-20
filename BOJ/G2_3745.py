import sys
input=sys.stdin.readline

def binary_search(lis, num):
    left=0
    right=len(lis)-1
    while left<right:
        mid=(left+right)//2
        if (num>lis[mid]): #들어갈 수 있는 인덱스 찾음
            left=mid+1
        else:
            right=mid
            
    return right

while True:
    try:
        n=int(input())
        lst=list(map(int, input().split())) #수열 입력받음
        
        lis_len=[1] #증가 부분 수열 길이 저장
        lis=[lst[0]] #증가 부분 수열 저장
        
        for i in range(1,n):
            if lst[i]>lis[-1]: #현재 수가 저장된 마지막 수보다 클 경우
                lis_len.append(lis_len[-1]+1) #길이 정보 갱신
                lis.append(lst[i]) #현재 값 추가
            else:
                idx=binary_search(lis, lst[i]) #증가 부분 수열에서 들어갈 수 있는 곳 찾음
                lis[idx]=lst[i] #현재 값 lis 배열에 넣어줌
                
        print(lis_len[-1]) #최종 길이
    except: #입력 없을 때
        sys.exit(0)