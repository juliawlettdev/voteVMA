from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

# Função para gerar um e-mail aleatório
def gerar_email_aleatorio():
    # Gerando uma string aleatória de letras de a a z com 10 caracteres
    nome_email = ''.join(random.choices(string.ascii_lowercase, k=10))
    return f"{nome_email}@gmail.com"

# Inicia o navegador Chrome
navegador = webdriver.Chrome()

# Acessa a página
navegador.get("https://www.mtv.com/event/vma/vote/best-k-pop")

# Aguarda a página carregar completamente
time.sleep(2)

# Variável para o contador, começando com 0
contador = 0

# Loop infinito
while True:
    print(f"Rodada {contador}: Iniciando ciclo...")

    # Localiza todos os elementos com a classe "chakra-button css-1cqntny"
    botoes = navegador.find_elements(By.CSS_SELECTOR, ".chakra-button.css-1cqntny")

    # Verifica se há pelo menos 6 botões na página
    if len(botoes) >= 6:
        # Seleciona o sexto botão (índice 5)
        botao_sexto = botoes[5]
        
        # Realiza 20 cliques no sexto botão
        for _ in range(20):
            botao_sexto.click()
            time.sleep(1)  # Intervalo de 1 segundo entre os cliques

            # Aguarda o modal abrir (ajuste o tempo de espera conforme necessário)
            time.sleep(2)
            
            # Gera um e-mail aleatório
            email = gerar_email_aleatorio()
            print(f"E-mail gerado: {email}")
            
            # Localiza o campo de input de e-mail dentro do modal
            try:
                input_email = navegador.find_element(By.NAME, "user_email")
                
                # Preenche o campo de e-mail com o e-mail gerado
                input_email.clear()  # Limpa o campo antes de inserir o e-mail
                input_email.send_keys(email)
                print(f"E-mail inserido no campo: {email}")
            except Exception as e:
                print(f"Erro ao localizar o campo de e-mail: {e}")
                
            # Localiza o botão de envio após inserir o e-mail e clica
            try:
                botao_enviar = navegador.find_element(By.CSS_SELECTOR, ".chakra-button.css-1r4lbh0")
                botao_enviar.click()
                print("Botão de envio clicado.")
            except Exception as e:
                print(f"Erro ao localizar o botão de envio: {e}")

            # Aguarda um pouco antes de continuar ou realizar outras ações (se necessário)
            time.sleep(2)

            # Aqui vamos esperar o modal fechar ou a página atualizar
            # Se necessário, adicionar um tempo para garantir que a página tenha sido recarregada
            time.sleep(3)

            # Encontrar o décimo botão com a classe "chakra-button css-1cqntny" novamente
            botoes = navegador.find_elements(By.CSS_SELECTOR, ".chakra-button.css-1cqntny")

            # Verifica se há pelo menos 10 botões
            if len(botoes) >= 10:
                # Seleciona o décimo botão (índice 9)
                botao_decimo = botoes[9]
                
                # Realiza 20 cliques no décimo botão
                for _ in range(20):
                    botao_decimo.click()
                    time.sleep(1)  # Intervalo de 1 segundo entre os cliques
            else:
                print("Não há 10 botões com a classe especificada na página.")
            
            # Aguarda a abertura do modal após os 20 cliques
            time.sleep(3)
            
            # Localiza o botão com a classe "chakra-button css-ufo2k5" e clica nele
            try:
                # Usamos WebDriverWait para aguardar o botão ficar clicável
                botao_modal = WebDriverWait(navegador, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".chakra-button.css-ufo2k5"))
                )
                botao_modal.click()
                print("Botão do modal clicado.")
            except Exception as e:
                print(f"Erro ao localizar ou clicar no botão do modal: {e}")

            # Aguarda o fechamento do modal antes de clicar no próximo botão
            time.sleep(3)

            # Tenta fechar o modal após o clique
            try:
                # Procuramos por um botão de fechar do modal (ajuste conforme a implementação do seu site)
                botao_fechar_modal = WebDriverWait(navegador, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".chakra-modal__close-btn"))
                )
                botao_fechar_modal.click()
                print("Modal fechado.")
            except Exception as e:
                print(f"Erro ao tentar fechar o modal: {e}")
            
            # Aguarda 2 minutos antes de clicar no próximo botão, dando tempo para inspeção
            print("Esperando 2 minutos antes de clicar no botão de login...")
            time.sleep(120)  # Espera 2 minutos (120 segundos)

            # Agora, clica no botão de login com a classe "chakra-button AuthNav__login-btn css-ki1yvo"
            try:
                botao_login = WebDriverWait(navegador, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".chakra-button.AuthNav__login-btn.css-ki1yvo"))
                )
                botao_login.click()
                print("Botão de login clicado.")
            except Exception as e:
                print(f"Erro ao localizar o botão de login: {e}")
            
        # Incrementa o contador em 19
        contador += 19
        print(f"Contador após incremento: {contador}")
        
        # Adicione um tempo de espera entre os loops, caso queira evitar sobrecarregar a página
        time.sleep(10)

    else:
        print("Não há 6 botões com a classe especificada na página.")

# Fecha o navegador após os cliques e ações (embora o loop seja infinito, este código nunca será alcançado)
navegador.quit()
