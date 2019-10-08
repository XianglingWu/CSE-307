(* Part A *)
fun cycleListOnce(l)=
    tl(l)@(hd(l)::[]);

(* Part B *)
fun cycleList(i,l)=
    if i=0 then l
    else cycleList(i-1,cycleListOnce(l));

val list1Demonstrated = [1,2,3,4,5,6];
val PartA1 = cycleListOnce(list1Demonstrated);
val PartB1 = cycleList(3,list1Demonstrated);


val list2Demonstrated = [46,2,989,456,846,2965,56];
val PartA2 = cycleListOnce(list2Demonstrated);
val PartB2 = cycleList(4,list2Demonstrated);