import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px


# Função para conectar ao banco de dados
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="lhrawiczq2",  # Substitua pela sua senha
        database="ProgramaSocioCamisa7"
    )


# Função para executar consultas no banco de dados
def run_query(query, params=None):
    conn = connect_to_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params or ())
    result = cursor.fetchall()
    conn.close()
    return pd.DataFrame(result)

# Configuração do layout
st.set_page_config(page_title="Gerenciamento de Sócios", layout="wide")
st.title("Programa Sócio Camisa 7")

# Criação das abas
tabs = st.tabs([
    "Dashboard", "Sócios Ativos", "Pontos dos Sócios", "Relatório de Pagamentos",
    "Benefícios Disponíveis", "Ingressos por Sócio", "Eventos por Sócio", "Gerenciamento", "Busca Específica"
])

# Função para adicionar um novo sócio
def add_socio(nome, email, cpf, endereco, telefone, data_adesao, id_plano, metodo_pagamento):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # Determinar os pontos iniciais com base no plano
        pontos_iniciais = 0
        if id_plano == 3:  # Plano Ouro
            pontos_iniciais = 500
        elif id_plano == 2:  # Plano Prata
            pontos_iniciais = 300
        elif id_plano == 1:  # Plano Bronze
            pontos_iniciais = 100

        # Inserir o novo sócio na tabela Sócio
        socio_query = """
            INSERT INTO Sócio (Nome, Email, CPF, Endereço, Telefone, Data_adesao, ID_Plano, Pontos_socio)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        socio_values = (nome, email, cpf, endereco, telefone, data_adesao, id_plano, pontos_iniciais)
        cursor.execute(socio_query, socio_values)
        novo_id_socio = cursor.lastrowid  # Recupera o ID do sócio recém-adicionado

        # Recuperar o valor do plano
        plano_query = "SELECT Valor_mensal FROM Plano WHERE ID_Plano = %s"
        cursor.execute(plano_query, (id_plano,))
        valor_plano = cursor.fetchone()[0]

        # Inserir o pagamento inicial na tabela Pagamento
        pagamento_query = """
            INSERT INTO Pagamento (Data_pagamento, Valor_pago, Metodo_pagamento, Status_pagamento, ID_Socio, ID_Plano)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        pagamento_values = (data_adesao, valor_plano, metodo_pagamento, True, novo_id_socio, id_plano)
        cursor.execute(pagamento_query, pagamento_values)

        conn.commit()
        conn.close()
        st.success(f"Novo sócio {nome} adicionado com sucesso!")
    except Exception as e:
        st.error(f"Erro ao adicionar sócio: {e}")


# Função para remover um sócio
def remove_socio(id_socio):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # Remover dependências do sócio nas tabelas relacionadas
        cursor.execute("DELETE FROM Participacao_Evento WHERE ID_Socio = %s", (id_socio,))
        cursor.execute("DELETE FROM Ingresso WHERE ID_Socio = %s", (id_socio,))
        cursor.execute("DELETE FROM Pagamento WHERE ID_Socio = %s", (id_socio,))

        # Remover o sócio
        cursor.execute("DELETE FROM Sócio WHERE ID_Socio = %s", (id_socio,))
        conn.commit()
        conn.close()
        st.success("Sócio removido com sucesso!")
    except Exception as e:
        st.error(f"Erro ao remover sócio: {e}")

# Função para adicionar pontos a um sócio
def add_points_to_socio(id_socio, pontos_adicionais):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE Sócio SET Pontos_socio = Pontos_socio + %s WHERE ID_Socio = %s", (pontos_adicionais, id_socio))
        conn.commit()
        conn.close()
        st.success(f"{pontos_adicionais} pontos adicionados com sucesso!")
    except Exception as e:
        st.error(f"Erro ao adicionar pontos: {e}")


# Função para remover pontos de um sócio
def remove_points_from_socio(id_socio, pontos_removidos):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # Garantir que os pontos não fiquem negativos
        cursor.execute("SELECT Pontos_socio FROM Sócio WHERE ID_Socio = %s", (id_socio,))
        pontos_atuais = cursor.fetchone()[0]

        if pontos_atuais < pontos_removidos:
            st.error("Erro: Não é possível remover mais pontos do que o sócio possui.")
            return

        cursor.execute("UPDATE Sócio SET Pontos_socio = Pontos_socio - %s WHERE ID_Socio = %s", (pontos_removidos, id_socio))
        conn.commit()
        conn.close()
        st.success(f"{pontos_removidos} pontos removidos com sucesso!")
    except Exception as e:
        st.error(f"Erro ao remover pontos: {e}")


