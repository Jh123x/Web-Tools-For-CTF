# SQL Injection

## Looking at version

| DB Type    | Query                                                           |
| ---------- | --------------------------------------------------------------- |
| Oracle     | `SELECT banner FROM v$version` `SELECT version FROM v$instance` |
| Microsoft  | `SELECT @@version`                                              |
| PostgreSQL | `SELECT version()`                                              |
| MySQL      | `SELECT @@version`                                              |
| Sqlite3    | `SELECT sqlite_version()`                                       |

## Database contents

| DB Type   | Query                                                                           | Remarks                                                                                                                                                                      |
| --------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Oracle    | `SELECT TABLE_NAME, STATUS, FROM all_tables`                                    | [Full Schema](https://docs.oracle.com/cd/B19306_01/server.102/b14237/statviews_2105.htm#REFRN20286)                                                                          |
| Microsoft | `SELECT TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES` | [Full Schema](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/system-information-schema-views-transact-sql?view=sql-server-ver16) |
| Postgres  | `SELECT TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES` | [Full Schema](https://cloud.google.com/spanner/docs/information-schema-pg)                                                                                                   |
| SQLite3   | `SELECT name FROM sqlite_schema WHERE type='table''`                            | [Full Schema](https://www.sqlitetutorial.net/sqlite-show-tables/)                                                                                                            |

## Table information

| DB Type   | Query                                                                                                                                                                  | Remarks                                                                                                                          |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Oracle    | `SELECT table_name, owner, Tablespace_name, Num_Rows FROM all_tables`                                                                                                  | [Full Schema](https://docs.oracle.com/cd/B19306_01/server.102/b14237/statviews_2105.htm#REFRN20286)                              |
| Microsoft | `SELECT s.name as schema_name, t.name as table_name, c.* FROM sys.columns AS c INNER JOIN sys.tables AS t ON t.object_id = c.object_id WHERE t.name = '<TABLE_NAME>';` | [Full Schema](https://learn.microsoft.com/en-us/sql/relational-databases/tables/view-the-table-definition?view=sql-server-ver16) |
| Postgres  | `SELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_name = 'TABLE_NAME';`                                                           | [Full Schema](https://www.postgresql.org/docs/current/infoschema-columns.html)                                                   |
