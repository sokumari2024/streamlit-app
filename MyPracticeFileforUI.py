import streamlit  as st

# header
st.header("Start of UI")

# subheader

st.subheader("Test for SubHeader")

# Text

st.text("Text Line")

# check box

if (st.checkbox("Check the checkbox")):
    st.text("You clicked checkbox")

# Radio Button

status= st.radio("Select you Gender",('Male', 'Female'))
if(status=='Male'):
    st.text("You selected as Male")
else:
    st.text("you selected as Female")

#Interactive Function

num=st.number_input("Enter a num")
def sqr(num):
    return num*num


if st.button("Click to calulate square"):
    result=sqr(num)
    st.text(f"Result: {result}")
    