# Exibição de cada aba
with tabs[0]:  # Primeira aba como Dashboard
    st.subheader("Dashboard Resumido")

    # Total de Sócios Ativos
    total_socios_query = "SELECT COUNT(*) AS Total FROM Sócio WHERE Status_socio = TRUE"
    total_socios = run_query(total_socios_query)
    total_socios_valor = total_socios.iloc[0]['Total'] if not total_socios.empty else 0
    st.metric("Sócios Ativos", total_socios_valor)

    # Total de Pagamentos Recebidos
    total_pagamentos_query = "SELECT SUM(Valor_pago) AS Total FROM Pagamento WHERE Status_pagamento = TRUE"
    total_pagamentos = run_query(total_pagamentos_query)
    total_pagamentos_valor = float(total_pagamentos.iloc[0]['Total']) if not total_pagamentos.empty else 0.0
    st.metric("Total de Pagamentos (R$)", f"{total_pagamentos_valor:.2f}")

    # Média de Pontos dos Sócios
    media_pontos_query = "SELECT AVG(Pontos_socio) AS Media FROM Sócio WHERE Status_socio = TRUE"
    media_pontos = run_query(media_pontos_query)
    media_pontos_valor = float(media_pontos.iloc[0]['Media']) if not media_pontos.empty else 0.0
    st.metric("Média de Pontos dos Sócios", f"{media_pontos_valor:.2f}")

    # Sócio com Mais Pontos
    top_socio_query = "SELECT Nome, Pontos_socio FROM Sócio ORDER BY Pontos_socio DESC LIMIT 1"
    top_socio = run_query(top_socio_query)
    if not top_socio.empty:
        top_socio_nome = top_socio.iloc[0]['Nome']
        top_socio_pontos = int(top_socio.iloc[0]['Pontos_socio'])
        st.metric("Sócio com Mais Pontos", f"{top_socio_nome} ({top_socio_pontos})")
    else:
        st.metric("Sócio com Mais Pontos", "Nenhum dado disponível")

    # Número de Eventos Exclusivos Futuros
    eventos_futuros_query = """
        SELECT COUNT(*) AS Total FROM Evento_Exclusivo WHERE Data_evento >= CURDATE()
    """
    eventos_futuros = run_query(eventos_futuros_query)
    eventos_futuros_valor = eventos_futuros.iloc[0]['Total'] if not eventos_futuros.empty else 0
    st.metric("Próximos Eventos Exclusivos", eventos_futuros_valor)

    # Próximos Eventos
    eventos_query = """
        SELECT Nome_evento, Data_evento
        FROM Evento_Exclusivo
        WHERE Data_evento >= CURDATE()
        ORDER BY Data_evento ASC
        LIMIT 5
    """
    proximos_eventos = run_query(eventos_query)
    st.markdown("### Próximos Eventos Exclusivos")
    if not proximos_eventos.empty:
        proximos_eventos.index = proximos_eventos.index + 1
        st.table(proximos_eventos)
    else:
        st.info("Nenhum evento próximo.")

    # Gráficos no Dashboard
    st.markdown("#### Gráficos Resumidos")

    # Gráfico de Distribuição de Planos
    planos_query = """
        SELECT p.Nome_Plano, COUNT(s.ID_Socio) AS Total
        FROM Sócio s
        JOIN Plano p ON s.ID_Plano = p.ID_Plano
        GROUP BY p.Nome_Plano
    """
    planos = run_query(planos_query)
    if not planos.empty:
        fig1 = px.pie(
            planos,
            names="Nome_Plano",
            values="Total",
            title="Distribuição de Sócios por Plano",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig1, use_container_width=True)

    # Gráfico de Pagamentos Mensais
    pagamentos_por_mes_query = """
        SELECT DATE_FORMAT(Data_pagamento, '%Y-%m') AS Mes, SUM(Valor_pago) AS Total
        FROM Pagamento
        WHERE Status_pagamento = TRUE
        GROUP BY DATE_FORMAT(Data_pagamento, '%Y-%m')
        ORDER BY Mes
    """
    pagamentos_por_mes = run_query(pagamentos_por_mes_query)
    if not pagamentos_por_mes.empty:
        fig2 = px.bar(
            pagamentos_por_mes,
            x="Mes",
            y="Total",
            title="Pagamentos Recebidos por Mês",
            labels={"Mes": "Mês", "Total": "Valor Recebido (R$)"},
            color="Total",
            color_continuous_scale=px.colors.sequential.Teal
        )
        st.plotly_chart(fig2, use_container_width=True)

with tabs[1]:
    st.subheader("Sócios Ativos")
    query = """
        SELECT s.Nome, s.Email, s.Telefone, s.Data_adesao, s.Pontos_socio, p.Nome_Plano
        FROM Sócio s
        JOIN Plano p ON s.ID_Plano = p.ID_Plano
        WHERE s.Status_socio = TRUE
    """
    socios_ativos = run_query(query)
    if not socios_ativos.empty:
        socios_ativos.index = socios_ativos.index + 1  # Ajustar o índice para começar do 1
        st.dataframe(socios_ativos.style.set_table_styles(
            [{'selector': 'th', 'props': [('background-color', '#37474F'), ('color', 'white')]}]
        ))
    else:
        st.info("Nenhum sócio ativo encontrado.")



with tabs[2]:
    st.subheader("Pontos dos Sócios")

    # Consulta SQL para obter pontos dos sócios
    query = "SELECT Nome, Pontos_socio FROM Sócio ORDER BY Pontos_socio DESC"
    pontos_socios = run_query(query)

    if not pontos_socios.empty:

        pontos_socios.index = pontos_socios.index + 1

        # Exibe a tabela
        st.dataframe(pontos_socios)

        # Dashboard com informações detalhadas
        st.markdown("### Dashboard de Pontos")

        # Métricas gerais
        total_pontos = pontos_socios["Pontos_socio"].sum()
        num_socios = len(pontos_socios)
        media_pontos = pontos_socios["Pontos_socio"].mean()
        socio_top_pontos = pontos_socios.iloc[0]["Nome"]
        pontos_top_socio = pontos_socios.iloc[0]["Pontos_socio"]

        # Exibição de métricas
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total de Pontos", f"{total_pontos}")
        col2.metric("Média de Pontos", f"{media_pontos:.2f}")
        col3.metric("Sócio com Mais Pontos", socio_top_pontos)
        col4.metric("Pontos do Top Sócio", f"{pontos_top_socio}")

        # Gráficos detalhados
        st.markdown("#### Gráficos")

        # Gráfico de barras: Distribuição de pontos por sócio
        fig1 = px.bar(
            pontos_socios,
            x="Nome",
            y="Pontos_socio",
            title="Distribuição de Pontos por Sócio",
            labels={"Nome": "Sócio", "Pontos_socio": "Pontos"},
            color="Pontos_socio",
            color_continuous_scale=px.colors.sequential.Blues
        )
        st.plotly_chart(fig1, use_container_width=True)

        # Gráfico de pizza: Participação percentual dos pontos
        fig2 = px.pie(
            pontos_socios,
            names="Nome",
            values="Pontos_socio",
            title="Participação Percentual dos Pontos por Sócio",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig2, use_container_width=True)

    else:
        st.info("Nenhum ponto encontrado.")


