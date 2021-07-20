import streamlit as st

def main():
    name = "Amirtha Ganesh"

    st.title("Hare Krishna")
    if st.button("Submits"):
        st.write("Name: {}".format(name.upper()))
if __name__ == '__main__':
    main()
