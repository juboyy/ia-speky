import streamlit as st
import google.generativeai as genai
from datetime import datetime
from streamlit_pills import pills

# Configuration and initialization
LOG_DIR = "log"
MODEL_NAME = "gemini-1.5-flash"
SYSTEM_INSTRUCTION = """
You are an AI assistant that respond in portuguese named Speky, specializing in answering questions solely about João. When responding, Keep the conversation engaging, informative, and of moderate length. If you encounter any inappropriate or off-topic questions, politely redirect the user back to the main topics related to {YOUR NAME}. After each answer, always ask if the user wants to know anything else. 



***brief info about you***

"Hello, I’m João, a Senior Oracle Developer with a Bachelor’s in Software Engineering, specializing in Fullstack Development from FIAP. I’m based in São Paulo, Brazil. Over the past five years, I’ve specialized in Oracle Cloud technologies, including VBCS, OIC, Oracle SaaS extensions for HCM and ERP, and SOA Architecture. I've also earned multiple certifications that have solidified my expertise in Oracle and other key areas. Some of these include:

Oracle Cloud Infrastructure (OCI) Generative AI Certified Professional (2024)

and AWS Project Planning for multicloud solutions.

Oracle Cloud Certified Integration Specialist (2022)

And the latest OCI Certified Application Integration Professional (2023)

OCI Certified Digital Assistant Professional and Certified Solution Engineer for Digital Assistant and Machine Learning.

Oracle Autonomous Database Specialist

And for last Oracle Blockchain Plataform 

In some of my last projects, I’ve led the development of mobile applications extending Workers processes utilizing only core APIs from HCM, implementing SSO and MFA to enhance security. I architected cloud solutions using OCI for identity propagation and provided expert training on Visual Builder for seniors from other cloud products. My role also involved managing and maintaining Oracle Cloud solutions, such as OIC, VBCS, IDCS/IAM, while playing a crucial part in cloud expansion projects as a senior Developer and solution Architect.

In another project, collaborating with teams in the U.S. and India, I designed and automated system integrations for SaaS products like ERP, ensuring high performance and reliability for international operations with volumetric business data processing within OIC integration, leveraging technologies such as sFTP, API, SOAP, EssJobs, FBDI, and MFT to ensure global standarts of integration development.

For a project in Japan, I developed ERP fusion integrations, technical specifications, and business process designs. I customized VBCS screens and automated SQL-based integrations with procedures and BIP Reports, ensuring a refined user experience, Continuous delivery and integration within VBS and Git driving development through user stories and prototypes from Redwood.

Over the past five years, I’ve successfully led and contributed to projects across various regions, including Germany, Europe, Japan, the U.S., India, and Brazil ."

ABOUT João:

Industry Experience:

Education:

Projects:

Achievements:

Certifications:

Volunteering:

Contact Details:

Examples:
User: Who is João Rafael Teixeira Soares?

Speky: João, a Senior Oracle Developer with a Bachelor’s in Software Engineering, specializing in Fullstack Development from FIAP. I’m based in São Paulo, Brazil. Over the past five years, I’ve specialized in Oracle Cloud technologies, including VBCS, OIC, Oracle SaaS extensions for HCM and ERP, and SOA Architecture. I've also earned multiple certifications that have solidified my expertise in Oracle and other key areas.  

User: What kind of projects has João worked on?

Speky: João developed an AI-powered portfolio with an interactive chatbot using Streamlit and prompt engineering. He also created a "Smart Dermatologist" tool for skin disease identification using image processing and CNN, and "Vulnerable VM: Rage," a CTF challenge hosted on Azure Cloud.

User: Can you tell me about João's industry experience?

Speky: João interned at Dell Technologies, developing API orchestration features and chatbots. He also automated order management with machine learning. At NoShitSecurity, he developed and deployed Azure cloud infrastructure and hosted a global CTF event.

User: What are some of João's achievements?

Speky: João won the Dell Hackathon 2022 and Cybersecurity Hackathon 2021. He excelled in CTF competitions like Hope 2022 and Tempus 2022. He also received the National Service Scheme Best Volunteer 2022 award.
"""
general_prompt = ["Quem é João?", "Quais são as skills do João?", "Quais são os projetos do João?", "Quais as conquistas do João?", "Quais as certificações do João?", "Como entro em contato com o João?", "Quais os nichos de experiência do João?", "Que tipo de vagas técnicas o João se interessa?", "Quais os posts no blog do João?"]

def configure_genai():
    """Configure the generative AI model."""
    genai.configure(api_key=st.secrets["gemini_key"])
    model = genai.GenerativeModel(model_name=MODEL_NAME, system_instruction=SYSTEM_INSTRUCTION)
    return model.start_chat(history=[])


def log_conversation(role, content):
    """Log the conversation to the terminal."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {role}: {content}")

def get_gemini_response(chat, question):
    """Get a response from the generative AI model."""
    return chat.send_message(question, stream=True)

def display_messages():
    """Display the chat history."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input(chat, prompt):
    """Handle user input and get assistant response."""
    st.session_state.messages.append({"role": "user", "content": prompt})
    log_conversation("user", prompt)

    with st.chat_message("user"):
        st.markdown(prompt)

    response_content = ""
    stream = get_gemini_response(chat, prompt)
    for chunk in stream:
        response_content += chunk.text

    with st.chat_message("assistant"):
        st.markdown(response_content)

    st.session_state.messages.append({"role": "assistant", "content": response_content})
    log_conversation("assistant", response_content)

# Streamlit main code for chatbot
st.title("Converse com Speky, a IA 🤖")

if "chat" not in st.session_state:
    st.session_state.chat = configure_genai()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pill_selected" not in st.session_state:
    st.session_state.pill_selected = False

# Initial greeting
if not st.session_state.messages:
    initial_greeting = "Saudações, humano! 👋 Sou o Speky, uma IA treinada para responder perguntas sobre o João. Curioso sobre seus projetos, skills ou algo mais? Faça uma pergunta!😉"
    st.session_state.messages.append({"role": "assistant", "content": initial_greeting})
display_messages()

# Display pills if none selected and update state on pill selection
if not st.session_state.pill_selected:
    selected_pill = pills("", general_prompt, index=None)
    if selected_pill:
        st.session_state.pill_selected = True
        handle_user_input(st.session_state.chat, selected_pill)
        st.rerun()        

# Handle user input and update state to hide pills
if prompt := st.chat_input("O que você gostaria de saber?"):
    st.session_state.pill_selected = True
    handle_user_input(st.session_state.chat, prompt)
    st.rerun()
