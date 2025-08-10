from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import time
import random
import os
from datetime import datetime
import mss  # Biblioteca para screenshot da tela inteira

# Listas maiores de nomes e sobrenomes
nomes = [
    "ana", "carlos", "mariana", "joao", "luiza", "pedro", "juliana", "rafael",
    "marcos", "beatriz", "fernanda", "bruno", "camila", "diego", "elaine", "felipe",
    "gabriela", "henrique", "isabela", "joana", "kelly", "lucas", "marcia", "natalia",
    "oliveira", "paulo", "quiteria", "ricardo", "sandra", "tiago", "vanessa", "walter",
    "xavier", "yara", "zeca", "adriana", "alexandre", "alessandra", "amanda", "anderson",
    "andrea", "antonio", "artur", "augusto", "barbara", "bernardo", "bianca", "brenda",
    "caio", "camilly", "claudia", "cleber", "daniel", "daniela", "debora", "diego",
    "eduardo", "elena", "elis", "eloisa", "emily", "erica", "fabio", "felipe",
    "fernando", "flavia", "gabriel", "giovanna", "gustavo", "helena", "igor", "iris",
    "isadora", "jessica", "joaquim", "jose", "julia", "julio", "keila", "kenia",
    "laura", "leandro", "leonardo", "leticia", "lilian", "lorena", "lucas", "luiza",
    "luiz", "marcelo", "marcia", "maria", "marina", "mario", "matheus", "michele",
    "miguel", "monica", "natasha", "nicolas", "patricia", "paula", "pedro", "rafaela",
    "rafael", "renata", "ricardo", "roberto", "rodrigo", "samuel", "sandra", "sara",
    "sergio", "silvia", "simone", "sofia", "sueli", "thiago", "valentina", "victor",
    "victoria", "vinicius", "vivian", "wallace", "wesley", "william", "yuri", "zoe",
    "adriano", "alicia", "aline", "ana", "andrea", "augusto", "beatriz", "caio"
]

sobrenomes = [
    "silva", "souza", "oliveira", "pereira", "almeida", "rodrigues", "fernandes",
    "gomes", "martins", "barbosa", "santos", "dias", "melo", "costa", "araujo",
    "freitas", "carvalho", "lima", "moura", "rocha", "ribeiro", "teixeira", "pires",
    "rezende", "farias", "tavares", "assis", "marques", "campos", "dias", "vieira",
    "alves", "cardoso", "da silva", "dos santos", "de souza", "mendes", "medeiros",
    "cavalcante", "monteiro", "brito", "ramos", "vieira", "barros", "correa",
    "siqueira", "araujo", "batista", "machado", "pereira", "pinto", "albuquerque",
    "fonseca", "teixeira", "costa", "rodrigues", "faria", "tavares", "rodrigues",
    "freitas", "moraes", "guimaraes", "camargo", "araujo", "ferreira", "lopes",
    "barbosa", "costa", "marques", "perez", "pereira", "castro", "cunha", "moraes",
    "dantas", "araujo", "rodrigues", "ferreira", "gomes", "alves", "santana",
    "campos", "bastos", "lima", "dias", "batista", "pereira", "santos", "melo",
    "carvalho", "brito", "franco", "castro", "freitas", "almeida", "pacheco",
    "torres", "soares", "machado", "alves", "mendes", "rodrigues", "rocha", "silveira",
    "santos", "costa", "gomes", "oliveira", "pires", "fernandes", "rodrigues",
    "pinto", "moura", "tavares", "alves", "pires", "melo", "gomes", "batista", "pires",
    "siqueira", "assis", "carvalho", "freitas", "dias", "lopes", "albuquerque",
    "pereira", "moraes", "ramos", "soares", "guimaraes", "fernandes", "torres",
    "ribeiro", "castro"
]

def gerar_email_aleatorio():
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    numero = random.randint(1, 9999)
    return f"{nome}.{sobrenome}{numero}@gmail.com"

# ==========================
# Escolha do modo de execução
# ==========================
modo = input("Digite 'P' para POWER VOTE (20 cliques) ou ENTER para modo normal (10 cliques): ").strip().upper()
cliques_por_voto = 20 if modo == "P" else 10
print(f"Modo selecionado: {'POWER VOTE' if cliques_por_voto == 20 else 'NORMAL'} - {cliques_por_voto} cliques por voto.\n")

# Flag de controle para parar o loop
parar_execucao = False

def aguardar_enter():
    global parar_execucao
    input("Pressione ENTER a qualquer momento para encerrar o script...\n")
    parar_execucao = True

# Inicia o navegador Chrome
navegador = webdriver.Chrome()

# Inicia thread para escutar o Enter sem travar o código
threading.Thread(target=aguardar_enter, daemon=True).start()

contador = 0

