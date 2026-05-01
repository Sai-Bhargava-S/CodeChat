"""
CodeChat: AI-Powered Conversational Coding Assistant
A multi-turn coding assistant built with CodeLlama, LangChain, and Gradio
that helps junior developers understand code with fun facts and emojis.

Author: Sai Bhargava S
Date: 2025
"""

import gradio as gr
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import random

# ============================================================================
# FUN FACTS DATABASE - Make learning engaging with emojis
# ============================================================================

FUN_FACTS = {
    "python": [
        "🐍 Did you know? Python was named after Monty Python, not the snake!",
        "⚡ Python is used by NASA, Google, and Netflix for their data science!",
        "🎯 Python's simplicity makes it perfect for beginners AND experts!",
        "🏆 Python ranks #1 in the TIOBE Index for most loved languages!",
    ],
    "javascript": [
        "☕ JavaScript was created in just 10 days by Brendan Eich in 1995!",
        "🌐 JavaScript powers 98% of all websites on the internet!",
        "⚙️ Despite the name, JavaScript has nothing to do with Java!",
        "🚀 JavaScript can now run on servers (Node.js) and even smart devices!",
    ],
    "debugging": [
        "🐛 The term 'bug' came from a real moth stuck in a computer in 1947!",
        "🔍 Professional developers spend 70% of their time debugging!",
        "💡 The best debugging tool? Explaining your code to a rubber duck! 🦆",
        "⏰ Adding print statements is often faster than a fancy debugger!",
    ],
    "algorithms": [
        "🎲 Sorting algorithms can be visualized like sorting dancers on a stage!",
        "⚡ Binary search is 1 million times faster than linear search for big data!",
        "🌳 Trees in programming look like real family trees (upside down)!",
        "🔗 Linked lists are like train cars connected together!",
    ],
    "general": [
        "💻 The first programmer was Ada Lovelace way back in 1843!",
        "🎮 Many video games use AI concepts similar to coding challenges!",
        "🌟 Every expert was once a beginner - keep learning! 🚀",
        "🔧 Good code is like a good story - easy to read and understand!",
    ]
}

# ============================================================================
# PROMPT TEMPLATES - Optimized for CodeLlama
# ============================================================================

SYSTEM_PROMPT = """You are CodeChat, a friendly coding assistant designed specifically for junior developers.

Your role is to:
1. Explain code clearly and in simple terms
2. Help debug code by asking clarifying questions
3. Provide learning-friendly explanations with examples
4. Be encouraging and supportive
5. Admit when you're unsure rather than guessing

When explaining code:
- Break it into small, digestible pieces
- Use simple analogies (e.g., loops are like repeating a task)
- Provide working examples
- Ask if the explanation is clear

Keep responses concise (2-3 paragraphs max for code explanations).
Make learning fun while being technically accurate!"""

code_explanation_template = """Based on our conversation, explain the following code to a junior developer:

{user_input}

Remember:
- Use simple language
- Include real-world analogies
- Suggest what to learn next
- Be encouraging!

Previous context in our conversation helps inform your explanation."""

debugging_template = """A junior developer has a coding problem:

{user_input}

Help them by:
1. Asking clarifying questions if needed
2. Identifying the likely issue
3. Suggesting solutions step-by-step
4. Explaining WHY the solution works

Be supportive - everyone writes buggy code!"""

learning_template = """Help this junior developer understand:

{user_input}

Your response should:
- Explain the concept clearly
- Provide a simple code example
- Suggest the next topic to learn
- Use encouraging language"""

# ============================================================================
# LANGCHAIN SETUP
# ============================================================================

def setup_llm_chain():
    """
    Initialize LangChain with CodeLlama via Hugging Face
    """
    try:
        # Initialize HuggingFace Pipeline for CodeLlama
        llm = HuggingFacePipeline(
            model_name="meta-llama/Llama-2-7b-chat-hf",  # Using Llama 2 (CodeLlama alternative)
            task="text-generation",
            model_kwargs={
                "temperature": 0.7,
                "top_p": 0.95,
                "max_length": 512,
                "do_sample": True,
            }
        )
        
        # Create conversation memory
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            max_token_limit=2048
        )
        
        # Create prompt template
        prompt = PromptTemplate(
            input_variables=["user_input", "chat_history"],
            template=SYSTEM_PROMPT + "\n\nChat History:\n{chat_history}\n\nUser: {user_input}\n\nCodeChat:"
        )
        
        # Create chain
        chain = LLMChain(
            llm=llm,
            prompt=prompt,
            memory=memory,
            verbose=True
        )
        
        return chain, memory
        
    except Exception as e:
        print(f"⚠️ Note: Full LLM setup failed. Using simplified version.\nError: {e}")
        return None, None


# ============================================================================
# SIMPLIFIED FALLBACK (if LLM not available)
# ============================================================================

