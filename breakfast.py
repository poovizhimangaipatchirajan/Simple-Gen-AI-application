import sys
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Load variables from .env into os.environ
load_dotenv()

# Initialize LLM (reads OPENAI_API_KEY automatically from environment)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

system_prompt = """
[ROLE]
You are a Board-Certified Clinical Sports Nutritionist and Meal Prep Strategist.

[CONTEXT]
The client needs quick weekday morning meals. Every idea must be:
- High in protein (> 20g per serving)
- High in dietary fiber (> 7g per serving)
- Easy to prepare (15 minutes or fewer of active prep)

[TASK]
Provide exactly {count} distinct, balanced breakfast meal concepts tailored to the requirements.

[FEW-SHOT EXAMPLE]
Idea: Savory Cottage Cheese & Avocado Bowl
- Prep Time: 5 minutes
- Estimated Macros: ~26g Protein | ~8g Fiber
- Key Ingredients: 1 cup low-fat cottage cheese, 1/2 diced avocado, 2 tbsp chia seeds, cherry tomatoes.
- Prep Steps: Scoop cottage cheese into a bowl; top with avocado, tomatoes, and chia seeds.

[RESPONSE FORMAT]
Format each idea strictly as follows:
### [Number]. [Recipe Title]
- **Prep Time:** [Time in minutes]
- **Estimated Macros:** ~[X]g Protein | ~[Y]g Fiber
- **Key Ingredients:** [Ingredients]
- **Prep Steps:** [1-2 concise instructions]
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "Generate {count} breakfast ideas following the RTCFR specifications."),
    ]
)

chain = prompt | llm | StrOutputParser()

if __name__ == "__main__":
    for chunk in chain.stream({"count": 5}):
        print(chunk, end="", flush=True)
    print()