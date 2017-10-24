let print_int x = Printf.printf "%d\n" x;;
let read_int () =
  Scanf.scanf " %d" (fun x->x)

let rec double nb =
  if nb = 0 then ()
  else
    begin
      print_int (read_int()*2);
      double(nb-1);
    end

let _ = double (read_int());;
