import json




prompt_301 = "Let's first understand the problem, extract relevant variables and their corresponding numerals, " \
             "and devise a plan. Then, let's carry out the plan, calculate intermediate variables (pay attention to " \
             "correct numeral calculation and commonsense), solve the problem step by step, and show the answer."
prompt_305 = "Let's first understand the problem, extract relevant variables and  their corresponding numerals, " \
             "and make a complete plan. Then, let's carry out the plan, calculate intermediate variables (pay " \
             "attention to correct numerical calculation and commonsense), " \
             "solve the problem step by step, and show the answer."
prompt_jx_302 = "Let's first understand the given math problem carefully, extract relevant variables and their corresponding numerals, and then"\
"propose a step-by-step plan to solve the problem."\
"Then apply the appropriate mathematical formula to each step in the plan to calculate(pay attention to accurate calculations and follow the order of steps strictly.)."
prompt_jx_303 = """\
You are an expert in  arithmetic reasoning.Let's use the following steps to solve the problem.
[Steps]
1. **Understand the Problem**: Carefully read and analyze the given math problem. Identify the question being asked and the information provided.\

2. **Identify Variables**: Extract the relevant variables from the problem, along with their corresponding values if given. This may include quantities, rates, percentages, etc.\

3. **Plan a Solution**: Develop a step-by-step plan to solve the problem. This should outline each operation or procedure you'll need to perform in order to reach the solution.

4. **Apply Formulas**: For each step in your plan, apply the appropriate mathematical formulas or principles. This might include algebraic equations, geometric formulas, arithmetic operations, etc.

5. **Calculate Correctly**: Ensure accurate calculations at each step. It's crucial to maintain precision and avoid rounding errors until the final step. Remember to strictly follow the order of operations in your calculations.
[Answer]
"""
prompt_jx_304 = """\
You are an expert in  arithmetic reasoning.Let's use the following steps to solve the problem.
The answer should be a choice belogs to answer choice.
[Steps]
1. **Understand the Problem**: Carefully read and analyze the given math problem. Identify the question being asked and the information provided.\

2. **Identify Variables**: Extract the relevant variables from the problem, along with their corresponding values if given. This may include quantities, rates, percentages, etc.\

3. **Plan a Solution**: Develop a step-by-step plan to solve the problem. This should outline each operation or procedure you'll need to perform in order to reach the solution.

4. **Apply Formulas**: For each step in your plan, apply the appropriate mathematical formulas or principles. This might include algebraic equations, geometric formulas, arithmetic operations, etc.

5. **Calculate Correctly**: Ensure accurate calculations at each step. It's crucial to maintain precision and avoid rounding errors until the final step. Remember to strictly follow the order of operations in your calculations.
[Answer]

"""
prompt_jx_305 = """\
You are an expert in  arithmetic reasoning.Let's use the following five steps to solve the problem.
The answer should be a choice belogs to answer choice.
[Steps]
1. **Understand the Problem**: Carefully read and analyze the given math problem. Identify the question being asked and the information provided.\

2. **Identify Variables**: Extract the relevant variables from the problem, along with their corresponding values if given. This may include quantities, rates, percentages, etc.\

3. **Plan a Solution**: Develop a step-by-step plan to solve the problem. This should outline each operation or procedure you'll need to perform in order to reach the solution.

4. **Apply Formulas**: For each step in your plan, apply the appropriate mathematical formulas or principles. This might include algebraic equations, geometric formulas, arithmetic operations, etc.

5. **Calculate Correctly**: Ensure accurate calculations at each step. It's crucial to maintain precision and avoid rounding errors until the final step. Remember to strictly follow the order of operations in your calculations.
Please show the process and the answer.
"""
prompt_jx_306 = """\
You are an expert in  arithmetic reasoning.Let's use the following five steps to solve the problem.
[Steps]
1. **Understand the Problem**: Carefully read and analyze the given math problem. Identify the question being asked and the information provided.\

2. **Identify Variables**: Extract the relevant variables from the problem, along with their corresponding values if given. This may include quantities, rates, percentages, etc.\

3. **Plan a Solution**: Develop a step-by-step plan to solve the problem. This should outline each operation or procedure you'll need to perform in order to reach the solution.

4. **Apply Formulas**: For each step in your plan, apply the appropriate mathematical formulas or principles. This might include algebraic equations, geometric formulas, arithmetic operations, etc.

5. **Calculate Correctly**: Ensure accurate calculations at each step. It's crucial to maintain precision and avoid rounding errors until the final step. Remember to strictly follow the order of operations in your calculations.
Please show the process and the answer.
"""
prompt_jx_307 = """\
You are an expert in arithmetic reasoning.Let's use the following five steps to solve the problem.
[Steps]
1. **Understand the question**:Figure out the meaning of the question,include the target of the question and the relation between variables.
2. **Identify Variables**: Extract the correct relevant variables from the problem, along with their corresponding values if given. This may include quantities, rates, percentages, etc.\
3. **Plan a Solution**: Develop a step-by-step plan to solve the problem. This should outline each operation or procedure you'll need to perform in order to reach the solution.
4. **Apply Formulas**: For each step in your plan, apply the appropriate mathematical formulas or principles. This might include algebraic equations, geometric formulas, arithmetic operations, etc.
5. **Calculate**: Ensure accurate calculations and calculate formulas to get result. Remember to strictly follow the order of operations in your calculations.
Please show the reasoning process and the answer.
"""
prompt_jx_308 = """\
You are an expert in arithmetic reasoning.Let's use the following five steps to solve the problem.
The answer should be a choice belogs to answer choice.
[Steps]
1. **Understand the question**:Figure out the meaning of the question,include the target of the question and the relation between variables.
2. **Identify Variables**: Extract the correct relevant variables from the problem, along with their corresponding values if given. This may include quantities, rates, percentages, etc.\
3. **Plan a Solution**: Develop a step-by-step plan to solve the problem. This should outline each operation or procedure you'll need to perform in order to reach the solution.
4. **Apply Formulas**: For each step in your plan, apply the appropriate mathematical formulas or principles. This might include algebraic equations, geometric formulas, arithmetic operations, etc.
5. **Calculate**: Ensure accurate calculations and calculate formulas to get result. Remember to strictly follow the order of operations in your calculations.
Please show the reasoning process and the answer.
"""
prompt_jx_309 ="""\
You are an expert in arithmetic reasoning.Let's use the following four steps to solve the math problem.
question, information, 
[Steps]
1. **Identify Variables**: Extract the correct relevant variables from the problem, along with their corresponding values if given.
2. **Plan a Solution**: Develop a step-by-step plan to solve the problem. 
3. **Apply Formulas**: For each step in your plan, apply the appropriate mathematical formulas or principles. This might include algebraic equations, geometric formulas, arithmetic operations, etc.
4. **Calculate**: Ensure accurate calculations and calculate formulas to get result. Remember to strictly follow the order of operations in your calculations.
Please show the reasoning process and the answer.
"""
prompt_jx_201 ="""\
You are an expert in arithmetic reasoning.Let's use the following four steps to solve the math problem.
[Steps]
1. **Identify Variables**: Extract the correct relevant variables from the problem, along with their corresponding values if given.
2. **Plan a Solution**: Develop a step-by-step plan to solve the problem. 
3. **Apply Formulas**: For each step in your plan, apply the appropriate mathematical formulas or principles. This might include algebraic equations, geometric formulas, arithmetic operations, etc.
4. **Calculate**:  Strictly follow the order of operations in your calculations  and calculate correctly.
Please show the reasoning process and the answer.
"""
prompt_jx_202 ="""\
You are an expert in arithmetic reasoning.Let's use the following four steps to solve the math problem.
[Steps]
1. **Identify Variables**: Extract the correct relevant variables from the problem, along with their corresponding values if given.
2. **Plan a Solution**: Develop a step-by-step plan to solve the problem. 
3. **Apply Formulas**: For each step in your plan, apply the appropriate mathematical formulas or principles..
4. **Calculate**:  Strictly follow the order of operations in your calculations  and calculate correctly.
Please show the reasoning process and the answer.
"""
prompt_jx_211 ="""\
You are an expert in arithmetic reasoning.Let's use the following four steps to solve the math problem.
[Steps]
1. **Identify Variables**: Extract the correct relevant variables and their corresponding values from the problem.
2. **Plan a Solution**: Develop a step-by-step plan to solve the problem. 
3. **Apply Formulas**: For each step in your plan, apply the appropriate mathematical formulas or principles. This might include algebraic equations, geometric formulas, arithmetic operations, etc.
4. **Calculate**:  Strictly follow the order of operations in your calculations  and calculate correctly.
Please show the reasoning process and the answer.
"""
prompt_jx_212 ="""\
You are an expert in arithmetic reasoning.Let's use the following four steps to solve the math problem.
[Steps]
1. **Identify Variables**: Extract the correct relevant variables and their corresponding values from the problem.
2. **Plan a Solution**: Develop a simple step-by-step plan. 
3. **Apply Formulas**: For each step in your plan, apply the appropriate mathematical formulas or principles.
4. **Calculate**:  Strictly follow the order of operations in your calculations and calculate correctly.
Please show the reasoning process and the answer.
"""
prompt_jx_401 ="""\
You are an expert in common sense reasoning.Let's use the following steps to solve the problem.
[Steps]
1. **Plan a Solution**: Develop a simple step-by-step plan.
2. **Solve the problem**:  Follow the order of your plan and choose the unique choice.
Please show the reasoning process and the answer.
"""

