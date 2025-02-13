from flask import Flask, redirect, render_template,url_for
from flask import request
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("./data_tokenizer")
model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-cnn_dailymail")

app=Flask(__name__)


@app.route("/",methods=['POST', 'GET'])
def value():
    return render_template('welcome.html')


@app.route("/getstarted", methods=['POST', 'GET'])
def page():
    text = None
    if request.method == 'POST':
        input_vlu = request.form.get('inp_text')  # Use request.form.get() to safely retrieve form data 
        inputs = tokenizer(input_vlu, return_tensors="pt")
        generated_summary = model.generate(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'], length_penalty=0.8, num_beams=8, max_length=200)
        decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True, clean_up_tokenization_spaces=True) for s in generated_summary]
        print("Generated Summary:", decoded_summaries)
        
        return render_template('output.html', result=decoded_summaries,vlu=1)
    return render_template('text.html',vlu=0)


if __name__ == "__main__":
    app.run(debug=True)



