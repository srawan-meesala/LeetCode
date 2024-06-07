tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
st = []
for i in tokens:
    if i in ['+', '-', '*', '/']:
        a = st.pop()
        b = st.pop()
        if i == '+':
            st.append(a+b)
        elif i == '-':
            st.append(b-a)
        elif i == '*':
            st.append(b*a)
        elif i == '/':
            if a < 0 and b < 0:
                st.append((-b)//(-a))
            elif a < 0 and not b < 0:
                st.append((b)//(-a))
            elif not a < 0 and b < 0:
                st.append((-b)//(a))
            else:
                st.append((b)//(a))
        print(st)
    else:
        st.append(int(i))
        print(st)

print(st)