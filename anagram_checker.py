# anagram_checker.py

word1 = input("choose first word to anagram check >")
word2 = input("choose second word to anagram check >")
word1 = word1.lower()
word2 = word2.lower()
print(word1)
word1_list = list(word1)
word2_list = list(word2)
print(word1_list)
word1_list.sort()
word2_list.sort()
if word1_list == word2_list:
    print("anagram!")