with tabs[3]:
    st.subheader("Relatório de Pagamentos")

    # Consulta SQL para obter os pagamentos
    query = """
        SELECT s.Nome AS Nome_Socio, p.Data_pagamento, p.Valor_pago, p.Metodo_pagamento, p.Status_pagamento
        FROM Pagamento p
        JOIN Sócio s ON p.ID_Socio = s.ID_Socio
    """
    pagamentos = run_query(query)

    if not pagamentos.empty:

        pagamentos.index = pagamentos.index + 1

        # Exibe a tabela de pagamentos
        st.dataframe(pagamentos)

        # Dashboard com informações detalhadas
        st.markdown("### Dashboard de Pagamentos")

        # Filtrar pagamentos confirmados
        pagamentos_confirmados = pagamentos[pagamentos["Status_pagamento"] == 1]

        # Métricas gerais
        total_recebido = pagamentos_confirmados["Valor_pago"].sum()
        num_pagamentos = len(pagamentos)
        num_pagamentos_pendentes = len(pagamentos[pagamentos["Status_pagamento"] == 0])
        media_pagamentos = pagamentos_confirmados["Valor_pago"].mean()

        # Exibição de métricas
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Recebido (R$)", f"{total_recebido:.2f}")
        col2.metric("Total de Pagamentos", num_pagamentos)
        col3.metric("Pagamentos Pendentes", num_pagamentos_pendentes)
        col4.metric("Média dos Pagamentos (R$)", f"{media_pagamentos:.2f}" if not pd.isna(media_pagamentos) else "0.00")

        # Gráficos detalhados
        st.markdown("#### Gráficos")

        # Gráfico de barras: Valor pago por método de pagamento (apenas confirmados)
        metodo_pagamento_fig = px.bar(
            pagamentos_confirmados.groupby("Metodo_pagamento")["Valor_pago"].sum().reset_index(),
            x="Metodo_pagamento",
            y="Valor_pago",
            title="Total Recebido por Método de Pagamento",
            labels={"Valor_pago": "Valor Recebido (R$)", "Metodo_pagamento": "Método de Pagamento"},
            color="Metodo_pagamento"
        )
        st.plotly_chart(metodo_pagamento_fig, use_container_width=True)

        # Gráfico de pizza: Status dos pagamentos
        status_pagamento_fig = px.pie(
            pagamentos,
            names="Status_pagamento",
            title="Distribuição de Status de Pagamentos",
            color_discrete_sequence=px.colors.sequential.RdBu,
            hole=0.4
        )
        st.plotly_chart(status_pagamento_fig, use_container_width=True)

        # Gráfico de linhas: Pagamentos ao longo do tempo (apenas confirmados)
        pagamentos_confirmados["Data_pagamento"] = pd.to_datetime(pagamentos_confirmados["Data_pagamento"])
        pagamentos_por_data = pagamentos_confirmados.groupby("Data_pagamento")["Valor_pago"].sum().reset_index()
        pagamentos_por_data_fig = px.line(
            pagamentos_por_data,
            x="Data_pagamento",
            y="Valor_pago",
            title="Pagamentos ao Longo do Tempo",
            labels={"Data_pagamento": "Data", "Valor_pago": "Valor Pago (R$)"}
        )
        st.plotly_chart(pagamentos_por_data_fig, use_container_width=True)

    else:
        st.info("Nenhum pagamento encontrado.")



