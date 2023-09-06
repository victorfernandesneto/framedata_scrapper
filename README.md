# # webscrapperv2

## Descrição do projeto

### Motivação

Jogos de luta, além de mecanicamente desafiadores, nos impõe constantes *knowledge checks*. A *CAPCOM* disponibilizou, em seu [site](https://www.streetfighter.com/6/character), uma tabela para cada personagem de STREET FIGHTER 6 que contém informações cruciais sobre seus golpes, onde medimos desde quanto tempo ele demora para sair a quanto de barra ele enche caso acerte. Chamamos esse conjunto de informações de *framedata*. Como está em um site, é possível acessar essas informações e, melhor ainda, é possível armazenar essas informações importantes em um banco de dados. Esse projeto faz exatamente isso e de maneira muito simples, utilizando o *Selenium* para fazer o *webscrapping* e o *PostgreSQL* para armazenar na *database*.

### Como rodar
- Crie um banco de dados com o nome compatível com o ```dbname``` da linha 7. O meu é "framedata" (não erre a sua senha também hehe).
- Comando para instalar as bibliotecas: 
```
pip install -r requirements.txt
```
- Simplesmente rode ``` python main.py ``` no terminal e não seja macetado nas filas ranqueadas de STREET FIGHTER 6.