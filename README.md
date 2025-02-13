<h1>📝 Abstractive Text Summarization</h1>

<h2>🚀 Introduction</h2>
<p>This project focuses on generating human-like text summaries using **Natural Language Processing (NLP)** and **Deep Learning**. Unlike extractive summarization, which picks key sentences, **abstractive summarization** understands and rewrites the text in a more concise and coherent manner.</p>

<p>We fine-tuned **Google's PEGASUS model**, an advanced Transformer-based model designed specifically for text summarization tasks.</p>

<p>📄 For more details, refer to the <a href="(https://github.com/aryansharma7341/Abstractive-Text-Summarization/blob/main/Documentation/Documentation_Minor_Project_II_08.pdf)">Documentation</a>.</p>

<hr>

<h2>📂 Directory Structure</h2>
<p>The project is structured as follows:</p>

<pre>
Abstractive_Text_Summarization
│
├── data_preprocessing
│   ├── text_cleaning.py
│   ├── tokenization.py
│   └── dataset_preparation.py
│
├── model_training
│   ├── train_pegasus.py
│   ├── loss_optimization.py
│   ├── evaluation.py
│   └── fine_tuning.py
│
├── web_application
│   ├── app.py
│   ├── templates/
│   ├── static/
│   └── api.py
│
└── documentation
    ├── research_paper_summaries.md
    ├── model_comparisons.md
    └── performance_analysis.md
</pre>

<ul>
  <li><strong>Data Preprocessing</strong>: Prepares raw text data by removing noise, tokenizing, and formatting it for training.</li>
  <li><strong>Model Training</strong>: Fine-tunes the **PEGASUS** model using a dataset of text-summary pairs.</li>
  <li><strong>Web Application</strong>: A Flask-based UI where users can input text and receive AI-generated summaries.</li>
  <li><strong>Documentation</strong>: Detailed reports on model architecture, comparisons, and performance analysis.</li>
</ul>

<hr>

<h2>🏗️ System Architecture</h2>
<p align="center">
  <img src="https://your-image-link-here.com/system-architecture.png" alt="System Architecture" width="75%"/>
</p>

<hr>

<h2>🎬 Demo</h2>
<p>🔗 <strong>Watch the full demo here:</strong> <a href="https://www.youtube.com/watch?v=your-video-link">YouTube Video</a></p>

<p align="center">
  <img src="https://your-image-link-here.com/demo.gif" alt="Abstractive Text Summarization Demo" width="75%"/>
</p>

<hr>

<h2>📊 Model Performance</h2>

<table>
  <tr>
    <th>Model</th>
    <th>Dataset</th>
    <th>ROUGE Score</th>
    <th>Training Time</th>
  </tr>
  <tr>
    <td>PEGASUS</td>
    <td>XSum</td>
    <td><strong>45.67</strong></td>
    <td>10 hours</td>
  </tr>
  <tr>
    <td>BART</td>
    <td>CNN/DailyMail</td>
    <td>42.89</td>
    <td>12 hours</td>
  </tr>
  <tr>
    <td>T5</td>
    <td>Newsroom</td>
    <td>40.12</td>
    <td>14 hours</td>
  </tr>
</table>

<p>Our **fine-tuned PEGASUS model** achieves a <strong>ROUGE Score of 45.67</strong>, making it an excellent choice for abstractive text summarization.</p>

<hr>

<h2>⚡ Installation & Setup</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Python 3.8+</li>
  <li>PyTorch</li>
  <li>Hugging Face Transformers</li>
  <li>Flask</li>
  <li>NumPy & Pandas</li>
</ul>

<h3>Steps</h3>

<pre>
# Clone the repository
git clone https://github.com/aryansharma7341/Abstractive-Text-Summarization.git
cd Abstractive-Text-Summarization

# Install required dependencies
pip install -r requirements.txt

# Run the Flask application
cd web_application
python app.py
</pre>


<hr>

<h2>🏆 Contributors</h2>
<p>👤 <strong>Aryan Sharma</strong><br>
📧 <a href="aryansharma7341.as@gmail.com">Email</a><br>
🔗 <a href="https://github.com/aryansharma7341">GitHub</a><br>
🔗 <a href="www.linkedin.com/in/aryansharma7341">LinkedIn</a></p>


<p>🌟 <strong>If you find this project useful, don't forget to ⭐ the repository!</strong></p>