with tabs[4]:
    st.subheader("Benefícios Disponíveis")

    # Consulta de dados para os benefícios
    query = """
        SELECT s.Nome AS Nome_Socio, b.Tipo_Beneficio, b.Pontos_necessarios, s.Pontos_socio
        FROM Sócio s
        JOIN Plano_Beneficio pb ON s.ID_Plano = pb.ID_Plano
        JOIN Benefício b ON pb.ID_Beneficio = b.ID_Beneficio
        WHERE s.Pontos_socio >= b.Pontos_necessarios
    """
    beneficios_df = run_query(query)

    # Dashboard de Benefícios
    if not beneficios_df.empty:
        st.markdown("### Dashboard: Benefícios Disponíveis")
        st.markdown("Visualize e analise os benefícios disponíveis para os sócios.")

        st.markdown("#### Dados de Benefícios")

        beneficios_df.index = beneficios_df.index + 1

        st.dataframe(beneficios_df.style.set_table_styles(
            [{'selector': 'th', 'props': [('background-color', '#37474F'), ('color', 'white')]}]))

        # Gráficos organizados em colunas
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### Pontos Necessários por Tipo de Benefício")
            fig1 = px.bar(
                beneficios_df,
                x="Tipo_Beneficio",
                y="Pontos_necessarios",
                color="Tipo_Beneficio",
                title="Pontos Necessários",
                color_discrete_sequence=px.colors.qualitative.Set3,
            )
            st.plotly_chart(fig1, use_container_width=True)

            st.markdown("#### Pontos dos Sócios com Benefícios Disponíveis")
            fig2 = px.bar(
                beneficios_df,
                x="Nome_Socio",
                y="Pontos_socio",
                color="Nome_Socio",
                title="Pontos dos Sócios",
                color_discrete_sequence=px.colors.qualitative.Pastel,
            )
            st.plotly_chart(fig2, use_container_width=True)

        with col2:
            st.markdown("#### Distribuição de Benefícios por Tipo")
            fig3 = px.pie(
                beneficios_df,
                names="Tipo_Beneficio",
                values="Pontos_necessarios",
                title="Distribuição de Benefícios",
                color_discrete_sequence=px.colors.sequential.RdBu,
            )
            st.plotly_chart(fig3, use_container_width=True)

            st.markdown("#### Quantidade de Benefícios por Sócio")
            fig4 = px.histogram(
                beneficios_df,
                x="Nome_Socio",
                title="Quantidade de Benefícios",
                color="Nome_Socio",
                color_discrete_sequence=px.colors.qualitative.T10,
            )
            st.plotly_chart(fig4, use_container_width=True)
    else:
        st.info("Nenhum benefício disponível.")

with tabs[5]:  # Aba de Ingressos por Sócio
    st.subheader("Ingressos por Sócio")

    # Consulta para exibir ingressos
    query = """
        SELECT s.Nome AS Nome_Socio, i.Jogo, i.Data_jogo, i.Desconto
        FROM Ingresso i
        JOIN Sócio s ON i.ID_Socio = s.ID_Socio
    """
    ingressos = run_query(query)

    if not ingressos.empty:

        ingressos.index = ingressos.index + 1

        st.dataframe(ingressos)
    else:
        st.info("Nenhum ingresso encontrado.")

    st.markdown("---")
    st.markdown("### Resumo de Ingressos")

    # Total de Ingressos Vendidos
    total_ingressos_query = "SELECT COUNT(*) AS Total FROM Ingresso"
    total_ingressos = run_query(total_ingressos_query)
    total_ingressos_valor = total_ingressos.iloc[0]['Total'] if not total_ingressos.empty else 0
    st.metric("Total de Ingressos Vendidos", total_ingressos_valor)

    # Média de Desconto Oferecido
    media_desconto_query = "SELECT AVG(Desconto) AS Media FROM Ingresso"
    media_desconto = run_query(media_desconto_query)
    media_desconto_valor = float(media_desconto.iloc[0]['Media'] * 100) if not media_desconto.empty else 0.0
    st.metric("Média de Desconto (%)", f"{media_desconto_valor:.2f}")

    # Próximos Jogos
    proximos_jogos_query = """
        SELECT Jogo, Data_jogo
        FROM Ingresso
        WHERE Data_jogo >= CURDATE()
        ORDER BY Data_jogo ASC
        LIMIT 5
    """
    proximos_jogos = run_query(proximos_jogos_query)
    st.markdown("### Próximos Jogos")
    if not proximos_jogos.empty:
        st.table(proximos_jogos)
    else:
        st.info("Nenhum jogo futuro encontrado.")

    # Gráficos
    st.markdown("#### Análises Gráficas")

    # Distribuição de Descontos
    if not ingressos.empty:
        fig1 = px.histogram(
            ingressos,
            x="Desconto",
            title="Distribuição de Descontos nos Ingressos",
            labels={"Desconto": "Desconto (%)"},
            nbins=10,
            text_auto=True,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig1, use_container_width=True)

    # Total de Ingressos por Sócio
    ingressos_por_socio_query = """
        SELECT s.Nome AS Nome_Socio, COUNT(i.ID_Ingresso) AS Total
        FROM Ingresso i
        JOIN Sócio s ON i.ID_Socio = s.ID_Socio
        GROUP BY s.Nome
        ORDER BY Total DESC
        LIMIT 10
    """
    ingressos_por_socio = run_query(ingressos_por_socio_query)
    if not ingressos_por_socio.empty:
        fig2 = px.bar(
            ingressos_por_socio,
            x="Nome_Socio",
            y="Total",
            title="Total de Ingressos por Sócio",
            labels={"Nome_Socio": "Sócio", "Total": "Ingressos"},
            color="Total",
            color_continuous_scale=px.colors.sequential.Teal
        )
        st.plotly_chart(fig2, use_container_width=True)


