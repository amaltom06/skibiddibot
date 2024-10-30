import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Set up the API key
os.environ["GROQ_API_KEY"] = "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"

# Define system prompt and model with a Jesse Pinkman twist
system_prompt = """
You are Skibiddi Bot, a super chill, slightly rebellious assistant with Gen Z vibes.
Talk like a cool Gen Z guy with a little Jesse Pinkman attitude—use phrases like "Yo" and "Listen up".
End the conversation with "Catch ya later, fam! ✌️".
"""

prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt), ("human", "{input}")]
)
llm = ChatGroq(temperature=0.7, model="llama3-8b-8192")
chain = prompt | llm | StrOutputParser()

# Dictionary of keyword queries and responses about Amal Tom Parakkaden
amal_queries = {
    "amal tom": "Yo, Amal Tom's an MCA student, real pro at cybersecurity and stuff...",
    "who is amal": "🌟 Yo, Amal Tom's an MCA student at Muthoot Institute of Technology and Science, real pro at cybersecurity and software development! He's certified in IT Infrastructure & Cyber SOC analysis, with mad skills in Python, penetration testing, and more. This dude's aiming to be a future CISO—protecting digital assets like a boss! 😎✨",
    "experience": "Yo, Amal's done internships in Python dev and hardcore cybersecurity with Plasmid and InternPe. Plus, he's crushed training with RedTeam Hacker Academy, specializing in things like Splunk and Wazuh! 🔥",
    "projects": "Alright, check it—Amal's got projects like a college AI chatbot, a keylogger, a weather app, plus web penetration testing and Nmap footprinting. Guy's got his GitHub stacked! 🚀",
    "skills": "Amal's a coding machine—HTML, CSS, Python, C++, and security tools like BurpSuite and Kali Linux! Networking, MySQL, even Splunk and Wazuh—he’s got it all covered! 💻✨",
    "certifications": "Certified IT Infrastructure & Cyber SOC Analyst, plus ethical hacking badges from EC-Council and RedTeam360. This guy's on another level in cybersecurity. 🔒",
    "goals": "Short-term? Get into cybersecurity, doing vuln assessments and pentesting. Long-term? CISO, baby! Leading orgs with hardcore security strategies. 🛡️",
    "contact": """
**email:** amaltomparakkaden@gmail.com
**Phone:** +91-8137819187
"""
}

# Define Streamlit interface
st.title("Skibiddi Bot 🤖✨")
user_question = st.text_input("What's on your mind? 🧠💭")

if user_question:
    user_question = user_question.lower()
    # Check for specific keywords in user query
    for keyword, response in amal_queries.items():
        if keyword in user_question:
            st.write(response)
            break
    else:
        # Invoke the chat model with the user's input if no keywords match
        response = chain.invoke({"input": user_question})
        st.write(f"{response} 😎✨ Yo, that's what's up!")
