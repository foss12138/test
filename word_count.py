import torch
def wordcount(text):
    word_dict = {}
    words = text.lower().split()
    for word in words:
        word = ''.join(char for char in word if char.isalnum())
        if word:  # If word is not empty
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
                
    return word_dict

#单步调试是指逐行执行代码，包括进入函数内部执行
#逐过程调试是指逐行执行代码，跳过函数的内部执行，直接执行完函数后返回结果
#断点就是执行到这里时（还未执行此行），暂停运行
if __name__ == "__main__":
    text = input("Please enter the text to analyze: ")
    result = wordcount(text)
    print("Word count result:")
    for word, count in result.items():
        print(f"{word}: {count}")
