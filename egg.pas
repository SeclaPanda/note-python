var
    count, j, k, sqrtI, num: longint;
begin
    num := 452022;
    count := 0;
    while True do begin
        sqrtI := round(sqrt(num));
        for j := 2 to sqrtI do begin
            if num mod j = 0 then begin
               if (j + num div j) mod 7 = 3 then begin
                  count := count + 1;
                  writeln(num, ' ', j + num div j);
                  break;
               end
               else break;
            end;
        end;
        if count = 5 then break;
        num := num + 1;
    end;
end.