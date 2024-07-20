import json
import re

def preprocess(json_data):
    # Parse JSON data
    data = json.loads(json_data)
    
    
    output = []
    
    # Iterate through list in data
    for item in data:
        # Check if 'annotations' exists in current item
        if 'annotations' in item:
            annotations = item['annotations']
            
            # Iterate through each annotation in the item
            for annotation in annotations:
                if 'result' in annotation:
                    for result in annotation['result']:
                        if 'value' in result and 'text' in result['value']:
                            text = result['value']['text']
                            label = result['value']['hypertextlabels'][0]
                            label = label.replace(' ', '').upper()
                            # Split text into words
                            words = re.findall(r'\S+|\s+', text)
                            
                            # Create label for each word where the first word in label is given 'I'
                            # and the following words are given 'B' indicators
                            for i, word in enumerate(words):
                                if word.strip():  # Ignore empty strings
                                    if i == 0:
                                        output.append(f"{word} B-{label}")
                                    else:
                                        output.append(f"{word} I-{label}")
    
    return '\n'.join(output)

with open('vvarma42@gatech.edu.json', 'r') as file:
    json_data = file.read()

result = preprocess(json_data)

with open('output.txt', 'w') as file:
    file.write(result)

print("Finshed preprocessing. Output in output.txt")