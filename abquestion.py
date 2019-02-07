def divide_chunks(l,n):
    for i in range(0, len(l),n):
        yield l[i:i+n]

def solution(a,b):
        list1=[];
        list2=[];
        listfinal=[];
        for i in range(0,b):
            list1.append('b');
        for i in range(0, a):
            list2.append('a');

        n=2
        a=list(divide_chunks(list2, n))
        b=list(divide_chunks(list1,n))
        print(a)
        print(b)

        while(a and b) :
                listfinal.append(a.pop());
                listfinal.append(b.pop());
        return listfinal

print(solution(5,4))


