# V1: Baseline as a LangGraph graph

In this baseline, every `CREATE TABLE` statement goes into one prompt and the LLM writes the SQL.

| File | Contents |
|---|---|
| `V1.0LangraphBaseLine.ipynb` | Notebook prototype of the graph |
| `V1.1BaseLinesqlite.py` | Script version that runs on the SQLite BIRD databases |
| `V1.2BaseLinemysql.py` | Moves to MySQL (`bird_mini_dev`) and a vLLM server |
| `MySQL_test.ipynb` | Test queries against the MySQL database |
