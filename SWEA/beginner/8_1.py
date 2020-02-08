S = input()

list = []


if len(S) % 2 == 0:
    for i in range(len(S)//2):
        if S[i] == S[len(S) - i - 1]:
            list.append(i)
            if len(list) == len(S):
                print(S)
                print('입력하신 단어는 회문(Palindrome)입니다.')
else:
    for i in range(len(S)//2 - 1):
        if S[i] == S[len(S) - i - 1]:
            list.append(S[len(S)//2])
            list.append(i)
            if len(list) == len(S):
                print(S)
                print('입력하신 단어는 회문(Palindrome)입니다.')
    

# def palindromeCheck(m_str):
   
#    for i in range(0, len(m_str)):
      
#       if m_str[i] != m_str[len(m_str)-1-i]:
#          return False
#       return True
 
# t = input()
# print(t)
# if palindromeCheck(t) : 
#    print("입력하신 단어는 회문(Palindrome)입니다.")
# else :
#    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")