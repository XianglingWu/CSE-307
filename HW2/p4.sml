fun list1(L) =
if L = nil then nil
else hd(L)::list3(tl(L))
and
list2(L) =
if L=nil then nil
else list1(tl(L))
and
list3(L) =
if L=nil then nil
else list2(tl(L));


val listDemonstrated = [46,2,989,456,846,2965,56,6];
val firstList = list1(listDemonstrated);
val secondList = list2(listDemonstrated);
val thirdList = list3(listDemonstrated);