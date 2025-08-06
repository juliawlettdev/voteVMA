from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import time
import random
import string
import os
from datetime import datetime

def gerar_email_aleatorio():
    nome_email = ''.join(random.choices(string.ascii_lowercase, k=10))
    return f"{nome_email}@gmail.com"

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
                for _ in range(20):
                    botao_decimo.click()
                    time.sleep(1)
                contador += 20
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

                    # Aguarda o atributo aria-expanded mudar para "true"
                    WebDriverWait(navegador, 10).until(
                        lambda driver: accordion_botao.get_attribute("aria-expanded") == "true"
                    )
                    print("Accordion expandido.")

                    # Captura o 14º elemento (índice 13)
                    elementos_accordion = WebDriverWait(navegador, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".chakra-accordion__item.css-pnnn2f"))
                    )
                    if len(elementos_accordion) >= 14:
                        elemento_para_print = elementos_accordion[13]
                    else:
                        raise Exception(f"Esperado ao menos 14 elementos, mas encontrados {len(elementos_accordion)}")

                    navegador.execute_script("""
                        arguments[0].style.maxHeight = 'none';
                        arguments[0].style.overflow = 'visible';
                    """, elemento_para_print)

                    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento_para_print)
                    time.sleep(1)

                    # Captura o QUINTO elemento com classe css-0 dentro do accordion
                    elementos_css0 = elemento_para_print.find_elements(By.CSS_SELECTOR, ".css-0")
                    if len(elementos_css0) >= 5:
                        quinto_elemento = elementos_css0[4]
                        navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", quinto_elemento)
                        time.sleep(1)

                        caminho_captura = r"D:\\capturaVmaLisa"
                        if not os.path.exists(caminho_captura):
                            os.makedirs(caminho_captura)
                        nome_arquivo = f"css0_5_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                        caminho_completo = os.path.join(caminho_captura, nome_arquivo)
                        quinto_elemento.screenshot(caminho_completo)
                        print(f"Print do 5º .css-0 salvo em: {caminho_completo}")
                    else:
                        print(f"Menos de 5 elementos com classe .css-0 encontrados: {len(elementos_css0)}")

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
