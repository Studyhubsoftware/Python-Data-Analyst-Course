import streamlit as st
st.image("https://th.bing.com/th/id/R.07111228fd92d6b5cc2a99bca60dbccd?rik=dGXv9fe%2bd17GWw&riu=http%3a%2f%2fwww.ilutegroup.com%2fwp-content%2fuploads%2f2017%2f07%2fquizzy_letter_Q_decorative_luxury_LED_lighting_lamp-.jpg&ehk=QN1cTZRI79%2fg46yCTYAPciIABHrzQm1J%2fk9Gmz35icY%3d&risl=&pid=ImgRaw&r=0")
st.title("string App")
message = st.text_area("Enter some text")
button = st.button("Process text")

if button:
    st.write(message)
if st.checkbox("Show words"):
    word = message.split()
    st.write(words)
if st.sidebar.checkbox("character count"): 
    for char in message:
        st.write(f'{char} : {message.count(char)}')
       
