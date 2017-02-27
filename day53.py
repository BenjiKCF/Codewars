def reverse(st):
    return ' '.join(st.split(' ')[::-1])


print reverse('Hello World') #== 'World Hello'
print reverse('Hi There.') #== 'There. Hi'
