###### Department Breakdown

| Department            | Nodes | Locations                          |
| --------------------- | ----- | ---------------------------------- |
| HR                    | 25    | all 25 on floor 1                  |
| Finance               | 28    | all 28 on floor 1                  |
| Sales & Marketing     | 25    | split 16 on floor 1, 9 on floor 2  |
| Legal                 | 25    | all 25 on floor 2                  |
| IT                    | 46    | split 36 on floor 2, 10 on floor 3 |
| Security              | 16    | all 16 on floor 3                  |
| Communications        | 22    | all 22 on floor 3                  |
| Business Consultants  | 61    | split 27 on floor 3, 34 on floor 4 |
| Client Management     | 31    | all 31 on floor 4                  |
| Research and Analysis | 16    | split 4 on floor 4, 12 on floor 5  |
| Project Management    | 16    | all 16 on floor 5                  |
| Executive             | 1     | all 1 on floor 5                   |

###### Totals (~17 access level switches)

| Floor   | Switches | Nodes          |
| ------- | -------- | -------------- |
| Floor 1 | 3        | 25, 28, 16     |
| Floor 2 | 3        | 9, 25, 36      |
| Floor 3 | 4        | 10, 16, 22, 27 |
| Floor 4 | 3        | 34, 31, 4      |
| Floor 5 | 3        | 12, 16, 1      |


| Floor   | Closet | Depts                                                                           | Distribution |
| ------- | ------ | ------------------------------------------------------------------------------- | ------------ |
| Floor 1 | A      | HR (25) D2                                                                      |              |
|         | B      | Finance (28) D2<br>Sales (16) D1                                                |              |
| Floor 2 | A      | Sales (9) D1<br>Legal (25) D2                                                   | Dist A       |
|         | B      | IT (36) D2                                                                      | Dist B       |
| Floor 3 | A      | IT (10) D2<br>Security (16) D1<br>                                              |              |
|         | B      | Communications (22) D1<br>Business Consultants (27) D1                          |              |
| Floor 4 | A      | Business Consultants (34) D1                                                    |              |
|         | B      | Client Management (31) D1<br>Research and Analysis (4) D2                       |              |
| Floor 5 | A      | Research and Analysis (12) D2<br>Project Management (16) D2<br>Executive (1) D2 |              |
|         | B      |                                                                                 |              |

###### Notes:
- Each department should be networked with future expansion in mind
	- at least one step higher than required number of ports to accommodate growth
	- will also provide "executives" the connectivity they will require (see below)
	- will also provide space for ap connection
- Assignment brief mentions executives:
	- "...executives without their own offices are accommodated in standard cubicles situated alongside other staff members within their respective departments..."