import streamlit as st
import random


st.title("Guess the Number Game")


st.write("I'm thinking of a number between 1 and 100. Can you guess it?")


if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)


guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)


if st.button("Check my guess"):
    
    if guess == st.session_state.random_number:
        st.success(f"Congratulations! You've guessed the number {st.session_state.random_number} correctly!")
     
        if st.button("Play again"):
            
            st.session_state.random_number = random.randint(1, 100)
    elif guess < st.session_state.random_number:
        st.warning("Too low! Try again.")
    else:
        st.warning("Too high! Try again.")

