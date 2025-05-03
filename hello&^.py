s="I Hate Indian Traditions"
print("original\tAND 127 \tOR 127")
for p in s:
    and_res=ord(p) & 127
    or_res=ord(p)^127
    print(f"{p}({ord(p)})\t\t {and_res}\t\t {or_res}")