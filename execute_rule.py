import pandas as pd
import json

INPUT_FILE="input.xlsx"
OUTPUT_FILE="output.xlsx"

# 读取原始模板
df=pd.read_excel(INPUT_FILE)

# 读取AI生成规则
with open(
    "rules.json",
    encoding="utf-8"
) as f:

    rules=json.load(f)

output=[]

for _, row in df.iterrows():

    # 保留原始行
    output.append(
        row.to_dict()
    )

    condition=rules["condition"]

    col=condition["column"]

    target=condition["equals"]

    if str(row[col])==target:

        for action in rules["generate"]:

            new_row=row.copy()

            action_col=action["column"]

            action_val=action["value"]

            # 如果引用已有列
            if action_val in row.index:

                new_row[
                    action_col
                ]=row[
                    action_val
                ]

            # 如果固定值
            else:

                new_row[
                    action_col
                ]=action_val

            output.append(
                new_row.to_dict()
            )

final=pd.DataFrame(
    output
)

final.to_excel(
    OUTPUT_FILE,
    index=False
)

print("DONE")