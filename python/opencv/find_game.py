table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+='
ODL = map(int, '13572064')
def trans(x):
    l = x & 7
    h = (x >> 3) & 7
    n_h = ODL.index(h)
    n_l = ODL.index(l)
    return (n_h << 3) + n_l


s = 'U2FsdGVkX1+GwlYSkb6ewlmShlAAR+k1oKV87HFVoZlaCLiKUa3RsXxMlzs88xv2gvX9wXRao4SLaiOyB8l13w=='
new_table = sorted(table, key=lambda c: trans(table.index(c)))
print new_table
s_l = len(s)
i = 0
num_list = []
while i < s_l:
    num = 0
    for t in range(3, -1, -1):
        order = new_table.index(s[i])
        num += order << t * 6
        i += 1
        if i >= s_l:
            break
    num_list.append(num)
str_num_list = []
for num in num_list:
    for i in range(2, -1, -1):
        temp_num = (num >> (i * 8)) & 255
        str_num_list.append(temp_num)
s = str(map(chr, str_num_list))
print s
