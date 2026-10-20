import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
client=OpenAI()

st.set_page_config(page_title="AI Mock Interview Coach",layout="wide")
st.title("💻AI Mock Interviewing Coach")

domain=st.text_input("Enter domain")
jobr=st.text_input("Enter job role")
diff=st.text_input("Enter difficulty level")
option=st.radio("Select Practice Mode",["Mock Que and Ans","Self Practice and Evaluation"])

if option=="Mock Que and Ans":
    question=st.number_input("Enter number of question")
    prompt=f''' You are an Interview coach. Your task is generating  mock interview questions on the basis of
given domain {domain}, job role {jobr} , number of questions {question} and difficulty level {diff}.
Generate proper mock interview question and answer relevant to current industry standards helpful to freshers and 
ug students.
Title of Domain:
Question1:
Answer1:

Question2:
Answer2:

'''
    response=client.responses.create(model="gpt-4.1-mini",input=prompt)
    st.write(response.output_text)

else:
    with st.form("Mock Practice"):
        answer=st.text_area("Enter your answer")
        submit=st.form_submit_button("Mock Evaluation")

    if submit:
        prompt = f"""You are an interview coach.
    Generate one interview question for:
    Domain: {domain}
    Job role: {jobr}
    Difficulty: {diff}
    Candidate answer: {answer if answer else "No answer provided yet"}

    If no answer is provided, display the question and ask the candidate
    to submit an answer.
    If an answer is provided, evaluate it against the generated question.
    Provide feedback, improvements, a score out of 10, and a better sample answer.
    Clearly separate the question and evaluation."""

        response=client.responses.create(model="gpt-4.1-mini",input=prompt)
        st.write(response.output_text)

#Re-Run.automatic theme, automatic recoring, cache clearing<- Why streamlit is better than html,css
#MVP-MARKET VIABLE PRODUCT