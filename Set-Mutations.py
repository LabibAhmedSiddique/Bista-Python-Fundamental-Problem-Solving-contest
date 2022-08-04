A = int(input())
A_set = str(input())
A_list = A_set.split()  # string list

int_A_list = [int(i) for i in A_list]  # convert to int
A_set = set(int_A_list)  # convert to set

N = int(input())
for i in range(N):

    command = str(input())
    command_list = command.split()
    int_command_num = int(command_list[1])

    if command_list[0] == 'update':
        temp_set = set(map(int, input().split()))
        A_set.update(temp_set)

    elif command_list[0] == 'intersection_update':
        temp_set = set(map(int, input().split()))
        A_set.intersection_update(temp_set)
    elif command_list[0] == 'difference_update':
        temp_set = set(map(int, input().split()))

        A_set.difference_update(temp_set)
    elif command_list[0] == 'symmetric_difference_update':
        temp_set = set(map(int, input().split()))
        A_set.symmetric_difference_update(temp_set)

print(sum(A_set))
