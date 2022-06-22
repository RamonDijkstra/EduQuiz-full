from transformers import GPT2Tokenizer
import json
import os
GPT2tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Get current path
cur_path = os.path.abspath(os.getcwd())

# Paths
path_1 = '/processed_data/gpt3/completion_1/processed_train.json'
path_2 = '/processed_data/gpt3/completion_2/processed_train.json'
path_3 = '/processed_data/gpt3/completion_3/processed_train.json'
path_4 = '/processed_data/gpt3/completion_4/processed_train.json'
path_5 = '/processed_data/gpt3/completion_5/processed_train.json'
path_6 = '/processed_data/gpt3/completion_6/processed_train.json'

# Counters
count_tokens_1 = 0
count_tokens_2 = 0
count_tokens_3 = 0
count_tokens_4 = 0
count_tokens_5 = 0
count_tokens_6 = 0

# Data lists
train_data_1 = []
train_data_2 = []
train_data_3 = []
train_data_4 = []
train_data_5 = []
train_data_6 = []

# Fill the data lists
with open(cur_path + path_1) as f:
    for dictionary in f:
        train_data_1.append(json.loads(dictionary))

with open(cur_path + path_2) as f:
    for dictionary in f:
        train_data_2.append(json.loads(dictionary))

with open(cur_path + path_3) as f:
    for dictionary in f:
        train_data_3.append(json.loads(dictionary))

with open(cur_path + path_4) as f:
    for dictionary in f:
        train_data_4.append(json.loads(dictionary))

with open(cur_path + path_5) as f:
    for dictionary in f:
        train_data_5.append(json.loads(dictionary))

with open(cur_path + path_6) as f:
    for dictionary in f:
        train_data_6.append(json.loads(dictionary))

# Count
for data_instance in train_data_1:
    count_tokens_1 += len(GPT2tokenizer(data_instance['prompt'])['input_ids'])
    count_tokens_1 += len(GPT2tokenizer(data_instance['completion'])['input_ids'])
    
for data_instance in train_data_2:
    count_tokens_2 += len(GPT2tokenizer(data_instance['prompt'])['input_ids'])
    count_tokens_2 += len(GPT2tokenizer(data_instance['completion'])['input_ids'])

for data_instance in train_data_3:
    count_tokens_3 += len(GPT2tokenizer(data_instance['prompt'])['input_ids'])
    count_tokens_3 += len(GPT2tokenizer(data_instance['completion'])['input_ids'])

for data_instance in train_data_4:
    count_tokens_4 += len(GPT2tokenizer(data_instance['prompt'])['input_ids'])
    count_tokens_4 += len(GPT2tokenizer(data_instance['completion'])['input_ids'])

for data_instance in train_data_5:
    count_tokens_5 += len(GPT2tokenizer(data_instance['prompt'])['input_ids'])
    count_tokens_5 += len(GPT2tokenizer(data_instance['completion'])['input_ids'])

for data_instance in train_data_6:
    count_tokens_6 += len(GPT2tokenizer(data_instance['prompt'])['input_ids'])
    count_tokens_6 += len(GPT2tokenizer(data_instance['completion'])['input_ids'])

# Epochs
epochs = 4

# Print
with open('gpt3_costs/gpt3_fine_tune_cost.txt', 'w') as f:
    print('Total tokens completion 1:', count_tokens_1 * epochs)
    print('Finetune cost completion 1', '$', round(count_tokens_1 * epochs / 1000 * 0.003, 2))
    print('Total tokens completion 2:', count_tokens_2 * epochs)
    print('Finetune cost completion 2', '$', round(count_tokens_2 * epochs / 1000 * 0.003, 2))
    print('Total tokens completion 3:', count_tokens_3 * epochs)
    print('Finetune cost completion 3', '$', round(count_tokens_3 * epochs / 1000 * 0.003, 2))
    print('Total tokens completion 4:', count_tokens_4 * epochs)
    print('Finetune cost completion 4', '$', round(count_tokens_4 * epochs / 1000 * 0.003, 2))
    print('Total tokens completion 5:', count_tokens_5 * epochs)
    print('Finetune cost completion 5', '$', round(count_tokens_5 * epochs / 1000 * 0.003, 2))
    print('Total tokens completion 6:', count_tokens_6 * epochs)
    print('Finetune cost completion 6', '$', round(count_tokens_6 * epochs / 1000 * 0.003, 2))

    f.write('Total tokens completion 1: ' + str(count_tokens_1 * epochs) + '\n')
    f.write('Finetune cost completion 1: ' + '$' + str(round(count_tokens_1 * epochs / 1000 * 0.003, 2)) + '\n\n')
    f.write('Total tokens completion 2: ' + str(count_tokens_2 * epochs) + '\n')
    f.write('Finetune cost completion 2: ' + '$' + str(round(count_tokens_2 * epochs / 1000 * 0.003, 2)) + '\n\n')
    f.write('Total tokens completion 3: ' + str(count_tokens_3 * epochs) + '\n')
    f.write('Finetune cost completion 3: ' + '$' + str(round(count_tokens_3 * epochs / 1000 * 0.003, 2)) + '\n\n')
    f.write('Total tokens completion 4: ' + str(count_tokens_4 * epochs) + '\n')
    f.write('Finetune cost completion 4: ' + '$' + str(round(count_tokens_4 * epochs / 1000 * 0.003, 2)) + '\n\n')
    f.write('Total tokens completion 5: ' + str(count_tokens_5 * epochs) + '\n')
    f.write('Finetune cost completion 5: ' + '$' + str(round(count_tokens_5 * epochs / 1000 * 0.003, 2)) + '\n\n')
    f.write('Total tokens completion 6: ' + str(count_tokens_6 * epochs) + '\n')
    f.write('Finetune cost completion 6: ' + '$' + str(round(count_tokens_6 * epochs / 1000 * 0.003, 2)) + '\n\n')