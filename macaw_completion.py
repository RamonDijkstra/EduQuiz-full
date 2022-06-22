from utils import load_model, run_macaw
from tqdm import tqdm
import json
import os

print('First do GPT-3 completions')

model_dict = load_model("allenai/macaw-11b")

path = "generated_data_gpt3/experiment_4/input_macaw.json"

test_data = []

for line in open(path):
    test_data.append((json.loads(line)))

generated = {}

for i in tqdm(range(len(test_data))):
    res = run_macaw(test_data[i]['prompt'], model_dict)
    output_raw_list = res['output_raw_list']    
    generated[i+1] = output_raw_list

if not os.path.exists("output"):
    os.mkdir("output")

with open("generated_data_gpt3/experiment_4/generated_answers_macaw.json", 'w') as f:
    json.dump(generated, f)

print("Experiment 1 done")

path = "generated_data_gpt3/experiment_5/input_macaw.json"

test_data = []

for line in open(path):
    test_data.append((json.loads(line)))

generated = {}

for i in tqdm(range(len(test_data))):
    res = run_macaw(test_data[i]['prompt'], model_dict)
    output_raw_list = res['output_raw_list']    
    generated[i+1] = output_raw_list

with open("generated_data_gpt3/experiment_5/generated_answers_macaw.json", 'w') as f:
    json.dump(generated, f)

print("Experiment 2 done")

path = "generated_data_gpt3/experiment_6/input_macaw.json"

test_data = []

for line in open(path):
    test_data.append((json.loads(line)))

generated = {}

for i in tqdm(range(len(test_data))):
    res = run_macaw(test_data[i]['prompt'], model_dict)
    output_raw_list = res['output_raw_list']    
    generated[i+1] = output_raw_list

with open("generated_data_gpt3/experiment_6/generated_answers_macaw.json", 'w') as f:
    json.dump(generated, f)

print("Experiment 3 done")

print("Start Macaw models")

path = "processed_data/macaw/completion_1/processed_test.json"

test_data = []

for line in open(path):
    test_data.append((json.loads(line)))

generated = {}

for i in tqdm(range(len(test_data))):
    res = run_macaw(test_data[i]['prompt'], model_dict)
    output_raw_list = res['output_raw_list']    
    generated[i+1] = output_raw_list

with open("generated_data_macaw/experiment_1/generated.json", 'w') as f:
    json.dump(generated, f)

print("Experiment 4 done")

path = "processed_data/macaw/completion_2/processed_test.json"

test_data = []

for line in open(path):
    test_data.append((json.loads(line)))

generated = {}

for i in tqdm(range(len(test_data))):
    res = run_macaw(test_data[i]['prompt'], model_dict)
    output_raw_list = res['output_raw_list']    
    generated[i+1] = output_raw_list

with open("generated_data_macaw/experiment_2/generated.json", 'w') as f:
    json.dump(generated, f)

print("Experiment 5 done")

path = "processed_data/macaw/completion_3/processed_test.json"

test_data = []

for line in open(path):
    test_data.append((json.loads(line)))

generated = {}

for i in tqdm(range(len(test_data))):
    res = run_macaw(test_data[i]['prompt'], model_dict)
    output_raw_list = res['output_raw_list']    
    generated[i+1] = output_raw_list

with open("generated_data_macaw/experiment_3/generated.json", 'w') as f:
    json.dump(generated, f)

print("Experiment 6 done")

# DISTRACTORS

path = "processed_data/macaw/completion_4/processed_test.json"

test_data = []

for line in open(path):
    test_data.append((json.loads(line)))

generated = {}

for i in tqdm(range(len(test_data))):
    res = run_macaw(test_data[i]['prompt'], model_dict)
    output_raw_list = res['output_raw_list']    
    generated[i+1] = output_raw_list

with open("generated_data_macaw/experiment_4/generated_distractors.json", 'w') as f:
    json.dump(generated, f)

print("Experiment 7 done")

mc_options = []

for key in generated:
    mc = generated[key][0].split("= ")[1]
    mc_options.append(mc)

generated = {}

