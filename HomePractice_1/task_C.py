'''
n = int(input())
spaces = [int(input()) for _ in range(n)]

total_presses = 0
current_spaces = 0

for space in spaces:
    if space > current_spaces:
        total_presses += (space - current_spaces) // 4 + (space - current_spaces) % 4
    elif space < current_spaces:
        total_presses += (current_spaces - space) // 4
    current_spaces = space

print(total_presses)'''

n = int(input())
a = [int(input()) for _ in range(n)]
print(sum(k // 4 + min(k % 4, 2) for k in a))