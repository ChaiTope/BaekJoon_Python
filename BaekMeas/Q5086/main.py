Ext = []
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        if B % A == 0:
            Ext.append("factor")
        elif A % B == 0:
            Ext.append("multiple")
        else:
            Ext.append("neither")

print("\n".join(Ext))