# n = list(str(input()))  #리스트로 쪼개고
# # print(n)
# n = sorted(n, reverse=True)  #뒤집어서 정렬하고
# # print(n)
# k = ''.join(n)  #합쳐서 추출하고
# # print(k)
# print(k)  #출력하면 끝

#상남자 특 한줄로 모든 풀이 끝냄
print(''.join(sorted(list(str(input())), reverse=True)))