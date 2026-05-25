
print('                 TODO LIST BY DARSHAN 😎')
print('')
while True:

    print('1. For Add Task')
    print('2. for View all task')
    print('3. for Delete task')
    print('4. for Exit App')
    print("")
    a = int(input('Enter Your Choise : '))
    print("")
    if a == 1:
        task = (input('Enter Your Task : '))
        
        tasks = task.split(' ')

        file = open("tasks.txt", "a")
        for t in tasks:
            file.write(t.strip() + "\n")
        file.close()
        print('Task added successfully ✅')

    if a == 2:
        file = open("tasks.txt", "r")
        task = file.read()
        file.close()

        print('⬇️   Your Task : ')
        print("")
        print(task)

    if a == 3:

        file = open("tasks.txt", "r")
        tasks = file.readlines()
        file.close()

        print("⬇️   Your Tasks:")
        for i in range(len(tasks)):
            print(i + 1, tasks[i].strip())
        print("")
        nums = input("Enter task number to delete: ")
        nums = nums.split()


        for n in sorted(nums, reverse = True):
            n = int(n)
            if 1<= n <= len(tasks):
                tasks.pop(n - 1)

        file = open("tasks.txt", "w")
        file.writelines(tasks)
        file.close()
        print("")
        print("Task deleted successfully ❌")
    print("") 
    if a == 4:
        print('App Closed Bye')
        break 