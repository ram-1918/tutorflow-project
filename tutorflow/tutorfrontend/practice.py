# val = 1
# for i in range(0,5):
#     res = ''
#     for j in range(i+1):
#         res += ' '+str(val)
#         val += 1
#     print(res)

# space = 4-1
# for i in range(4):
#     exp = ''
#     for j in range(2*i+1+1):
#         exp += str(j)
#     print((space - i)*' ' + rev + exp)

def pyramid(space, prev, j, val):
    if j == val: return prev
    prev = space*' '+str(prev) if j == 1 else space*' '+str(j)+str(prev)+str(j)
    print(prev)
    return pyramid(space-1, prev.strip(' '), j + 1, val)
val = int(input())
pyramid(val-1,1,1,val)



# # String res =
#  '';
# # int val = 1;
# # for(int i = 0; i < 5; i++){
# #     res = ''
# #     for(int j = 0; j < i + 1; j++){
# #         res += ' '+ val;
# #         val += 1;
# #     }
# #     System.out.println(res)
# # }
# dp = [[1]*(i+1) for i in range(10)]
# for i in range(2, 10):
#     for j in range(1, len(dp[i-1])):
#         dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
# print(dp)