
fun add1(num)= num+1;
fun add2(num)= num+2;
fun add3(num)= num+3;

fun F(funList,argList)=
if argList = [] then nil
else (hd(argList),hd(funList)(hd(argList)))::F(tl(funList),tl(argList));

val funList = [add1,add2,add3];
val argList = [4,456,9480];
val Demo = F(funList,argList);