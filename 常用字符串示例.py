# Quotation Manipulation
# 演示字符串方法

# IBM主席thomas Watson在1943年的时候说的
quote = "I think there is a world market for maybe five computers."
print("quote:I think there is a world market for maybe five computers.")

print("\n\nOriginal quote:")
print(quote)

print("\n In uppercase:")
print(quote.upper())
# upper()返回字符串的大写形式

print("\n In lowercase")
print(quote.lower())
# lower()返回字符串的小写形式

print("\n As a title")
print(quote.title())
# title()返回一个新的字符串，每个单词的首字母大写，其余小写

print("\n With a minor replacement")
print(quote.replace("five", "millions of"))
# replace(old,new[,max])返回一个新的字符串，原始字符串中的字符串old会被替换成字符串new。可选的max用于限制替换的次数

print("\n In inverse")
print(quote.swapcase())
# swapcase()返回一个新的字符串，其中的大小写形式互换。

print("\n 除去空白")
print(quote.strip())
# strip()返回一个新的字符串，原始字符串首尾处的一切空白符（即制表符、空格、换行符等）都会被去除掉

print("\n\n\nSaying:i am a boy.")
Saying = "i am a boy."
print("\nIn a sentence")
print(Saying.capitalize())
# capitalize()返回一个新的字符串，首字母大写其余小写。


input("\n\n\n\nPress the enter key to exit")
