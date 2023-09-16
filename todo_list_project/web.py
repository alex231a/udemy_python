import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_in = st.session_state["new_todo"] + "\n"
    todos.append(todo_in)
    functions.write_todos(todos)


st.title("MY TODO APP")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter new todo...", on_change=add_todo, key="new_todo")

print("hello")
st.session_state

