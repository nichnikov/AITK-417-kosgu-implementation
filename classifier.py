import os
import re
import pandas as pd
from src.texts_processing import TextsTokenizer

keys_df = pd.read_csv(os.path.join("data", "keys.csv"), sep="\t")
keys = list(keys_df["keys"])
modid = list(keys_df["modid"])

tokenizer = TextsTokenizer()
lm_keys = [" ".join(l) for l in tokenizer(keys)]

k_m_dict = {k: m for k, m in zip(lm_keys, modid)}

queries_df = pd.read_csv(os.path.join("data", "queries.csv"), sep="\t")
queries = list(queries_df["text"])
lm_queries = [" ".join(l) for l in tokenizer(queries)]

patterns = re.compile("|".join(lm_keys))
queries_dicts = queries_df.to_dict(orient="records")
results = []
for lm_q, d in zip(lm_queries, queries_dicts):
    # r = patterns.search(lm_q)
    r = patterns.findall(lm_q)
    if r:
        # d["find_text"] = r.group()
        # d["find_modid"] = k_m_dict[r.group()]
        d["find_texts"] = list(set(r))
        d["find_modids"] = list(set([k_m_dict[i] for i in r]))
    else:
        d["find_texts"] = "No"
        d["find_modids"] = "No"
    results.append(d)

results_df = pd.DataFrame(results)
results_df.to_csv(os.path.join("data", "kosgu_search_result.csv"), sep="\t", index=False)
print(results_df)