# Bibliotecas importadas para o projeto:
import streamlit as st
import datetime
import pandas as pd
import numpy as np

            
# Distribuição de páginas do site:
st.sidebar.title('Menu')
pagina_selecionada = st.sidebar.selectbox('Opções para realizar o acerto:', ['Dados Empresa', 'Dados da Frota', 'Cadastro Motorista', 'Cadastro Dados Viagem', 'Cadastro Abastecimentos', 'Cadastro Despesas', 'Fechamento do Acerto'])

# Seleções de páginas do site:
if pagina_selecionada == 'Dados Empresa':
    st.title("Acerto de Contas Transportes Gurupi Eirelli")
    st.subheader('CNPJ: 18.042.398/0001-94') 
    st.subheader('Inscrição Estadual: ')     
    st.subheader('Endereço: Rua 1, 45 SALA B.')
    st.subheader('Bairro: Valle dos Igarapés.')  
    st.subheader('Cidade: Igarapé.')  
    st.subheader('UF: Minas Gerais.')  
    
 
elif pagina_selecionada == 'Dados da Frota':
    st.title('Dados da Frota: ')
    with st.form(key="Include_Dados_Frota"):
        input_frota = st.text_input("Digite o número da frota: ") 
        input_placa_cavalo = st.text_input("Digite a placa do cavalo: ")  
        input_placa_carreta = st.text_input("Digite a placa da carreta: ")   
        enviar_dados_frota = st.form_submit_button("Enviar")
        
        
    
    if enviar_dados_frota:
        st.write(f"Frota: {input_frota}")
        st.write(f"Placa Cavalo: {input_placa_cavalo}")
        st.write(f"Placa Carreta: {input_placa_carreta}")
 
 
    
elif pagina_selecionada == 'Cadastro Motorista':
    st.title('Dados do Motorista: ')
    with st.form(key="Include_Cadastro_Motorista"):
        input_nome_motorista = st.text_input("Digite o nome do motorista:")  
        input_cpf_motorista = st.text_input("Digite o CPF do motorista:")  
        input_data_nascimento_motorista = st.date_input("Selecione a data do nascimento do motorista:", format="DD-MM-YYYY")     
        enviar_dados_motorista = st.form_submit_button("Enviar")
    
    
    
    if enviar_dados_motorista:
        st.write(f"Nome do Motorista: {input_nome_motorista}")
        st.write(f"CPF do Motorista:  {input_cpf_motorista}")
        st.write(f"Data do Nascimento do Motorista: {input_data_nascimento_motorista:%d/%m/%y}")
    
    
    
     
elif pagina_selecionada == 'Cadastro Dados Viagem':
    st.title('Dados da Viagem: ')
    with st.form(key="Include_Cadastro_Dados_Viagem"):
        input_numero_contrato = st.number_input("Digite o número do contrato: ", format="%d", step=1)
        input_valor_frete = st.number_input("Valor do Frete: ")
    
       
        selecao_adiantamento = st.selectbox('Selecione uma opção de adiantamento: ', ['Adiantamento em Cheque', 'Adiantamento Cartão Débito', 'Adiantamento em Folha'])
        enviar_dados_viagem = st.form_submit_button("Enviar")
       
    if selecao_adiantamento == 'Adiantamento em Folha':
        sem_adiantamento = (input_valor_frete * 0)
        st.write(f"Valor do Adiantamento:  R$ {sem_adiantamento:.2f}")

    else:
        adiantamento = (input_valor_frete * 0.5)
        st.write(f"Valor do Adiantamento:  R$ {adiantamento:.2f}")
        
        
    
    
    
elif pagina_selecionada == 'Cadastro Abastecimentos':
    st.title('Dados dos Abastecimentos: ')
    with st.form(key="Include_Cadastro_Abastecimentos"):
    
        st.write('---')
    
        # Containeres dos dados dos abastecimentos:
        with st.container():
            st.subheader('Km Viagem: ')
            input_km_inicial = st.number_input("Quilometragem Inicial da Viagem: ")
            input_km_final = st.number_input("Quilometragem Final da Viagem: ")
 
        st.write('---')     
      
        with st.container():
            st.subheader('Diesel: ')
            input_data_abastecimento = st.date_input("Data do Abastecimento:", format="DD/MM/YYYY")
            input_litragem_abastecimento_diesel = st.number_input("Litragem do Abastecimento de Diesel:")
            input_valor_abastecimento_diesel = st.number_input("Valor do Abastecimento de Diesel: ")
 
        st.write('---')   
    
        with st.container():
            st.subheader('Arla32: ')
            input_litragem_abastecimento_arla = st.number_input("Litragem do Arla32: ")
            input_valor_abastecimento_arla = st.number_input("Valor do Arla32: ")
    
      
    # Variáveis dos dados dos abastecimentos
        with st.container():  
            quilometros_rodados = st.write(input_km_final - input_km_inicial)
            media_consumo_diesel = st.write(quilometros_rodados  / input_litragem_abastecimento_diesel)               
            valor_total_abastecimento = st.write(input_valor_abastecimento_diesel + input_valor_abastecimento_arla)
            enviar_dados_abastecimentos = st.form_submit_button("Enviar")
        
         
    st.write('---')
    
    # Prints dos dados do abastecimento no site:
    st.subheader('Relatório do Abastecimento: ')    
    with st.container():
        st.write(f"Data do Abastecimento:  {input_data_abastecimento:%d/%m/%y}")
        st.write(f"Litragem do Abastecimento de Diesel: {input_litragem_abastecimento_diesel:.3f}")
        st.write(f"Valor do Abastecimento de Diesel:  R$ {input_valor_abastecimento_diesel:.2f}")

        st.write(f"Litragem do Abastecimento de Arla32: {input_litragem_abastecimento_arla:.3f}")
        st.write(f"Valor do Abastecimento de Arla32:  R$ {input_valor_abastecimento_arla:.2f}")
        st.write(f"Valor total do Abastecimento: R$ {valor_total_abastecimento:.2f}")
        st.write(f"Quilometros Rodados:  {quilometros_rodados}")
        st.write(f"Média Consumo de Diesel: {media_consumo_diesel}")

elif pagina_selecionada == 'Cadastro Despesas':
    st.title('Dados das Despesas: ')
    with st.form(key="Include_Cadastro_Despesas"):
        
    
        # Variáveis dos dados de despesas::
        chapa = st.number_input("Valor do Chapa: ")
        caixinha = st.number_input("Valor da Caixinha:")
        conferente = st.number_input("Valor do Conferênte: ")
        borracheiro = st.number_input("Valor do Borracheiro: ")
        mecanico = st.number_input("Valor do Mecânico: ")
        demais_despesas = st.number_input("Valor das Demais Despesas: ")
    
    
    
        # Cálculos Despesas:
        total_despesas = chapa + caixinha + conferente  + borracheiro + mecanico + demais_despesas
        
        enviar_dados_despesas = st.form_submit_button("Enviar")
        
        
            
    with st.container():
        if enviar_dados_despesas:
            st.write(f'A despesa total é:  R$ {total_despesas:.2f}')    
         
         
         
elif pagina_selecionada == 'Fechamento do Acerto':
    st.title('Fechamento do Acerto de Contas: ')
    