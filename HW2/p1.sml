(* The smallest value for getting overflow is 45 *)
fun f(x)=
    if x<3 then 1
    else f(x-1)+f(x-2);
    