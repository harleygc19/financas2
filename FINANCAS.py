import streamlit as st
import pandas as pd
from openpyxl import load_workbook
import tela1.tela1 as tela1

st.set_page_config(page_title="Finanças HD",layout='wide',page_icon="Financas4.png")

df = pd.read_excel('Contas.xlsx')

def verificar_credenciais(username, senha):
    try:
        df = pd.read_excel('senhas.xlsx')
    except FileNotFoundError:
        st.error('Arquivo senhas não encontrado')        
        return False
    except Exception as e:
        st.error(f'Erro ao ler o arquivo: {e}')
        return False

    if any((df["username"] == username) & (df["senha"] == senha)):
        return True
    return False





# Código para Página de login
def login_page():
    
    col1,col2,col3 = st.columns((0.5,1,0.5))
    with col2:

         imagem1 = st.image('Financas4.png',use_column_width=True)
         imagem1 = st.sidebar.image('Financas4.png',use_column_width=True)
   
    username = st.sidebar.text_input('login')
    
    senha = st.sidebar.text_input('senha',type='password')

    if st.sidebar.button('login'):
        if verificar_credenciais(username, senha):
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.rerun()
        else: 
            st.error('usuário ou senha incorretos, tente novamente')
    st.sidebar.text('Controle financeiro HD') 


def pag_inicial():
    st.subheader('Controle Financeiro HD',divider='gray')
    pag1, pag2, pag3 = st.tabs(['Cadastro de Gastros','Cadastro de Recebimentos','Tabela'])
    with pag1:
        
        tela1.tela_formulario()

    with pag2:
        st.write ('Cadastro de recebimentos')

    with pag3:
        tela1.tela_tabela()











def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        pag_inicial()
    else:
        login_page()

if __name__ == "__main__":
    main()
