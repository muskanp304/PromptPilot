# AI Assistant - Complete Documentation

## 📋 Project Overview

This is a **production-ready AI Assistant** built with Python and OpenAI's API. It demonstrates prompt engineering principles with multiple functions, different prompt styles, user feedback mechanisms, and statistical analysis.

### ✨ Key Features

- **4 Core Functions:**
  - ❓ Answer Questions (3 styles: simple, detailed, professional)
  - 📝 Summarize Text (3 styles: bullet, abstract, simplified)
  - ✨ Generate Creative Content (3 styles: story, poetry, ideas)
  - 💡 Provide Advice (3 styles: practical, expert, motivational)

- **Prompt Engineering Excellence:**
  - 12 carefully designed prompts (3 per function)
  - Varying length, specificity, tone, and complexity
  - Production-quality prompt templates

- **Feedback System:**
  - Rate responses (1-5 stars)
  - Mark as helpful/unhelpful
  - Add comments and suggestions
  - Automatic statistics and analysis

- **User-Friendly Interface:**
  - Intuitive command-line menu
  - Clear formatting and instructions
  - Real-time feedback collection
  - Performance statistics dashboard

---

## 🚀 Quick Start (5 minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Get Your API Key

This project supports both OpenAI and Google Gemini providers.

#### OpenAI
1. Go to https://platform.openai.com/account/api-keys
2. Create a new API key
3. Copy the key (starts with `sk-`)

#### Gemini / Google Cloud
1. Create a Google Cloud project
2. Enable the Generative Language API (`generativelanguage.googleapis.com`)
3. Create a valid API key or OAuth credential for that project
4. Copy the key or token

### Step 3: Create .env File
In the `AI Assistant` folder, create a file named `.env`.

#### Use OpenAI:
```
OPENAI_API_KEY=sk-your_actual_key_here
AI_PROVIDER=openai
```

#### Use Gemini:
```
GEMINI_API_KEY=your_gemini_key_here
AI_PROVIDER=gemini
```

**If you put a Gemini auth token in `OPENAI_API_KEY`, also set:**
```
AI_PROVIDER=gemini
```

**Or copy from example:**
```bash
cp .env.example .env
# Then edit .env and replace with your actual API key
```

### Step 4: Run the Application
```bash
python main.py
```

---

## 📖 Project Structure

```
AI Assistant/
├── main.py                      # Main application entry point
├── assistant.py                 # Core AI Assistant (OpenAI integration)
├── prompts.py                   # Prompt templates (12 total)
├── feedback.py                  # Feedback collection & analysis
├── requirements.txt             # Python dependencies
├── .env.example                 # Template for configuration
├── .env                         # Your API key (create this)
├── feedback_data.json           # Automatically created feedback storage
├── README.md                    # This file
├── setup_guide.md               # Detailed setup instructions
└── __init__.py                  # Python package marker
```

---

## 🎯 How to Use

### Running the Application
```bash
python main.py
```

You'll see the main menu:
```
============================================================
  🤖 AI ASSISTANT MAIN MENU
============================================================

1. ❓ Answer Questions       - Ask factual questions
2. 📝 Summarize Text         - Summarize articles or documents
3. ✨ Generate Creative      - Stories, poems, ideas
4. 💡 Get Advice             - Tips and suggestions
5. 📊 View Feedback Stats    - See response quality stats
6. ℹ️  Help & Instructions    - Learn how to use
7. 🚪 Exit                   - Quit the application
```

### Example Workflows

#### Example 1: Answer a Question
```
1. Select "1. Answer Questions"
2. Choose a prompt style (e.g., "Detailed & Educational")
3. Enter your question: "What is machine learning?"
4. Get AI response
5. Optionally provide feedback (helpful? rating?)
```

#### Example 2: Summarize an Article
```
1. Select "2. Summarize Text"
2. Choose a style (e.g., "Bullet Point Summary")
3. Paste article text (type END when done)
4. Get concise summary
5. Rate the summary
```

#### Example 3: Generate Creative Content
```
1. Select "3. Generate Creative Content"
2. Choose: Story, Poetry, or Brainstorm Ideas
3. Provide topic
4. Get creative output
5. Share feedback for improvement
```

#### Example 4: Get Advice
```
1. Select "4. Get Advice"
2. Choose advice style
3. Enter topic
4. Get practical tips
5. Rate helpfulness
```

---

## 📊 Feedback & Statistics

### Collecting Feedback
After each AI response, you're asked:
```
📝 Provide feedback? (yes/no): yes
✓ Was this response helpful? (yes/no): yes
✓ Rate the response (1-5 stars): 5
✓ Any comments or suggestions?: Great answer, very clear!
```

### Viewing Statistics
Select option "5. View Feedback Stats" to see:
- Total responses collected
- Percentage marked as helpful
- Average rating across all responses
- Performance breakdown by function
- Per-function usage statistics