while not parar_execucao:
    try:
        navegador.get("https://www.mtv.com/event/vma/vote/best-k-pop")

        WebDriverWait(navegador, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".chakra-button.css-1cqntny"))
        )

        print(f"\nRodada atual: +{contador} votos")
        botoes = navegador.find_elements(By.CSS_SELECTOR, ".chakra-button.css-1cqntny")

        if len(botoes) >= 10:
            botao_decimo = botoes[9]

            navegador.execute_script("document.querySelector('.chakra-stack.css-w5nh5y')?.style?.setProperty('display', 'none');")
            botao_decimo.click()
            time.sleep(1)

            try:
                modal_content = WebDriverWait(navegador, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".chakra-modal__content-container"))
                )
                tabindex = modal_content.get_attribute("tabindex")
                if tabindex == "-1":
                    navegador.execute_script("arguments[0].setAttribute('tabindex', '1');", modal_content)
                navegador.execute_script("arguments[0].setAttribute('data-focus-lock-disabled', 'true');", modal_content)
            except Exception as e:
                print(f"Erro ao ajustar o modal: {e}")

            email = gerar_email_aleatorio()
            print(f"E-mail gerado: {email}")

            try:
                input_email = WebDriverWait(navegador, 10).until(
                    EC.presence_of_element_located((By.NAME, "user_email"))
                )
                input_email.clear()
                input_email.send_keys(email)
            except Exception as e:
                print(f"Erro ao localizar campo de e-mail: {e}")

            try:
                botao_enviar = WebDriverWait(navegador, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".chakra-button.css-1r4lbh0"))
                )
                botao_enviar.click()
            except Exception as e:
                print(f"Erro ao clicar em enviar: {e}")

            try:
                WebDriverWait(navegador, 10).until(
                    EC.invisibility_of_element_located((By.CSS_SELECTOR, ".chakra-modal__content-container"))
                )
            except:
                pass

            botoes = navegador.find_elements(By.CSS_SELECTOR, ".chakra-button.css-1cqntny")
            if len(botoes) >= 10:
                botao_decimo = botoes[9]
                for _ in range(cliques_por_voto):  # Usa o modo escolhido (10 ou 20 cliques)
                    botao_decimo.click()
                    time.sleep(1)
                contador += cliques_por_voto
            else:
                print("Botões insuficientes.")

            portais = navegador.find_elements(By.CSS_SELECTOR, ".chakra-portal")
            for portal_div in portais:
                try:
                    focus_lock_divs = portal_div.find_elements(By.CSS_SELECTOR, "[data-focus-lock-disabled]")
                    if not focus_lock_divs:
                        continue

                    focus_lock_div = focus_lock_divs[0]
                    navegador.execute_script("arguments[0].setAttribute('data-focus-lock-disabled', 'true');", focus_lock_div)

                    try:
                        botao_submit = focus_lock_div.find_element(By.CSS_SELECTOR, "button.chakra-button.css-ufo2k5")
                        navegador.execute_script("arguments[0].scrollIntoView(true);", botao_submit)
                        WebDriverWait(navegador, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-ufo2k5")))
                        botao_submit.click()
                        print("Botão Submit clicado.")
                        break
                    except Exception as e:
                        print(f"Erro ao clicar no botão Submit: {e}")
                except Exception as e:
                    print(f"Erro ao processar portal: {e}")

            try:
                WebDriverWait(navegador, 10).until(
                    EC.invisibility_of_element_located((By.CSS_SELECTOR, ".chakra-modal__content-container"))
                )

                # Clique no botão do accordion pelo ID com MouseEvent
                try:
                    accordion_botao = WebDriverWait(navegador, 5).until(
                        EC.presence_of_element_located((By.ID, "accordion-button-best-k-pop"))
                    )
                    click_script = """
                        var evt = new MouseEvent('click', {
                            bubbles: true,
                            cancelable: true,
                            view: window
                        });
                        arguments[0].dispatchEvent(evt);
                    """
                    navegador.execute_script(click_script, accordion_botao)
                    print("Accordion [best-k-pop] clique via MouseEvent disparado.")

                    WebDriverWait(navegador, 10).until(
                        lambda driver: accordion_botao.get_attribute("aria-expanded") == "true"
                    )
                    print("Accordion expandido.")

                    elementos_accordion = WebDriverWait(navegador, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".chakra-accordion__item.css-pnnn2f"))
                    )
                    if len(elementos_accordion) >= 14:
                        elemento_para_focar = elementos_accordion[13]
                    else:
                        raise Exception(f"Esperado ao menos 14 elementos, mas encontrados {len(elementos_accordion)}")

                    # Scroll para o 14º elemento
                    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento_para_focar)
                    time.sleep(1)

                    # Dentro do 14º item, pegar o quinto elemento .css-0
                    elementos_css0 = elemento_para_focar.find_elements(By.CSS_SELECTOR, ".css-0")
                    if len(elementos_css0) >= 5:
                        quinto_elemento = elementos_css0[4]
                    else:
                        raise Exception(f"Esperado ao menos 5 elementos .css-0, mas encontrados {len(elementos_css0)}")

                    # Scroll para o quinto elemento
                    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", quinto_elemento)
                    time.sleep(1)

                    # Ajuste para expandir o quinto elemento para mostrar tudo
                    navegador.execute_script("""
                        arguments[0].style.maxHeight = 'none';
                        arguments[0].style.overflow = 'visible';
                    """, quinto_elemento)

                    # Caminho para salvar a screenshot da tela inteira com mss
                    caminho_captura = r"C:\\CapturaTelaVMA"
                    if not os.path.exists(caminho_captura):
                        os.makedirs(caminho_captura)
                    nome_arquivo = f"screenshot_full_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                    caminho_completo = os.path.join(caminho_captura, nome_arquivo)

                    # Captura da tela inteira usando mss
                    with mss.mss() as sct:
                        sct.shot(output=caminho_completo)
                    print(f"Screenshot da tela inteira salvo em: {caminho_completo}")

                except Exception as e:
                    print(f"Erro ao clicar, expandir ou tirar print do accordion: {e}")

                navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                botao_login = WebDriverWait(navegador, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.AuthNav__login-btn.css-ki1yvo"))
                )
                botao_login.click()
                print("Botão de login clicado.")
            except Exception as e:
                print(f"Erro no pós-submit: {e}")

        else:
            print("Botões não suficientes encontrados.")

        print(f"----------------------- Total de votos acumulados: {contador} -----------------------")

    except Exception as erro_geral:
        print(f"Erro geral na rodada: {erro_geral}")

input("Pressione ENTER para sair...")
print("Script finalizado manualmente.")

