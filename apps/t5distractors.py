from transformers import T5ForConditionalGeneration, T5Tokenizer
import os


base_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of `t5distractors.py`
trained_tokenizer_path = os.path.join(base_dir, "race_distractors", "tokenizer")
trained_model_path = os.path.join(base_dir,"race_distractors", "model")


# # Local paths to the trained model and tokenizer
# trained_model_path = "race_distractors/model"
# trained_tokenizer_path = "race_distractors/tokenizer"

# Load the tokenizer and model from local paths
dis_tokenizer = T5Tokenizer.from_pretrained(trained_tokenizer_path,legacy=True)
dis_model = T5ForConditionalGeneration.from_pretrained(trained_model_path)

def get_distractors_t5(question, answer, context,tokenizer,model):
    """
    Generate distractors using the T5 model.
    """
    # Prepare the input text with question, answer, and context
    input_text = " ".join([question, tokenizer.sep_token, answer, tokenizer.sep_token, context])

    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt")

    # Generate the output from the model
    outputs = model.generate(**inputs, max_new_tokens=128, num_beams=5)

    # Decode and format the generated distractors
    distractors = tokenizer.decode(outputs[0], skip_special_tokens=False)
    distractors = distractors.replace(tokenizer.pad_token, "").replace(tokenizer.eos_token, "")
    distractors = [y.strip() for y in distractors.split(tokenizer.sep_token)]

    # Return the list of distractors
    return distractors

context = r"""
Mesophiles grow best in moderate temperature, typically between 25°C and 40°C (77°F and 104°F).
Mesophiles are often found living in or on the bodies of humans or other animals.
The optimal growth temperature of many pathogenic mesophiles is 37°C (98°F), the normal human body temperature.
 Mesophilic organisms have important uses in food preparation, including cheese, yogurt, beer and wine.""".replace("\n", "")
question = "What type of organism is commonly used in preparation of foods such as cheese and yogurt?"
answer = "mesophilic organisms"

# Generate distractors using the T5 model
if __name__ == "__main__":
    distractors = get_distractors_t5(question, answer, context,dis_tokenizer,dis_model)
    print("Distractors:", distractors)
    print(type(distractors))