prompt_jx_402 ="""\
You are an expert in common sense reasoning.Let's use the following steps to solve the problem concisely.
[Steps]
1. **Plan a Solution**: Develop a simple step-by-step plan.
2. **Solve the problem**:  Follow the order of your plan and choose the unique best choice.
Please show the reasoning process and the answer.
"""
prompt_jx_501 ="""\
You are an expert in concatenating characters.Let's use the following  steps to answer the question.
[Steps]
1. **Plan a Solution**: Develop a step-by-step plan. 
2. **Solve the problem**: Follow the order of your plan.
Please show the reasoning process and the answer.
"""
prompt_jx_502 ="""\
You are an expert in concatenating characters.Let's use the following  steps to answer the question concisely.
[Steps]
1. **Plan a Solution**: Develop a simple step-by-step plan. 
2. **Solve the problem**: Follow the order of your plan.
Please show the reasoning process and the answer.
"""
prompt_jx_601 ="""\
You are an expert in guessing coins.Let's use the following  steps to answer the question.
[Steps]
1. **Plan a Solution**: Develop a step-by-step plan. 
2. **Solve the problem**: Follow the order of your plan.
Please show the reasoning process and the answer.
"""
prompt_jx_602 ="""\
You are an expert in guessing coins.Let's use the following  steps to answer the question concisely.
[Steps]
1. **Plan a Solution**: Develop a simple step-by-step plan. 
2. **Solve the problem**: Follow the order of your plan.
Please show the reasoning process and the answer.
"""
prompt_jx_701 ="""\
You are an expert in common sense reasoning.Let's use the following steps to solve the problem.
[Steps]
1. **Plan a Solution**: Develop a simple step-by-step plan.
2. **Solve the problem**:  Follow the order of your plan and answer 'yes' or 'no'.
Please show the reasoning process and the answer.
"""