for i in tqdm(range(len(test_data))):
    prompt = test_data[i]['prompt']
    temp = prompt.split("$mcoptions$ ; ")[1]
    question = temp.split(" $answer$")[0]
    context = temp.split("$context$ = ")[1]
    new_prompt = "$answer$ ; " + question + " $mcoptions$ = " + mc_options[i] + " $context$ = " + context
    
    res = run_macaw(new_prompt, model_dict)
    output_raw_list = res['output_raw_list']    
    generated[i+1] = output_raw_list

with open("generated_data_macaw/experiment_4/generated_answers.json", 'w') as f:
    json.dump(generated, f)

print("Experiment 8 done")    

# STEPWISE QUIZ

path = "processed_data/macaw/completion_5/processed_test.json"

test_data = []

for line in open(path):
    test_data.append((json.loads(line)))

generated = {}

for i in tqdm(range(len(test_data))):
    res = run_macaw(test_data[i]['prompt'], model_dict)
    output_raw_list = res['output_raw_list']    
    generated[i+1] = output_raw_list

with open("generated_data_macaw/experiment_5/generated_questions.json", 'w') as f:
    json.dump(generated, f)

print("Experiment 9 done")

questions = []

for key in generated:
    q = generated[key][0].split("= ")[1].split(". ")[-1]
    questions.append(q)

generated = {}

for i in tqdm(range(len(test_data))):
    prompt = test_data[i]['prompt']
    context = prompt.split("$question$ ;")[1]
    new_prompt = "$answer$ ; " + "$question$ = " + questions[i] + context
    res = run_macaw(new_prompt, model_dict)
    output_raw_list = res['output_raw_list']    
    generated[i+1] = output_raw_list

with open("generated_data_macaw/experiment_5/generated_answers.json", 'w') as f:
    json.dump(generated, f)

print("Experiment 10 done")

answers = []
for key in generated:
    a = generated[key][0].split("= ")[1].split(". ")[-1]
    answers.append(a)

generated = {}

for i in tqdm(range(len(test_data))):
    prompt = test_data[i]['prompt']
    context = prompt.split("$question$ ;")[1]
    new_prompt = "$mcoptions$ ; " + "$question$ = " + questions[i] + " $answer$= " + answers[i] + context
    res = run_macaw(new_prompt, model_dict)
    output_raw_list = res['output_raw_list']    
    generated[i+1] = output_raw_list

with open("generated_data_macaw/experiment_5/generated_distractors.json", 'w') as f:
    json.dump(generated, f)

print("Experiment 11 done")

mc_options = []

for key in generated:
    mc = generated[key][0].split("= ")[1]
    mc_options.append(mc)

generated = {}

for i in tqdm(range(len(test_data))):
    prompt = test_data[i]['prompt']
    context = prompt.split("$question$ ;")[1]
    new_prompt = "$question$ ; " + "$answer$ = " + answers[i] + context
    res = run_macaw(new_prompt, model_dict)
    output_raw_list = res['output_raw_list']    
    generated[i+1] = output_raw_list

with open("generated_data_macaw/experiment_5/generated_questions_2.json", 'w') as f:
    json.dump(generated, f)

print("Experiment 12 done")

generated = {}

for i in tqdm(range(len(test_data))):
    prompt = test_data[i]['prompt']
    context = prompt.split("$question$ ;")[1]
    new_prompt = "$answer$ ; " + "$question$ = " + questions[i] + " $mcoptions$ = " + mc_options[i] + context
    res = run_macaw(new_prompt, model_dict)
    output_raw_list = res['output_raw_list']    
    generated[i+1] = output_raw_list

with open("generated_data_macaw/experiment_5/generated_quiz_answers.json", 'w') as f:
    json.dump(generated, f)

print("Experiment 13 done")

# FULL QUIZ GENERATION

path = "processed_data/macaw/completion_6/processed_test.json"

test_data = []

for line in open(path):
    test_data.append((json.loads(line)))

generated = {}

for i in tqdm(range(len(test_data))):
    res = run_macaw(test_data[i]['prompt'], model_dict)
    output_raw_list = res['output_raw_list']    
    generated[i+1] = output_raw_list

with open("generated_data_macaw/experiment_6/generated_quiz.json", 'w') as f:
    json.dump(generated, f)

print("Experiment 14 done")