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

# Ciclo único
print(f"Rodada {contador}: Iniciando ciclo...")

# Localiza todos os elementos com a classe "chakra-button css-1cqntny"
botoes = navegador.find_elements(By.CSS_SELECTOR, ".chakra-button.css-1cqntny")

# Verifica se há pelo menos 10 botões na página
if len(botoes) >= 10:
    # Seleciona o décimo botão (índice 9)
    botao_decimo = botoes[9]

    # Oculta o elemento sobreposto (por exemplo, o menu ou outro elemento)
    navegador.execute_script("document.querySelector('.chakra-stack.css-w5nh5y').style.display = 'none';")
    
    # Realiza 15 cliques no décimo botão
    for _ in range(1):
        botao_decimo.click()
        time.sleep(1)  # Intervalo de 1 segundo entre os cliques

        # Aguarda o modal abrir (ajuste o tempo de espera conforme necessário)
        time.sleep(2)

        # Quando o modal aparecer, altere o data-focus-lock-disabled e o tabindex
        try:
            modal_content = WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".chakra-modal__content-container"))
            )

            # Verifica se o tabindex é -1 e o altera para 1
            tabindex = modal_content.get_attribute("tabindex")
            if tabindex == "-1":
                # Altera o tabindex para 1
                navegador.execute_script("arguments[0].setAttribute('tabindex', '1');", modal_content)
                print("tabindex alterado para 1.")

            # Altera o data-focus-lock-disabled para "true"
            navegador.execute_script("arguments[0].setAttribute('data-focus-lock-disabled', 'true');", modal_content)
            print("data-focus-lock-disabled alterado para 'true'.")

        except Exception as e:
            print(f"Erro ao tentar alterar o modal: {e}")

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

            # Realiza 15 cliques no décimo botão novamente
            for _ in range(19):
                botao_decimo.click()
                time.sleep(1)  # Intervalo de 1 segundo entre os cliques
        else:
            print("Não há 10 botões com a classe especificada na página.")

        # Aguarda a abertura do modal após os 15 cliques
        time.sleep(3)

    # Após os 15 cliques no décimo botão, clica no botão com a classe "chakra-button css-1tz6b2b"
    try:
        botao_chakra_1tz6b2b = navegador.find_element(By.CSS_SELECTOR, ".chakra-button.css-1tz6b2b")
        
        # Rola até o botão antes de clicar
        navegador.execute_script("arguments[0].scrollIntoView();", botao_chakra_1tz6b2b)
        time.sleep(1)  # Aguarda um pouco para garantir que o botão está visível
        
        # Tenta clicar no botão
        botao_chakra_1tz6b2b.click()
        print("Botão chakra-button css-1tz6b2b clicado.")
    except Exception as e:
        print(f"Erro ao localizar o botão chakra-button css-1tz6b2b: {e}")

else:
    print("Não há 10 botões com a classe especificada na página.")

# Aqui o código ficará parado após o ciclo
print("Finalizando o ciclo. O código agora ficará parado.")
# O navegador permanece aberto para inspeção manual ou outras ações
# navegador.quit()
