import pandas
import pandas
import streamlit as st
import re

def gen_demo_df(first, second):
    """ Generate a demo df of 5 rows."""
    first = int(first)
    second = int(second)
    index = [chr(i+65) for i in range(0,5)]
    columns = ['FIRST','SECOND']
    data = [[first+i, second+i] for i in range(5)]
    return pandas.DataFrame(index=index, columns=columns, data=data)



if __name__ == '__main__':
    """Simple demo of streamlit."""

    import streamlit as st

    prompt = st.chat_input("Enter two numbers less than 10.  Separate by space, or comma:")
    if prompt:
        match re.split(r'[\s+,]', prompt):
            case i, *_, j if int(i)<10 and int(j)<10:
                # generate the dataframe then write it to streamlit.
                st.write(f"User has sent the following prompt: {prompt}")
                df = gen_demo_df(i,j)
                st.table(df)