prompt_jx_702 ="""\
You are an expert in common sense reasoning.Let's use the following steps to solve the problem concisely.
[Steps]
1. **Plan a Solution**: Develop a step-by-step plan.
2. **Solve the problem**:  Follow the order of your plan and answer 'yes' or 'no'.
Please show the reasoning process and the answer.
"""
prompt_jx_trigger_1 = """\
You are an expert in arithmetic reasoning.Let's use the following four steps to solve the math problem.
[Steps]
1. **Identify Variables**: Extract the correct relevant variables and their corresponding values from the problem.
2. **Plan a Solution**: Develop a step-by-step plan to solve the problem.
3. **Calculate**:  Calculate correctly.
Please show the reasoning process and the answer.
"""
prompt_jx_trigger_2 = """\
You are an expert in arithmetic reasoning.Let's use the following four steps to solve the math problem.
[Steps]
1. **Identify Variables**: Extract the correct relevant variables and their corresponding values from the problem.
2. **Plan a Solution**: Develop a step-by-step plan to solve the problem. 
3. **Calculate**:  Strictly follow the order of operations in your calculations  and calculate correctly.
Please show the reasoning process and the answer.
"""
prompt_jx_trigger_3 ="""\
You are an expert in arithmetic reasoning.Let's use the following four steps to solve the math problem.
[Steps]
1. **Identify Variables**: Extract the correct relevant variables and their corresponding values from the problem.
2. **Plan a Solution**: Develop a step-by-step plan to solve the problem. 
3. **Apply Formulas**: For each step in your plan, apply the appropriate mathematical formulas or principles. This might include algebraic equations, geometric formulas, arithmetic operations, etc.
4. **Calculate**:  Strictly follow the order of operations in your calculations  and calculate correctly.
Please show the reasoning process and the answer.
"""
prompt_jx_trigger_4 ="""\
Let's think step by step.
"""


def get_prompt(prompt_id,type):
    if type == 0:
        try:
            demos = None
            return demos, eval('prompt_{}'.format(prompt_id))
            # return demos, eval('prompt_jx_{}'.format(prompt_id))
        except NameError as e:
            raise NameError('can\'t find prompt_id: {}'.format(prompt_id))
    elif type == 1:
        try:
            demos = None
            # return demos, eval('prompt_{}'.format(args.prompt_id))
            return demos, eval('prompt_jx_{}'.format(prompt_id))
        except NameError as e:
            raise NameError('can\'t find prompt_id: {}'.format(prompt_id))
    else:
        try:
            demos = None
            return demos, eval('prompt_jx_trigger_{}'.format(prompt_id))
        except NameError as e:
            raise NameError('can\'t find prompt_id: {}'.format(prompt_id))
    


def construct_input(prompt, text):
    # inputs = 'Q:' + text + "\nA: " + prompt
    inputs = prompt + 'Q:' + text + "\nA: " 
    return inputs
