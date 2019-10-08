
fun duplicateList([])=[]
    |duplicateList(x::y)=
        x::x::duplicateList(y);


val list1Demonstrated = [1,2,3,4,5,6];
val Demo1 = duplicateList(list1Demonstrated);
val list2Demonstrated = [46,2,989,456,846,2965,56];
val Demo2 = duplicateList(list2Demonstrated);