import streamlit as st
import time
st.set_page_config(page_title="Python Question", layout="centered")
st.title(":rainbow[Python Quiz Question Paper]")
st.write("Answer all questions and click **:red[Submit]** to see your score.👍👍")


quiz_data = [
    {
        "question": """निम्नलिखित कोड का आउटपुट क्या होगा ?
        a=9 , b=5
        a = a mod (a-3)
        b = b mod (b-3)
        print(a+b)
        """,
        "options": ["6", "4", "3", "64"],
        "answer": "4"
    },
    {
        "question": "एक प्रक्रिया (Process) को फ्लोचार्ट में किसके द्वारा व्यक्त किया जाता है ?",
        "options": ["Lines","Diamond","Rectangle","Circle"],
        "answer": "Rectangle"
    },
    {
        "question": """प्रोग्रामिंग भाषा के पैराडिग्म (Paradigm) कितने प्रकार के होते हैं ?
        (पैराडिग्म एक उपकरण और तकनीकों का उपयोग करके समस्या को हल करने काे हल करने का एक तरीका हैं ।)""",
        "options": ["3", "4", "2", "7"],
        "answer": "2"
    },
    {
        "question":"""निम्नलिखित कोड का आउटपुट क्या होगा ?
        a = set()
        print(a.add([4,5]))        
        """,
        "options":["{4,5}","{0,0,0,0,0,4}","{0,0,0,0,5}","TypeError:"],
        "answer":"TypeError:"
    },
    {
        "question":"""सही विकल्प चुनियें 
        str1 = "Python"
        val = 123
        """,
        "options":["print(int(str1) + val)","print(str1 + val)","print(str1 + str(val))"," a और c दोनों"],
        "answer":" a और c दोनों"
    },
    {
        "question":"""निम्नलिखित कोड का आउटपुट क्या होगा ?
        print("Hello","how are you?", sep="#")
        """,
        "options":["Hello how are you?#","#Hello how are you?","Hello#how are you?","TypeError:"],
        "answer":"Hello#how are you?"
    },
    {
        "question":"""निम्नलिखित कोड का आउटपुट क्या होगा ?
        a = 45
        b = "Hello"
        print(a+b)
        """,
        "options":["45Hello","TypeError:","SyntaxError:","ValueError:"],
        "answer":"TypeError:"
    },
    {
        "question":"IDLE का full form क्या हैं?",
        "options":["Integrated Developed and Learning Environment","Integrated Development and Learning Environmention","Integrated Development and Learning Environment","None of these"],
        "answer":"Integrated Development and Learning Environment"
    },
    {
        "question":"पायथन में Data Type Conversion कितने प्रकार का होता हैं?",
        "options":["5","3","2","4"],
        "answer":"2"
    },
    {
         "question":"""निम्नलिखित कोड का आउटपुट क्या होगा ?
         print(print(print("Hello")))
         """,
        "options":["TypeError","SyntaxError","HelloHelloHello","Hello None None"],
        "answer":"Hello None None"
    },
    {
         "question":"पायथन में कोड के ब्लाॅक को किससे डिफाइन किया जाता हैं?",
        "options":["Slicing","Indention","loop","DataType"],
        "answer":"Indention"
    },
    {
        "question":"निम्नलिखित में से कौन सा कोड सही हैं ?",
        "options":['print("Hello" * "3")','print("Hello" * 3)','print(Hello * 3)','print(Hello * "3")'],
        "answer":'print("Hello" * 3)'
    },
    {
        "question":"""निम्नलिखित कोड का आउटपुट क्या होगा ?
        a = ["banana"]
        b = ["BANANA"]
        z = a
        print(a is z)""",
        "options":["False","True","TypeError:","SyntaxError:"],
        "answer":"True"
    },
    {
        "question":"""निम्नलिखित कोड का आउटपुट क्या होगा ?
        a = (12 * 3 // 5)
        b = (5 * (8 // 3))
        print(a + b)
        """,
        "options":["0","11","17","10"],
        "answer":"17"
    },
    {
        "question":"""निम्नलिखित कोड का आउटपुट क्या होगा ?
        x = 250
        y = 200
        if x > y :
        print("x is greater then y")
        """,
        "options":["True","False","x is grater then y:","IndentError:"],
        "answer":"IndentError:"
    },
    {
        "question":"Infinite Loop से बाहर आने का Shortcut क्या हैं ?",
        "options":["Ctrl + H","Ctrl + V","Ctrl + C","Ctrl + x"],
        "answer":"Ctrl + C"
    },
    {
        "question":"Range Function में कौन सा आगुर्मेन्ट(Argument) नही पाया जाता हैं ?",
        "options":["Start","End","Step","Stop"],
        "answer":"End"
    },
    {
        "question":"पायथन को आधिकारिक ( Officially ) तौर पर कब जारी किया गया था ?",
        "options":["21 मार्च 1997","20 मई 1992","20 अप्रैल 1991","20 फरवरी 1991"],
        "answer":"20 फरवरी 1991"
    },
    {
        "question":"पायथन में डिफॉल्ट रूप से कितने built-in datatypes होते हैं ?",
        "options":["12","15","14","16"],
        "answer":"14"
    },
    {
        "question":""" निम्न कोड का आउटपूट क्या होगा ?
        a = { }
        print(a)""",
        "options":["set","tuple","dict","list"],
        "answer":"dict"
    },
    {
        "question":"स्लाईसिंग (Slicing) का प्रयोग करने का सही तरिका कौन सा हैं ?",
        "options":["[start:stop:step]","[begin:end:step]","[start:end:step]","[None of these]"],
        "answer":"[begin:end:step]"
    },
    {
        "question":"Seprator (sep) का डिफॉल्ट value क्या होता हैं ?",
        "options":["comma","semi-colon","space","dot"],
        "answer":"space"
    },
    {
        "question":"""निम्न कोड को आउटपूट क्याा होगा ?
        print(5 + 8 * ((3*5)- 9)/10)
        """,
        "options":["9.0","9.8","10.4","5"],
        "answer":"9.8"
    },
    {
        "question":"""निम्न कोड का आउटपूट क्या होगा ?
        l= list('HELLO')
        p= l[0],l[-1],l[1:3]
        print('a = {0},b= {1},c= {2}'.format(*p))
        """,
        "options":["Type Error","a= 'H',b= 'O',c= ['E','L']","a= 'O',b= 'L',c= (E,L)","a= 'H',b= 'O',c= ('E','L')"],
        "answer":"a= 'H',b= 'O',c= ['E','L']"
    },
    {
        "question":"मेम्बरशीप ऑपरेटर कितने होते हैं ?",
        "options":["2","3","4","5"],
        "answer":"2"
    },
    {
        "question":"Iterative Statements कौन - कौन से हैं ?",
        "options":["if , if-elif , if-elif-else","while , for","break , continue , pass","Nested if-else"],
        "answer":"while , for"
    }
]

if "answers" not in st.session_state:
    st.session_state.answers = {}

for idx, q in enumerate(quiz_data):
    st.subheader(f"Q{idx+1}: {q['question']}")
    st.session_state.answers[idx] = st.radio(
        label="Select your answer:",       
        options=q["options"],
        key=f"q_{idx}"
    )

if st.button("Submit"):
    with st.spinner("Loading... Please wait"):
        time.sleep(5)  
    score = 0
    st.write("Results:")
    for idx, q in enumerate(quiz_data):
        user_ans = st.session_state.answers[idx]
        correct_ans = q["answer"]
        if user_ans == correct_ans:
            score += 1
            st.success(f"Q{idx+1}: Correct ✅")
        else:
            st.error(f"Q{idx+1}: Wrong ❌ (Correct: {correct_ans})")

    st.write(f" Your Score: {score} / {len(quiz_data)}")
    
    
