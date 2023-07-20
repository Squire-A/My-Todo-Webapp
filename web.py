import streamlit as st
import functions as fn

todos = fn.open_todos()


def add_todo():
    new_todo = st.session_state['new_todo']
    todos.append(new_todo+"\n")
    fn.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("I learned how to make this app by doing Ardit's python megacourse.")


for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        fn.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo",
              placeholder="Add a new todo here",
              on_change=add_todo, key='new_todo')

