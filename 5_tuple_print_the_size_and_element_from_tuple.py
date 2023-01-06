"""Assume, you have been given a tuple.
book_info = (
("Best Mystery & Thriller","The Silent Patient",68,821),
("Best Horror","The Institute",75,717),
("Best History & Biography","The five",31,783 ),
("Best Fiction","The Testaments",98,291)
)
Write a Python program that prints the size of the tuple and all its elements as shown below.
===================================================================
Output:
Size of the tuple is: 4
('Best Mystery & Thriller', 'The Silent Patient', 68, 821)
('Best Horror', 'The Institute', 75, 717)
('Best History & Biography', 'The five', 31, 783)
('Best Fiction', 'The Testaments', 98, 291)
===================================================================
"""




# solution:

given_tuple= (
("Best Mystery & Thriller","The Silent Patient",68,821),
("Best Horror","The Institute",75,717),
("Best History & Biography","The five",31,783 ),
("Best Fiction","The Testaments",98,291)
)
 
print("Size of the tuple is: ", len(given_tuple))

for i in given_tuple:
  print(i)