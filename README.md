# Crazy Nave 🚀

Um jogo de nave estilo *Space Invaders*, desenvolvido em Python com a biblioteca Pygame como projeto para a disciplina de Programação Orientada a Objetos.
Membros: @RaulSuzuki, @RafaelFerreira e @DiegoFelipe

O nome é uma homenagem à música **"Crazy Train" de Ozzy Osbourne**, a eletrizante trilha sonora que acompanha o gameplay!

## Funcionalidades Principais

- **Jogabilidade Clássica:** Desvie dos projéteis e destrua hordas de inimigos para sobreviver.
- **Trilha Sonora Eletrizante:** Ação embalada pelo som de "Crazy Train".
- **Inimigo Inteligente:** Cuidado com o Alien especial! Ele não segue um padrão fixo e seus movimentos são pensados para te desafiar.

## Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Game-Project-OO/Game-Project.git](https://github.com/Game-Project-OO/Game-Project.git)
    ```
2.  **Acesse a pasta do projeto:**
    ```bash
    cd Game-Project
    ```
3.  **Instale as dependências (Pygame):**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Execute o arquivo principal:**
    ```bash
    python main.py
    ```

## Conceitos de Programação Orientada a Objetos Aplicados

O projeto foi 100% estruturado com base nos pilares da Programação Orientada a Objetos para garantir um código limpo, modular e reutilizável.

### Classes
Toda a estrutura do jogo é baseada em classes. Cada entidade, como a nave do jogador, os inimigos e os projéteis, é representada por um objeto, que encapsula seus próprios dados (atributos) e comportamentos (métodos).

* **Exemplos:** `Player`, `Alien`, `Laser`, e a classe principal `Jogo` que orquestra todo o funcionamento.

### Herança
Utilizamos herança para reaproveitar código e criar especializações. Todos os inimigos, por exemplo, derivam de uma classe base que contém os atributos e métodos comuns, os power ups, inclusive, herdam de uma classe abstrata base.

* **Exemplo Prático:** A classe `AlienRicochete` herda da classe `Alien`, reutilizando métodos como `define_alvo()` e `update()`.

### Classes Abstratas
Para definir um "contrato" que todas as entidades do jogo devem seguir, usamos classes abstratas. Isso garante que qualquer personagem ou objeto na tela implemente os métodos essenciais para o funcionamento do jogo.

* **Exemplo Prático:** Uma classe abstrata `PowerUps` define os métodos `powerups_update()`, `destruir()` e `efeito()` forçando todas as classes filhas (como `Cura`, `Escudo` e `Vida`) a implementarem sua própria lógica de atualização de estado e renderização.

### Composição e Agregação
As relações entre os objetos foram modeladas com composição e agragação para criar sistemas coesos e desacoplados.

* **Composição:** A classe `Jogador` possui um objeto `Laser` como atributo. A arma é parte essencial do jogador e seu ciclo de vida está atrelado ao dele (se a nave é destruída, a arma também é).
* **Agregação:** A classe `Jogo` gerencia uma lista de `Alien`. Os aliens existem como objetos independentes e são adicionados ou removidos da lista de forma dinâmica, sem que a existência de um dependa da existência do outro.

### Tratamento de Exceções
Para tornar o jogo mais robusto e à prova de falhas, o código utiliza blocos `try...except` para lidar com erros que poderiam interromper a execução, como o carregamento de arquivos externos.

* **Exemplo Prático:** Ao carregar o ranking que é um arquivo `(.txt)`, o código é envolvido por um `try...except FileNotFoundError`. Caso o arquivo não seja encontrado, o jogo continua sem abrir o arquivo.

## O Alien Inteligente: Um Desafio a Mais!

Um dos destaques do **Crazy Nave** é o **Alien Inteligente**. Enquanto os inimigos comuns se movem em formação, este adversário foi projetado para quebrar padrões:

* **Rastreia o Jogador:** Ele analisa a posição da nave do jogador (eixo X) para ajustar sua movimentação e se posicionar de forma estratégica.
* **Movimento Não Linear:** Sua trajetória é menos previsível, tornando-o um alvo mais difícil e um perigo constante.
* **Desafio Tático:** Ele força o jogador a se movimentar constantemente e a não depender de pontos seguros na tela, aumentando a dificuldade e a diversão.
