def find(sub, s) :
   sub_index_beg = 0
   sub_index_end = len(sub) - 1
   sub_char_beg = sub[sub_index_beg];
   sub_char_end = sub[sub_index_end];

   s_index_beg = sub_index_beg;
   s_index_end = sub_index_end;

   while (s_index_end < len(s)) :
     if s[s_index_beg] == sub_char_beg and s[s_index_end] == sub_char_end : 
       i = s_index_beg + 1
       j = 1
       match = True;
       while  j < len(sub) - 1 :
         if s[i] != sub[j] :
            match = False;
         j = j+1;
         i = i+1
       if match == True:
         print("Match");
         return s_index_beg
     s_index_end = s_index_end + 1
     s_index_beg = s_index_beg + 1

   return -1 