with tabs[6]:  # Aba de Eventos por Sócio
    st.subheader("Eventos por Sócio")

    # Consulta para exibir eventos
    query = """
        SELECT ee.Nome_evento, ee.Data_evento, s.Nome AS Nome_Socio, pe.Data_inscricao
        FROM Evento_Exclusivo ee
        JOIN Participacao_Evento pe ON ee.ID_Evento = pe.ID_Evento
        JOIN Sócio s ON pe.ID_Socio = s.ID_Socio
    """
    eventos = run_query(query)

    if not eventos.empty:

        eventos.index = eventos.index + 1

        st.dataframe(eventos)
    else:
        st.info("Nenhum evento encontrado.")

    st.markdown("---")
    st.markdown("### Resumo de Eventos")

    # Total de Eventos Realizados
    total_eventos_query = "SELECT COUNT(*) AS Total FROM Evento_Exclusivo"
    total_eventos = run_query(total_eventos_query)
    total_eventos_valor = total_eventos.iloc[0]['Total'] if not total_eventos.empty else 0
    st.metric("Total de Eventos Realizados", total_eventos_valor)

    # Total de Participações
    total_participacoes_query = "SELECT COUNT(*) AS Total FROM Participacao_Evento"
    total_participacoes = run_query(total_participacoes_query)
    total_participacoes_valor = total_participacoes.iloc[0]['Total'] if not total_participacoes.empty else 0
    st.metric("Total de Participações em Eventos", total_participacoes_valor)

    # Eventos Futuros
    proximos_eventos_query = """
        SELECT Nome_evento, Data_evento
        FROM Evento_Exclusivo
        WHERE Data_evento >= CURDATE()
        ORDER BY Data_evento ASC
        LIMIT 5
    """
    proximos_eventos = run_query(proximos_eventos_query)
    st.markdown("### Próximos Eventos")
    if not proximos_eventos.empty:
        st.table(proximos_eventos)
    else:
        st.info("Nenhum evento futuro encontrado.")

    # Gráficos
    st.markdown("#### Análises Gráficas")

    # Total de Participações por Evento
    participacoes_por_evento_query = """
        SELECT ee.Nome_evento, COUNT(pe.ID_Socio) AS Total
        FROM Evento_Exclusivo ee
        JOIN Participacao_Evento pe ON ee.ID_Evento = pe.ID_Evento
        GROUP BY ee.Nome_evento
        ORDER BY Total DESC
        LIMIT 10
    """
    participacoes_por_evento = run_query(participacoes_por_evento_query)
    if not participacoes_por_evento.empty:
        fig1 = px.bar(
            participacoes_por_evento,
            x="Nome_evento",
            y="Total",
            title="Participações por Evento",
            labels={"Nome_evento": "Evento", "Total": "Participações"},
            color="Total",
            color_continuous_scale=px.colors.sequential.Blues
        )
        st.plotly_chart(fig1, use_container_width=True)

    # Participações por Sócio
    participacoes_por_socio_query = """
        SELECT s.Nome AS Nome_Socio, COUNT(pe.ID_Evento) AS Total
        FROM Participacao_Evento pe
        JOIN Sócio s ON pe.ID_Socio = s.ID_Socio
        GROUP BY s.Nome
        ORDER BY Total DESC
        LIMIT 10
    """
    participacoes_por_socio = run_query(participacoes_por_socio_query)
    if not participacoes_por_socio.empty:
        fig2 = px.bar(
            participacoes_por_socio,
            x="Nome_Socio",
            y="Total",
            title="Participações por Sócio",
            labels={"Nome_Socio": "Sócio", "Total": "Participações"},
            color="Total",
            color_continuous_scale=px.colors.sequential.Teal
        )
        st.plotly_chart(fig2, use_container_width=True)


