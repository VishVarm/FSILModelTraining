from tner import get_dataset, TransformersNER
data, label2id = get_dataset(local_dataset={
    "train": "output.txt",
    "valid": "valid.txt",
    "test": "test.txt"
})
print(label2id)

model = TransformersNER("tner/roberta-large-fin", label2id=label2id, crf=True)
output = model.predict(["example text here"])  # give a list of sentences (or tokenized sentence) 
print(output)

