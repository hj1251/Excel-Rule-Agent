from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client=OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)

prompt=input(
"""
Describe rule:

"""
)

SYSTEM="""
Convert rule into JSON.

Return ONLY JSON.

Format:

{
 "condition":{

   "column":"",

   "equals":""

 },

 "generate":[

   {

      "column":"",

      "value":""

   }

 ]
}
"""

response=client.responses.create(

    model="gpt-4.1-mini",

    input=[
        {
            "role":"system",
            "content":SYSTEM
        },

        {
            "role":"user",
            "content":prompt
        }
    ]
)

clean=response.output_text

clean=clean.replace(
"```json",
""
)

clean=clean.replace(
"```",
""
)

rule=json.loads(
clean
)

with open(
"rules.json",
"w"
) as f:

    json.dump(
        rule,
        f,
        indent=4
    )

print(
"\nRULE SAVED"
)