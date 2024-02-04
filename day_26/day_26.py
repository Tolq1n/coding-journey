#151. Reverse Words in a String

def reverseWords(s):
    return " ".join(s.split()[::-1])

print(reverseWords(" the sky is blue "))