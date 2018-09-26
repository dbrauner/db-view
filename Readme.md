# DB View scripts

This project is intended to help when creating a database connection for NFeCloud Projects.
Eventually, we need to view/manage the database which is in a Cloud Foundry space, 
for that will need to stabilish a connection with CF using [chisel](https://github.wdf.sap.corp/NFeCloud/chisel), but then
you need to create a connection properly, as defined in the Chisel project.

the script `get_db_connection.py` helps to find the variables for connection, the usage is this:

1. Use the Chisel to connect to the database
```cmd
C:\Users\i844796\git\chisel>connect_dev.bat

```
2. Call the script with the desired space, in this case `dev`
```cmd
C:\Users\i844796\IdeaProjects\db-view>python get_db_connection.py dev
     "dbname": "19a2ea0479a2c51ed7efb9e056c8e9eb",
     "username": "75c0bffcd792959a148cbf34e1817390",
     "password": "9d547a8df965c70e05f979dd8c042e3d",

```
It will print in the console the values for creating the connection.

PS: You will need Python for that =)