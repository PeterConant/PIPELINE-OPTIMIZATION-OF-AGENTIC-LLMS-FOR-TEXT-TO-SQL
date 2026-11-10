# Archive

These are earlier versions of the pipeline, kept as a record of how the thesis code developed.
None of them are maintained, and their hardcoded paths match the old `src/` layout. The final
code is in [`text2sql/`](../text2sql/), and the code as it was at thesis submission is at the
`thesis-submission` tag.

| Folder | Version | What it did |
|---|---|---|
| [`v0-langchain-exploration/`](v0-langchain-exploration/) | V0 | First experiments: LangChain's `SQLDatabaseToolkit` agent on local Ollama models, a comparison of model sizes, first custom LangGraph tools, and early evaluation scripts |
| [`v1-baseline/`](v1-baseline/) | V1 | Baseline rebuilt as a LangGraph graph: every `CREATE TABLE` in one prompt, first on SQLite and then on MySQL with vLLM |
| [`v2-llm-table-selection/`](v2-llm-table-selection/) | V2 | The LLM chooses tables through a schema tool. V2.2 splits the work between a tool LLM and a generator LLM, which led to the SLM Selector |
| [`v3-token-measurement/`](v3-token-measurement/) | V3 | Token measurement, used to size vLLM's `--max-model-len`, plus each method as a standalone threaded script. V4 refactored these into shared `agents` / `nodes` / `tools` modules |
| `langgraph-course-notes.ipynb` | — | Notes from a LangGraph course taken while learning the framework |

The run logs for V3 and V4 are in [`mini_dev_main/sql_result/`](../mini_dev_main/sql_result/), and
the day-by-day reasoning is in [`DailyDocumentation.ipynb`](../DailyDocumentation.ipynb).