with tabs[7]:  # Aba de Gerenciamento
    st.subheader("Gerenciamento")

    # Seção de Gerenciar Sócios
    st.markdown("### Gerenciar Sócios")
    col1, col2 = st.columns(2)

    # Adicionar Sócio
    with col1.expander("Adicionar Sócio"):
        nome = st.text_input("Nome", key="add_nome")
        email = st.text_input("Email", key="add_email")
        cpf = st.text_input("CPF", key="add_cpf")
        endereco = st.text_input("Endereço", key="add_endereco")
        telefone = st.text_input("Telefone", key="add_telefone")
        data_adesao = st.date_input("Data de Adesão", key="add_data")

        query = "SELECT ID_Plano, Nome_Plano FROM Plano"
        planos_df = run_query(query)
        planos = {row['Nome_Plano']: row['ID_Plano'] for _, row in planos_df.iterrows()}
        plano = st.selectbox("Plano", list(planos.keys()), key="add_plano")
        metodo_pagamento = st.selectbox("Método de Pagamento", ["Cartão de Crédito", "Boleto Bancário", "Pix"],
                                        key="add_metodo")

        if st.button("Adicionar Sócio", key="btn_add_socio"):
            add_socio(nome, email, cpf, endereco, telefone, data_adesao, planos[plano], metodo_pagamento)

    # Remover Sócio
    with col2.expander("Remover Sócio"):
        query = "SELECT ID_Socio, Nome FROM Sócio"
        socios_df = run_query(query)
        socios = {row['Nome']: row['ID_Socio'] for _, row in socios_df.iterrows()}
        socio_selecionado = st.selectbox("Selecione o Sócio", list(socios.keys()), key="remove_socio")

        if st.button("Remover Sócio", key="btn_remove_socio"):
            remove_socio(socios[socio_selecionado])

    # Seção de Gerenciar Pontuações
    st.markdown("### Gerenciar Pontuação dos Sócios")
    col3, col4 = st.columns(2)

    # Adicionar Pontos
    with col3.expander("Adicionar Pontos"):
        query = "SELECT ID_Socio, Nome FROM Sócio"
        socios_df = run_query(query)
        socios = {row['Nome']: row['ID_Socio'] for _, row in socios_df.iterrows()}
        socio_pontuacao = st.selectbox("Selecione o Sócio para Adicionar Pontos", list(socios.keys()),
                                       key="add_points_socio")
        pontos = st.number_input("Quantidade de Pontos a Adicionar", min_value=0, step=1, key="add_points")

        if st.button("Adicionar Pontos", key="btn_add_points"):
            add_points_to_socio(socios[socio_pontuacao], pontos)

    # Remover Pontos
    with col4.expander("Remover Pontos"):
        query = "SELECT ID_Socio, Nome FROM Sócio"
        socios_df = run_query(query)
        socios = {row['Nome']: row['ID_Socio'] for _, row in socios_df.iterrows()}
        socio_pontuacao = st.selectbox("Selecione o Sócio para Remover Pontos", list(socios.keys()),
                                       key="remove_points_socio")
        pontos = st.number_input("Quantidade de Pontos a Remover", min_value=0, step=1, key="remove_points")

        if st.button("Remover Pontos", key="btn_remove_points"):
            remove_points_from_socio(socios[socio_pontuacao], pontos)

    # Seção de Gerenciar Ingressos
    st.markdown("### Gerenciamento de Ingressos")
    col5, col6, col7 = st.columns(3)

    # Adicionar Novo Jogo
    with col5.expander("Adicionar Novo Jogo"):
        socios_query = "SELECT ID_Socio, Nome FROM Sócio"
        socios_df = run_query(socios_query)
        socios = {row['Nome']: row['ID_Socio'] for _, row in socios_df.iterrows()}
        nome_socio = st.selectbox("Selecione o Sócio", list(socios.keys()), key="add_ingresso_socio")
        nome_jogo = st.text_input("Nome do Jogo", key="add_ingresso_nome_jogo")
        data_jogo = st.date_input("Data do Jogo", key="add_ingresso_data_jogo")
        desconto = st.slider("Desconto (%)", min_value=0, max_value=100, value=0, key="add_ingresso_desconto")

        if st.button("Adicionar Ingresso", key="add_ingresso_btn"):
            try:
                conn = connect_to_db()
                cursor = conn.cursor()
                query_add_ingresso = """
                    INSERT INTO Ingresso (Jogo, Data_jogo, Desconto, ID_Socio)
                    VALUES (%s, %s, %s, %s)
                """
                values = (nome_jogo, data_jogo, desconto / 100, socios[nome_socio])
                cursor.execute(query_add_ingresso, values)
                conn.commit()
                conn.close()
                st.success(f"Ingresso para o jogo '{nome_jogo}' adicionado com sucesso!")
            except Exception as e:
                st.error(f"Erro ao adicionar ingresso: {e}")

    # Editar Ingresso
    with col6.expander("Editar Ingresso Existente"):
        ingressos_query = "SELECT ID_Ingresso, Jogo FROM Ingresso"
        ingressos_df = run_query(ingressos_query)
        ingressos = {row['Jogo']: row['ID_Ingresso'] for _, row in ingressos_df.iterrows()}
        ingresso_selecionado = st.selectbox("Selecione o Ingresso para Editar", list(ingressos.keys()),
                                            key="edit_ingresso_select")

        novo_nome_jogo = st.text_input("Novo Nome do Jogo", value=ingresso_selecionado, key="edit_ingresso_nome_jogo")
        nova_data_jogo = st.date_input("Nova Data do Jogo", key="edit_ingresso_data_jogo")
        novo_desconto = st.slider("Novo Desconto (%)", min_value=0, max_value=100, value=0,
                                  key="edit_ingresso_desconto")

        if st.button("Salvar Alterações", key="edit_ingresso_btn"):
            try:
                conn = connect_to_db()
                cursor = conn.cursor()
                query_edit_ingresso = """
                    UPDATE Ingresso
                    SET Jogo = %s, Data_jogo = %s, Desconto = %s
                    WHERE ID_Ingresso = %s
                """
                values = (novo_nome_jogo, nova_data_jogo, novo_desconto / 100, ingressos[ingresso_selecionado])
                cursor.execute(query_edit_ingresso, values)
                conn.commit()
                conn.close()
                st.success(f"Ingresso '{novo_nome_jogo}' atualizado com sucesso!")
            except Exception as e:
                st.error(f"Erro ao atualizar ingresso: {e}")

    # Remover Ingresso
    with col7.expander("Remover Ingresso"):
        ingresso_remover = st.selectbox("Selecione o Ingresso para Remover", list(ingressos.keys()),
                                        key="remove_ingresso_select")

        if st.button("Remover Ingresso", key="remove_ingresso_btn"):
            try:
                conn = connect_to_db()
                cursor = conn.cursor()
                query_remove_ingresso = "DELETE FROM Ingresso WHERE ID_Ingresso = %s"
                cursor.execute(query_remove_ingresso, (ingressos[ingresso_remover],))
                conn.commit()
                conn.close()
                st.success(f"Ingresso '{ingresso_remover}' removido com sucesso!")
            except Exception as e:
                st.error(f"Erro ao remover ingresso: {e}")

    # Seção de Gerenciar Eventos
    st.markdown("### Gerenciamento de Eventos")
    col8, col9, col10 = st.columns(3)

    # Adicionar Novo Evento
    with col8.expander("Adicionar Novo Evento"):
        nome_evento = st.text_input("Nome do Evento", key="add_evento_nome")
        data_evento = st.date_input("Data do Evento", key="add_evento_data")
        localizacao = st.text_input("Localização", key="add_evento_local")
        capacidade = st.number_input("Capacidade Máxima", min_value=1, step=1, key="add_evento_capacidade")

        if st.button("Adicionar Evento", key="add_evento_btn"):
            try:
                conn = connect_to_db()
                cursor = conn.cursor()
                query_add_evento = """
                    INSERT INTO Evento_Exclusivo (Nome_evento, Data_evento, Localização, Capacidade)
                    VALUES (%s, %s, %s, %s)
                """
                values = (nome_evento, data_evento, localizacao, capacidade)
                cursor.execute(query_add_evento, values)
                conn.commit()
                conn.close()
                st.success(f"Evento '{nome_evento}' adicionado com sucesso!")
            except Exception as e:
                st.error(f"Erro ao adicionar evento: {e}")

    # Editar Evento Existente
    with col9.expander("Editar Evento Existente"):
        eventos_query = "SELECT ID_Evento, Nome_evento FROM Evento_Exclusivo"
        eventos_df = run_query(eventos_query)
        eventos = {row['Nome_evento']: row['ID_Evento'] for _, row in eventos_df.iterrows()}
        evento_selecionado = st.selectbox("Selecione o Evento para Editar", list(eventos.keys()), key="edit_evento_select")

        novo_nome_evento = st.text_input("Novo Nome do Evento", value=evento_selecionado, key="edit_evento_nome")
        nova_data_evento = st.date_input("Nova Data do Evento", key="edit_evento_data")
        nova_localizacao = st.text_input("Nova Localização", key="edit_evento_local")
        nova_capacidade = st.number_input("Nova Capacidade Máxima", min_value=1, step=1, key="edit_evento_capacidade")

        if st.button("Salvar Alterações", key="edit_evento_btn"):
            try:
                conn = connect_to_db()
                cursor = conn.cursor()
                query_edit_evento = """
                    UPDATE Evento_Exclusivo
                    SET Nome_evento = %s, Data_evento = %s, Localização = %s, Capacidade = %s
                    WHERE ID_Evento = %s
                """
                values = (novo_nome_evento, nova_data_evento, nova_localizacao, nova_capacidade, eventos[evento_selecionado])
                cursor.execute(query_edit_evento, values)
                conn.commit()
                conn.close()
                st.success(f"Evento '{novo_nome_evento}' atualizado com sucesso!")
            except Exception as e:
                st.error(f"Erro ao atualizar evento: {e}")

    # Remover Evento
    with col10.expander("Remover Evento"):
        evento_remover = st.selectbox("Selecione o Evento para Remover", list(eventos.keys()), key="remove_evento_select")

        if st.button("Remover Evento", key="remove_evento_btn"):
            try:
                conn = connect_to_db()
                cursor = conn.cursor()
                query_remove_evento = "DELETE FROM Evento_Exclusivo WHERE ID_Evento = %s"
                cursor.execute(query_remove_evento, (eventos[evento_remover],))
                conn.commit()
                conn.close()
                st.success(f"Evento '{evento_remover}' removido com sucesso!")
            except Exception as e:
                st.error(f"Erro ao remover evento: {e}")

    # Seção de Adicionar Sócios a Eventos
    st.markdown("### Gerenciar Participação em Eventos")
    col11, col12 = st.columns(2)

    # Adicionar Sócio a um Evento
    with col11.expander("Adicionar Sócio a um Evento"):
        # Consultar eventos disponíveis
        eventos_query = "SELECT ID_Evento, Nome_evento FROM Evento_Exclusivo"
        eventos_df = run_query(eventos_query)
        eventos = {row['Nome_evento']: row['ID_Evento'] for _, row in eventos_df.iterrows()}
        evento_selecionado = st.selectbox("Selecione o Evento", list(eventos.keys()), key="add_socio_evento_select")

        # Consultar sócios disponíveis
        socios_query = "SELECT ID_Socio, Nome FROM Sócio"
        socios_df = run_query(socios_query)
        socios = {row['Nome']: row['ID_Socio'] for _, row in socios_df.iterrows()}
        socio_selecionado = st.selectbox("Selecione o Sócio", list(socios.keys()), key="add_socio_select")

        # Data de inscrição
        data_inscricao = st.date_input("Data de Inscrição", key="add_socio_evento_data")

        if st.button("Adicionar Sócio ao Evento", key="add_socio_evento_btn"):
            try:
                conn = connect_to_db()
                cursor = conn.cursor()
                query_add_participacao = """
                    INSERT INTO Participacao_Evento (ID_Socio, ID_Evento, Data_inscricao)
                    VALUES (%s, %s, %s)
                """
                values = (socios[socio_selecionado], eventos[evento_selecionado], data_inscricao)
                cursor.execute(query_add_participacao, values)
                conn.commit()
                conn.close()
                st.success(f"Sócio '{socio_selecionado}' adicionado ao evento '{evento_selecionado}' com sucesso!")
            except Exception as e:
                st.error(f"Erro ao adicionar sócio ao evento: {e}")

    # Remover Sócio de um Evento
    with col12.expander("Remover Sócio de um Evento"):
        # Consultar participações existentes
        participacao_query = """
            SELECT pe.ID_Socio, s.Nome AS Nome_Socio, ee.Nome_evento
            FROM Participacao_Evento pe
            JOIN Sócio s ON pe.ID_Socio = s.ID_Socio
            JOIN Evento_Exclusivo ee ON pe.ID_Evento = ee.ID_Evento
        """
        participacao_df = run_query(participacao_query)

        if not participacao_df.empty:
            participacoes = {f"{row['Nome_Socio']} - {row['Nome_evento']}": (row['ID_Socio'], row['Nome_evento'])
                             for _, row in participacao_df.iterrows()}
            participacao_selecionada = st.selectbox("Selecione a Participação para Remover", list(participacoes.keys()),
                                                    key="remove_socio_evento_select")

            if st.button("Remover Participação", key="remove_socio_evento_btn"):
                try:
                    socio_id, evento_nome = participacoes[participacao_selecionada]
                    evento_id_query = "SELECT ID_Evento FROM Evento_Exclusivo WHERE Nome_evento = %s"
                    conn = connect_to_db()
                    cursor = conn.cursor()
                    cursor.execute(evento_id_query, (evento_nome,))
                    evento_id = cursor.fetchone()[0]

                    query_remove_participacao = """
                        DELETE FROM Participacao_Evento
                        WHERE ID_Socio = %s AND ID_Evento = %s
                    """
                    cursor.execute(query_remove_participacao, (socio_id, evento_id))
                    conn.commit()
                    conn.close()
                    st.success(f"Participação de '{participacao_selecionada}' removida com sucesso!")
                except Exception as e:
                    st.error(f"Erro ao remover participação: {e}")
        else:
            st.info("Nenhuma participação encontrada para remoção.")

