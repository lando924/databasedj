### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

  PostgreSQL is an ORM (object relational database) management system that uses SQL as its query language.

- What is the difference between SQL and PostgreSQL?

  SQL is the language used to communicate with relational databases. PostgreSQL uses SQL to interact with relational databases, like creating tables, defining schemas, and retrieving data.

- In `psql`, how do you connect to a database?

  You can do one of the following in the terminal zsh shell,
  psql
  \c name_of_database

- What is the difference between `HAVING` and `WHERE`?

  'WHERE' filters rows before any grouping is done in the query. It's used to specify conditions on individual rows in a table.

  'HAVING' filters grouped data after the GROUP BY clause. It's used to specify conditions on aggregate functions.

- What is the difference between an `INNER` and `OUTER` join?

  'INNER JOIN' combines rows from two tables where there is a match in the join condition. It returns only the matching rows from both tables.

  'OUTER JOIN' combines rows from two tables and includes non-matching rows from one or both tables. 

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  'LEFT OUTER' join includes all rows from the left table and the matching rows from the right table. If there is no match then the result will contain NULL.

  'RIGHT OUTER' does the same just from right to left.

- What is an ORM? What do they do?

  ORM map classes to database tables. It's just a simple way of working with relational databases. It makes development fater, and reduces the need for raw SQL.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

  The main difference between the two is that HTTP requests are client side (directly from browser). Using requests(server-side) doesn't make it visible to the user. Usually used in backend languages.

- What is CSRF? What is the purpose of the CSRF token?

  CSRF (Cross-Site Request Forgery) is a type of web security vulnerability where an attacker tricks a victim into performing unintended actions on a website or web application in which the victim is authenticated. The purpose of the CSRF token is to prevent attacks by creating unique random tokens for each session or form.

- What is the purpose of `form.hidden_tag()`?

  Flask-WTF automatically includes a CSRF token for every form to protect against Cross-Site Request Forgery (CSRF) attacks. It is used to insert hidden fields with the CSRF tokens. Helps ensure security.