def tower_of_hanoi(n,start,end,temp):
    if n==1:
        print("Move disk 1 from rod",start,"to rod",end)
        return
    tower_of_hanoi(n-1,start,temp,end)
    print("Move disk",n,"from rod",start,"to rod",end)
    tower_of_hanoi(n-1,temp,end,start)
tower_of_hanoi(3,"A","C","B")
