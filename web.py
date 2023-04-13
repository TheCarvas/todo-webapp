import streamlit as st
import functions

todos = functions.todos_from_file()


def add_todo():
    new_todo = st.session_state["new todo"]
    todos.append(new_todo+"\n")
    with open('todos.txt', 'w') as file:
        file.writelines(todos)


st.title("My todo App")
st.subheader("this is my todo app.")
st.write("This app is a great help to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="My next todo", placeholder="Add new todo...",
              on_change=add_todo, key='new todo')

