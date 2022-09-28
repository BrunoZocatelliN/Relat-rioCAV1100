
import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

st.set_page_config(layout="wide")

image = Image.open('nestle-chocolat-vector-logo-200x200.png')
st.sidebar.image(image,caption='',use_column_width=True)

st.title('_Relátório de Auditoria de Tablets_')
st.sidebar.markdown('Relatório base feito por : Bruno Zocatelli (NCE)')

user_input = st.sidebar.text_input("Digite seu nome")
st.write("Usuário resposavél pela Apresentação: ", user_input)

st.markdown('---')

st.markdown('# _Sobre a Auditoria_')
st.markdown(''' - _Esta Auditoria foi realizada com o intuito de proteger os bens atrelados a Nestle, mais especificamente na Fantastica Fabrica de Chocolate em Caçapava-SP_
             \n - _A auditoria tinha como principal motivo a realização da contagem de bens adquiridos pela empresa_''')

st.markdown('# _Base de Dados Utilizado como referencia_')

Dados = pd.read_excel('Relacao.xlsx')
st.dataframe(Dados)
            
st.markdown('---')

st.markdown('# _Envio de informações_')
st.markdown('- A Fabrica hoje conta com IPADs para pratiamente todos os setores, sendo exceção os setores que não estão ligados com a area de Digital, segue abaixo gráfico de demonstração da contagem geral dos aparelhos por setor')
st.markdown(''' - Alguns IPAD's não foram fisicamente verificados, Setores da fabrica realizaram suas próprias auditorias e enviaram as informações para complementar esta em questão, sendo assim
            segue o grafico de quantos foram verificados fisicamente''')


fig = px.bar(x = [28,17,7,6,4,2,2,2,2,2,1,1,1,1],
            y = ['Kit Kat   ','Choc 2   ','NCE   ','Confeitária   ','Choc 1   ','Logistica CPW   ','Armazem ME   ','Armazem PT   ','Armazem MPA   ','Sem Localização   ','Armazem CSSE   ','Almoxarifado   ','CAG   ','w1020   '],
            orientation='h', title=" Quantidade de Tablets por Linha/Setor ",
            labels={'x':'Quantidade','y':'Dados'})

st.plotly_chart(fig)

pix = px.bar(x = [28,57],
            y = ['Verificados Fisicamente   ','Não Verificados Fisicamente   '],
            orientation='h', title=" Quantidade de Tablets Verificados Fisicamente",
            labels={'x':'Quantidade de IPADs','y':'Tipo de Verificação'})

st.plotly_chart(pix)