with tabs[8]:
    st.subheader("Busca Específica")

    tipo_busca = st.selectbox(
        "Selecione o tipo de busca",
        ["Sócio", "Ingresso", "Evento", "Pagamento", "Benefício"]
    )

    if tipo_busca == "Sócio":
        st.markdown("#### Buscar Sócio")
        termo_socio = st.text_input("Digite o nome, e-mail ou CPF do sócio para buscar:")
        if st.button("Buscar Sócio"):
            query = """
                SELECT s.Nome, s.Email, s.CPF, s.Telefone, s.Data_adesao, s.Pontos_socio, p.Nome_Plano
                FROM Sócio s
                JOIN Plano p ON s.ID_Plano = p.ID_Plano
                WHERE s.Nome LIKE %s OR s.Email LIKE %s OR s.CPF LIKE %s
            """
            socios_resultado = run_query(query, (f"%{termo_socio}%", f"%{termo_socio}%", f"%{termo_socio}%"))
            if not socios_resultado.empty:
                socios_resultado.index = socios_resultado.index + 1
                st.dataframe(socios_resultado)
            else:
                st.info("Nenhum sócio encontrado.")

    elif tipo_busca == "Ingresso":
        st.markdown("#### Buscar Ingresso")
        termo_ingresso = st.text_input("Digite o nome do sócio ou jogo para buscar o ingresso:")
        if st.button("Buscar Ingresso"):
            query = """
                SELECT s.Nome AS Nome_Socio, i.Jogo, i.Data_jogo, i.Desconto
                FROM Ingresso i
                JOIN Sócio s ON i.ID_Socio = s.ID_Socio
                WHERE s.Nome LIKE %s OR i.Jogo LIKE %s
            """
            ingressos_resultado = run_query(query, (f"%{termo_ingresso}%", f"%{termo_ingresso}%"))
            if not ingressos_resultado.empty:
                ingressos_resultado.index = ingressos_resultado.index + 1
                st.dataframe(ingressos_resultado)
            else:
                st.info("Nenhum ingresso encontrado.")

    elif tipo_busca == "Evento":
        st.markdown("#### Buscar Evento")
        termo_evento = st.text_input("Digite o nome do evento ou nome do sócio para buscar o evento:")
        if st.button("Buscar Evento"):
            query = """
                SELECT ee.Nome_evento, ee.Data_evento, s.Nome AS Nome_Socio, pe.Data_inscricao
                FROM Evento_Exclusivo ee
                JOIN Participacao_Evento pe ON ee.ID_Evento = pe.ID_Evento
                JOIN Sócio s ON pe.ID_Socio = s.ID_Socio
                WHERE ee.Nome_evento LIKE %s OR s.Nome LIKE %s
            """
            eventos_resultado = run_query(query, (f"%{termo_evento}%", f"%{termo_evento}%"))
            if not eventos_resultado.empty:
                eventos_resultado.index = eventos_resultado.index + 1
                st.dataframe(eventos_resultado)
            else:
                st.info("Nenhum evento encontrado.")

    elif tipo_busca == "Pagamento":
        st.markdown("#### Buscar Pagamento")
        termo_pagamento = st.text_input("Digite o nome do sócio ou método de pagamento:")
        if st.button("Buscar Pagamento"):
            query = """
                SELECT s.Nome AS Nome_Socio, p.Data_pagamento, p.Valor_pago, p.Metodo_pagamento, p.Status_pagamento
                FROM Pagamento p
                JOIN Sócio s ON p.ID_Socio = s.ID_Socio
                WHERE s.Nome LIKE %s OR p.Metodo_pagamento LIKE %s
            """
            pagamentos_resultado = run_query(query, (f"%{termo_pagamento}%", f"%{termo_pagamento}%"))
            if not pagamentos_resultado.empty:
                pagamentos_resultado.index = pagamentos_resultado.index + 1
                st.dataframe(pagamentos_resultado)
            else:
                st.info("Nenhum pagamento encontrado.")

    elif tipo_busca == "Benefício":
        st.markdown("#### Buscar Benefício")
        termo_beneficio = st.text_input("Digite o tipo de benefício ou descrição:")
        if st.button("Buscar Benefício"):
            query = """
                SELECT b.Tipo_Beneficio, b.Pontos_necessarios, b.Descrição, pb.ID_Plano
                FROM Benefício b
                JOIN Plano_Beneficio pb ON b.ID_Beneficio = pb.ID_Beneficio
                WHERE b.Tipo_Beneficio LIKE %s OR b.Descrição LIKE %s
            """
            beneficios_resultado = run_query(query, (f"%{termo_beneficio}%", f"%{termo_beneficio}%"))
            if not beneficios_resultado.empty:
                beneficios_resultado.index = beneficios_resultado.index + 1
                st.dataframe(beneficios_resultado)
            else:
                st.info("Nenhum benefício encontrado.")



