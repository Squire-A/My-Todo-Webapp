import streamlit as st
import functions as fn

todos = fn.open_todos()


if 'latest_todo' not in st.session_state:
    st.session_state.something = ''


def add_todo():
    st.session_state['latest_todo'] = st.session_state['new_todo']
    st.session_state['new_todo'] = ''
    new_todo = st.session_state['latest_todo']
    todos.append(new_todo+"\n")
    fn.write_todos(todos)


st.title("My Todo App")
st.subheader("A basic todo app")
st.write("I learned how to make this app by doing Ardit Sulce's python megacourse.")


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
