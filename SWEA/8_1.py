def Palindrome(S):

    for i in range(len(S)):

        if s[i] != s[len(S)-1-i]:
            return False
        return True

s = input()
print(s)
if Palindrome(s):
    print('입력하신 단어는 회문(Palindrome)입니다.')
else:
    print('입력하신 단어는 회문(Palindrome)이 아닙니다.')