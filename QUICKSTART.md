# CodeChat: Quick Start Guide

Get CodeChat running in **5 minutes**! 🚀

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- ~2GB free disk space

## Installation & Run (5 Minutes)

### Option 1: Linux/macOS Terminal

```bash
# 1. Clone repository
git clone https://github.com/Sai-Bhargava-S/CodeChat.git
cd CodeChat

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py

# 5. Open in browser
# → http://localhost:7860
```

### Option 2: Windows Command Prompt

```cmd
# 1. Clone repository
git clone https://github.com/Sai-Bhargava-S/CodeChat.git
cd CodeChat

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py

# 5. Open in browser
# → http://localhost:7860
```

### Option 3: Docker (One Command)

```bash
docker build -t codechat:1.0 .
docker run -p 7860:7860 codechat:1.0

# Open browser at http://localhost:7860
```

---

## First Steps

### 1. Start a Conversation
```
You: "What's a function?"
CodeChat: "Great question! A function is... [explanation] ✨ [fun fact]"
```

### 2. Ask About Debugging
```
You: "My loop isn't working"
CodeChat: "Let's debug! Can you share the code? [helpful guidance]"
```

### 3. Learn New Concepts
```
You: "Explain Python lists"
CodeChat: "Lists are like containers... [simple explanation] [next topic suggestion]"
```

### 4. Clear and Start Over
```
Click: "Clear Conversation 🗑️" button
CodeChat: Resets history, ready for new topic
```

---

## Troubleshooting

### Issue: "Port 7860 already in use"
```bash
# Change port in app.py (line ~350):
interface.launch(server_port=7861)

# Then run:
python app.py
```

### Issue: "ModuleNotFoundError: No module named 'gradio'"
```bash
# Reinstall dependencies:
pip install --force-reinstall -r requirements.txt
```

### Issue: Slow responses
- App uses fallback mode (check console output)
- This is normal and expected
- Responses still work great!

### Issue: Can't connect to localhost:7860
- Make sure Python is still running
- Try a different browser
- Check your firewall settings

---

## Project Structure

```
CodeChat/
├── app.py                    ← Main application (run this!)
├── requirements.txt          ← Dependencies
├── README.md                 ← Full documentation
├── SDLC_DOCUMENTATION.md     ← Development details
├── CHANGELOG.md              ← Version history
├── LICENSE                   ← MIT License
└── QUICKSTART.md             ← This file!
```

---

## What's Inside

### Core Features ✨
- 💬 **Multi-turn Conversations** - Chat remembers context
- 🎓 **Beginner-Friendly** - Simple, fun explanations
- 😄 **Fun Facts** - 25+ emoji-enhanced facts
- 🐛 **Debugging Help** - Supportive error guidance
- 🌐 **Web Interface** - Works in any browser

### Technology Stack 🛠️
- **AI:** CodeLlama via LangChain
- **Frontend:** Gradio (no HTML/CSS needed!)
- **Language:** Python 3.9+
- **Models:** Llama2 7B (free from HuggingFace)

---

## Usage Examples

### Example 1: Learning Functions
```
User: What's a function and why do I need it?

CodeChat: Great question about function! 🎯

A function is a reusable block of code that does a specific job.
Think of it like a recipe - you write it once, then use it 
whenever you need it!

Instead of writing the same code 10 times, you write it once 
in a function and call it 10 times.

✨ Did you know? Python has thousands of built-in functions 
you can use right away!
```

### Example 2: Debugging Code
```
User: My code keeps throwing an error

CodeChat: Let's debug this together! 🐛

Could you share:
1. The exact error message?
2. The code that's causing it?
3. What you expected to happen?

Once I see these, we can figure it out step-by-step!

✨ Did you know? The term 'bug' came from a real moth stuck 
in a computer in 1947!
```

### Example 3: Learning Loops
```
User: How do loops work?

CodeChat: Loops are one of the most useful tools in programming! 🔄

Think of a loop like a recipe instruction: "Repeat these steps 
5 times" - that's exactly what loops do in code!

Example:
for i in range(5):
    print("Hello!")  # Prints 5 times

✨ Did you know? Loops can save you from writing the same code 
hundreds of times!
```

---

## Next Steps

1. ✅ **Run the app** - Get it working locally
2. 📚 **Read README.md** - Understand all features
3. 🔍 **Read SDLC_DOCUMENTATION.md** - See how it was built
4. 🌐 **Deploy it** - Share with friends using Heroku/Docker
5. 📝 **Customize it** - Add more fun facts or features
6. 🎯 **Contribute** - Help improve the project!

---

## Common Questions

### Q: Does it require internet?
**A:** The simplified mode works offline. Full LLM mode needs HuggingFace API.

### Q: Is my data saved?
**A:** No, conversations are in-memory only. Refresh = new chat.

### Q: Can I use it on mobile?
**A:** Yes! Gradio interface works on phones/tablets.

### Q: Can I deploy it online?
**A:** Yes! See deployment options in README.md

### Q: How do I add more fun facts?
**A:** Edit the `FUN_FACTS` dictionary in app.py

---

## Performance Tips

1. **Use simplified mode first** - Fastest way to try it
2. **Keep messages concise** - Faster processing
3. **Clear history regularly** - Keeps memory fresh
4. **Use modern browsers** - Chrome/Firefox work best

---

## Support & Help

- 📖 **Documentation:** README.md
- 🐛 **Report Issues:** GitHub Issues
- 💬 **Ask Questions:** GitHub Discussions
- 📧 **Email:** saibhargavas2005@gmail.com

---

## What You Can Ask CodeChat

✅ **Concepts:** "What's OOP?", "Explain recursion"  
✅ **Debugging:** "Why doesn't my code work?"  
✅ **Learning:** "How do I learn Python faster?"  
✅ **Examples:** "Show me a loop example"  
✅ **Best Practices:** "How should I name variables?"  
✅ **Language Basics:** "What's a variable?"  

❌ **Limitations:** Very advanced algorithms, specialized libraries (these are okay but simplified)

---

## Developer Info

- **Author:** Sai Bhargava S
- **Email:** saibhargavas2005@gmail.com
- **Location:** Bengaluru, India
- **GitHub:** github.com/Sai-Bhargava-S

---

## License

CodeChat is open source under the **MIT License**.  
See LICENSE file for details.

---

## Version

**Current Version:** 1.0.0 ✅  
**Released:** April 2025  
**Status:** Production Ready

---

**Ready to start?**  
Run `python app.py` and open http://localhost:7860 in your browser! 🚀

Happy coding! 💻
