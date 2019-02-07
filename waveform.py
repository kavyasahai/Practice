def sort_wave(a):
    for i in range(0,len(a),2):
        if(i>0 and a[i]<a[i-1]):
            a[i],a[i-1]=a[i-1],a[i]
        elif(i<len(a)-1 and a[i]<a[i+1]):
            a[i],a[i+1]=a[i+1],a[i]

    return a

print(sort_wave([10,5,6,2,20,100,80]))