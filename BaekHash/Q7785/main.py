N = int(input())
vis = [list(map(str, input().split())) for _ in range(N)]

vis_table = {key: value for key, value in vis}

result = [key for key, value in vis_table.items() if value == "enter"]

print("\n".join(sorted(result, reverse=True)))