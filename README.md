# 🗳️ VMA Voting Bot - Best K-Pop (MTV)

Este é um script de automação desenvolvido com **Python** e **Selenium** para automatizar votos na categoria **Best K-Pop** do evento MTV VMA.

> ⚠️ Uso exclusivo para fins educacionais e testes. O uso indevido pode violar termos de uso do site.

---

## 📌 Funcionalidades

- Geração de e-mails aleatórios mais realistas (nome.sobrenome + número) para validar votos  
- Votação automática com opção de 10 ou 20 cliques por rodada ("modo normal" e "POWER VOTE")  
- Interação com modais e elementos dinâmicos usando JavaScript para garantir funcionalidade  
- Captura automática de screenshot da tela inteira, focando no 5º elemento `.css-0` do accordion expandido  
- Execução contínua em loop, com possibilidade de encerrar ao pressionar `ENTER`  
- Salvamento automático das capturas em `C:\CapturaTelaVMA` (pasta criada automaticamente, se não existir)
---

## 🧰 Requisitos

- Python 3.8 ou superior  
- Google Chrome instalado  
- ChromeDriver compatível com a versão do seu Chrome (https://chromedriver.chromium.org/downloads)  
- Adicionar o ChromeDriver ao PATH do sistema ou informar caminho no script  

### Instalação de dependências

Execute o comando:

```bash
pip install selenium mss
```

---

## 🚀 Como usar

1. Certifique-se de ter o Chrome e o ChromeDriver instalados e configurados corretamente.  
2. Clone ou copie o script para seu computador.  
3. Execute o script Python:  
   ```bash
   python seu_script.py
   ```  
4. Escolha o modo de votação:  
   - Digite `P` para **POWER VOTE** (20 cliques por voto)  
   - Ou aperte `ENTER` para modo normal (10 cliques por voto)  
5. Para parar o script, pressione `ENTER` a qualquer momento.  

---

## 📂 Local das screenshots

As capturas de tela serão salvas em:

```
C:\CapturaTelaVMA
```

## 📌 Avisos

- O script foi desenvolvido para aprendizado e testes locais.  
- Respeite sempre as regras do site para evitar bloqueios.  
- O uso em massa ou abusivo pode ser identificado e bloqueado.
