__author__ = 'Jorian'
def acronym(phrase):
    ans = ""
    for word in phrase.split():
        ans = ans + word[0]
    return ans.upper()

def main():
    print("Acronym Builder")
    words = input("Enter a phrase: ")
    print("Acronym:", acronym(words))

main()