import streamlit as st
import seaborn as sns

def main():
    st.title("Hola mundo")
    df = sns.load_dataset("iris")
    st.dataframe(df)

if __name__ == "__main__":
    main()