Example output:
```
============================================================
FEEDBACK STATISTICS
============================================================

Overall Performance:
  • Total Responses Rated: 8
  • Helpful Responses: 7 (87.5%)
  • Average Rating: 4.5/5.0 ⭐

By Function:
  • QUESTIONS:
    - Uses: 3
    - Rating: 4.67/5.0
    - Helpful: 100%
  • SUMMARIZE:
    - Uses: 3
    - Rating: 4.33/5.0
    - Helpful: 80%
  • ADVICE:
    - Uses: 2
    - Rating: 4.0/5.0
    - Helpful: 100%
```

---

## 🎓 Prompt Engineering Insights

### Why Multiple Styles?

Each function has 3 different prompts demonstrating key engineering principles:

#### Answer Questions
1. **Simple & Direct** - Minimal context, fast answers (temp=0.3)
2. **Detailed & Educational** - Educational framing, more thorough (temp=0.3)
3. **Professional & Technical** - Expert-level, sources cited (temp=0.3)

#### Summarize Text
1. **Bullet Points** - Key facts in list format
2. **Abstract** - Academic-style 150-200 word summary
3. **Simplified** - Easy language for beginners

#### Creative Content
1. **Stories** - Complete narrative with twist (temp=0.9)
2. **Poetry** - Verse with vivid imagery (temp=0.9)
3. **Brainstorm** - Multiple unique concepts (temp=0.9)

#### Advice
1. **Practical** - Numbered, actionable steps
2. **Expert Perspective** - Industry best practices
3. **Motivational** - Encouraging, inspiring tone

### Temperature Settings

Different functions use different temperature values:
- **Low (0.3)** - Questions: more precise, consistent
- **Medium (0.5)** - Summarization: balanced
- **Medium-High (0.7)** - Advice: some variation
- **High (0.9)** - Creative: more diverse, novel outputs

---

## 🔧 Troubleshooting

### "ModuleNotFoundError: No module named 'openai'"
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### "OPENAI_API_KEY not found"
**Solution:** Create `.env` file in the project folder
```
OPENAI_API_KEY=sk-your_key_here
```

### "Invalid API Key"
**Solution:** 
- Check your key starts with `sk-`
- Ensure no extra spaces in `.env` file
- Verify key is still active on OpenAI dashboard

### "Rate limit exceeded"
**Solution:** Wait a few moments before the next request (API has rate limits)

### "Connection timeout"
**Solution:** Check your internet connection

---

## 📈 Extending the Project

### Add New Functions
1. Add prompt templates to `prompts.py`
2. Add corresponding method to `assistant.py`
3. Add menu option in `main.py`

### Add More Prompt Styles
Edit `prompts.py` and add to appropriate dictionary:
```python
"new_style": {
    "name": "Display Name",
    "template": "Your prompt template here..."
}
```

### Customize Temperature Values
Edit `assistant.py` methods to adjust creativity level:
```python
# More deterministic (0.0-0.5)
response = self.get_response(prompt, temperature=0.3)

# More creative (0.7-1.0+)
response = self.get_response(prompt, temperature=0.9)
```

### Change AI Model
Edit `assistant.py`:
```python
self.model = "gpt-4"  # Use GPT-4 instead of GPT-3.5
```

---

## 📝 Requirements for Project Submission

✅ **Functionality** - 4 distinct functions implemented
✅ **Prompt Design** - 12 prompts (3 per function) with varying:
  - Length and specificity
  - Tone and style
  - Complexity and context

✅ **User Interaction** - Command-line interface with:
  - Clear menu system
  - Multiple function selection
  - Formatted responses

✅ **Feedback Loop** - Complete feedback system:
  - Helpful/unhelpful ratings
  - 1-5 star ratings
  - Comment collection
  - Statistics dashboard

✅ **Documentation** - Comprehensive docs:
  - README (this file)
  - Setup guide
  - Inline code comments
  - Help menu in-app

---

## 🎯 Next Steps

1. **Install & Run:**
   ```bash
   pip install -r requirements.txt
   # Create .env with your API key
   python main.py
   ```

2. **Try Each Function:**
   - Test all 4 functions
   - Experiment with different styles
   - Provide feedback on responses

3. **Review Feedback Stats:**
   - See which prompts work best
   - Identify patterns in responses
   - Note user preferences

4. **Collect Data:**
   - Rate multiple responses
   - Use for prompt optimization
   - Build performance baselines

5. **Create PPT Presentation:**
   - Showcase different functions
   - Show feedback statistics
   - Demonstrate prompt effectiveness
   - Share insights about prompt engineering

---

## 📞 Support

For issues:
1. Check `setup_guide.md`
2. Review error messages carefully
3. Verify `.env` file configuration
4. Check API key validity on OpenAI dashboard

---

## 📄 License

Educational project for internship. Built with Python 3.8+ and OpenAI API.

**Created:** 2024
**Status:** Production-ready ✅