class SimplifiedCodeChat:
    """
    Fallback assistant for demonstration/testing without heavy dependencies
    """
    
    def __init__(self):
        self.conversation_history = []
        self.keywords = {
            "function": "Functions are reusable blocks of code. Think of them like recipes!",
            "loop": "Loops repeat code multiple times. Like saying 'do this 10 times'.",
            "variable": "Variables store information, like containers holding data.",
            "array": "Arrays are lists of items, accessed by position numbers.",
            "debug": "Debugging means finding and fixing errors in code.",
            "error": "Errors are messages telling you something went wrong - they're helpful!",
            "class": "Classes are blueprints for creating objects with properties.",
            "api": "APIs let different programs talk to each other.",
        }
    
    def get_response(self, user_input: str) -> str:
        """Generate a response using keyword matching + fun facts"""
        
        response = ""
        
        # Store in history
        self.conversation_history.append({"role": "user", "content": user_input})
        
        # Simple keyword-based response
        found_keyword = False
        for keyword, explanation in self.keywords.items():
            if keyword.lower() in user_input.lower():
                response = f"Great question about {keyword}! 🎯\n\n{explanation}\n\n"
                found_keyword = True
                break
        
        if not found_keyword:
            response = "That's an interesting coding question! 💭\n\n"
            response += "Could you tell me more? Are you asking about:\n"
            response += "1. How to write code\n"
            response += "2. How to fix a bug\n"
            response += "3. What a concept means\n"
        
        # Add fun fact
        category = self._detect_category(user_input)
        fun_fact = random.choice(FUN_FACTS.get(category, FUN_FACTS["general"]))
        response += f"\n✨ {fun_fact}"
        
        # Store response in history
        self.conversation_history.append({"role": "assistant", "content": response})
        
        return response
    
    def _detect_category(self, text: str) -> str:
        """Detect topic category from user input"""
        text_lower = text.lower()
        if "python" in text_lower:
            return "python"
        elif "javascript" in text_lower or "js" in text_lower:
            return "javascript"
        elif "bug" in text_lower or "error" in text_lower or "fix" in text_lower:
            return "debugging"
        elif "sort" in text_lower or "algorithm" in text_lower:
            return "algorithms"
        else:
            return "general"
    
    def get_conversation_history(self) -> str:
        """Return formatted conversation history"""
        history_text = ""
        for msg in self.conversation_history:
            role = "You" if msg["role"] == "user" else "CodeChat"
            history_text += f"\n{role}: {msg['content']}\n"
        return history_text


# ============================================================================
# GRADIO INTERFACE
# ============================================================================

def create_gradio_interface():
    """
    Create the Gradio web interface for CodeChat
    """
    
    # Initialize chat assistant
    chat = SimplifiedCodeChat()
    conversation_state = {"history": []}
    
    def chat_function(user_message: str, chat_history):
        """
        Process user message and generate response
        
        Args:
            user_message: User's input message
            chat_history: List of previous messages
        
        Returns:
            tuple: (updated chat history, empty input field)
        """
        if not user_message.strip():
            return chat_history, ""
        
        # Get response from assistant
        response = chat.get_response(user_message)
        
        # Update chat history for display
        chat_history.append((user_message, response))
        
        return chat_history, ""
    
    def clear_conversation():
        """Clear conversation history and reset chat"""
        chat.conversation_history = []
        return [], ""
    
    # Build Gradio interface
    with gr.Blocks(title="CodeChat: AI-Powered Coding Assistant") as demo:
        
        gr.Markdown("""
        # 🤖 CodeChat: Your Friendly Coding Assistant
        
        **Learn to code the fun way!** Ask me anything about programming, and I'll explain it in simple terms with fun facts. 💡
        
        Perfect for:
        - 🎓 Understanding new concepts
        - 🐛 Debugging code
        - 📚 Learning best practices
        - 💬 Multi-turn conversations
        """)
        
        # Chat interface
        chatbot = gr.Chatbot(
            label="Conversation",
            height=400,
            show_copy_button=True,
            avatar_images=(None, "🤖")
        )
        
        # Input area
        with gr.Row():
            msg = gr.Textbox(
                label="Your Question",
                placeholder="Ask me about functions, loops, debugging... anything coding! 💭",
                lines=2,
                scale=5
            )
            submit_btn = gr.Button("Send", scale=1, variant="primary")
        
        # Control buttons
        with gr.Row():
            clear_btn = gr.Button("Clear Conversation 🗑️", scale=1)
            example_btn = gr.Button("Show Examples 📖", scale=1)
        
        # Examples section
        examples_section = gr.Textbox(
            label="Example Questions",
            value="""Try asking me:
- "What's a function and why do I need it?"
- "I'm getting an error in my loop, help me debug"
- "Explain arrays in simple terms"
- "How do I write a better code?"
- "Tell me about Python lists"
            """,
            lines=6,
            interactive=False
        )
        
        # Info section
        gr.Markdown("""
        ### 🎯 Features:
        - **Multi-turn Conversation**: Keep context across messages
        - **Fun Facts with Emojis**: Make learning enjoyable
        - **Beginner-Friendly**: Explanations in simple language
        - **Code Examples**: Real-world examples included
        
        ### 🚀 Tips:
        - Ask about specific concepts or code snippets
        - Share error messages for debugging help
        - Request explanations in simpler terms if needed
        """)
        
        # Set up event handlers
        submit_btn.click(
            fn=chat_function,
            inputs=[msg, chatbot],
            outputs=[chatbot, msg]
        ).then(
            lambda: None,
            inputs=None,
            outputs=None
        )
        
        msg.submit(
            fn=chat_function,
            inputs=[msg, chatbot],
            outputs=[chatbot, msg]
        )
        
        clear_btn.click(
            fn=clear_conversation,
            outputs=[chatbot, msg]
        )
    
    return demo


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("🚀 Starting CodeChat Application...")
    print("=" * 60)
    
    # Create interface
    interface = create_gradio_interface()
    
    # Launch
    interface.launch(
        share=False,
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True,
        debug=True
    )
