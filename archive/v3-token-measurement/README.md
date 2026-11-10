# V3: Token measurement and standalone methods

Measuring tokens per prompt set vLLM's `--max-model-len` for each method. Each method is a
standalone script that runs questions in parallel threads.

| File | Contents |
|---|---|
| `V3token_measurements.py` | Measures prompt token counts |
| `token_eval_.ipynb` | Summarizes the token measurements with pandas |
| `V3ThreadedBaseline.py` | Baseline with parallel threads |
| `Sequential.py` | Two-stage pipeline: the LLM chooses tables through a schema tool, then the same LLM writes the SQL. Results are in `mini_dev_main/sql_result/Sequential/` |
| `Agentic.py` | Agent loop that fetches schemas itself, an early version of the Feedback Agent |
| `Embedding_Similarity.py` | First version of embedding-based table selection with FAISS, which became the Semantic Selector |

V4 (now [`text2sql/`](../../text2sql/)) moved the setup these scripts repeat into shared modules.
