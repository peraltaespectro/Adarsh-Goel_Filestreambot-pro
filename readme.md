![GitHub contributors](https://img.shields.io/github/contributors/adarsh-goel/filestreambot-pro?style=flat&color=green)
![GitHub repo size](https://img.shields.io/github/repo-size/adarsh-goel/filestreambot-pro?color=green)
![GitHub](https://img.shields.io/github/license/adarsh-goel/filestreambot-pro?color=green)


<h1 align="center"></h1>
<p align="center"> 
  <img src="https://socialify.git.ci/adarsh-goel/filestreambot-pro/image?description=1&descriptionEditable=A%20very%20fast%20file%20streaming%20bot%20used%20for%20streaming%20and%20downloading%20movies&font=Source%20Code%20Pro&forks=1&issues=1&language=1&logo=https%3A%2F%2Fuser-images.githubusercontent.com%2F88939380%2F137127129-a86fc939-2931-4c66-b6f6-b57711a9eab7.png&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Dark" alt="Cover Image" width="650">
  </a>
  
 <p align="center">
    Um bot do Telegram para transformar todos os arquivos de mídia e documentos em download direto instantâneo e link de fluxo.
    <br />
   </strong></a>
    <br />
    <a href="https://github.com/adarsh-goel/pro/issues">Reportar um erro</a>
    |
    <a href="https://github.com/adarsh-goel/filestreambot-pro/issues">Request Feature</a>
  </p>


<hr>

## Por favor, me siga para saber sempre que eu lançar um novo projeto❤️‍🔥
### Caso você esteja tendo problemas para implantar o bot, você pode contratar um desenvolvedor, temos taxas razoáveis [Clique aqui](https://t.me/+KvjFjOWicuZmOTQx)

## 🍁 Sobre este bot :

![streamingfilestreambot-professional-live_1](https://user-images.githubusercontent.com/88939380/137127129-a86fc939-2931-4c66-b6f6-b57711a9eab7.png)

</p>
<p align='center'>
    Este bot fornecerá links de streaming para arquivos do Telegram sem a necessidade de esperar até que o download seja concluído
</p>


## ♢ Como fazer o seu :


#### ♢ Clique neste menu suspenso e obtenha mais detalhes
<br>
<details>
  <summary><b>Deploy no Heroku:</b></summary>


1. Clone este repositório
2. Clique no botão para implantar e siga os passos

<h4> Então siga os passos acima 👆 e, em seguida, implantar outro bot sábio não funcionará</h4>

Pressione o botão abaixo para implantar rapidamente no Heroku/Raiwlay
Você pode hospedar localmente ou implantar em [Heroku](https://heroku.com)
### 💜 Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy/)

<br>


então vá para o <a href="#mandatory-vars">guia de variáveis</a> para mais informações sobre como configurar variáveis ambientais. </details>

<details>
  <summary><b>Características:</b></summary>
  
<p>

🚀Características<p>
💥Super rápido⚡️ baixar e transmitir links.<br>
💥Nenhum anúncio nos links gerados.<br>
💥Interface super-rápida.<br>
💥Junto com os links, você também obtém informações do arquivo como nome, tamanho, etc..<br>
💥Suporte a um canal de atualizações.<br>
💥Suporte de banco de dados Mongodb para transmissão.<br>
💥Proteção com senha.<br>
💥Interface amigável.<br>
💥Verificação de ping.<br>
💥Verificação de DC do usuário.<br>
💥CPU em tempo real, RAM, uso da Internet. <br>
💥Suporte de domínio personalizado. <br>
💥Todo o código indesejado removido. <br>
💥Muito mais cansado de escrever check-out implantando-o. 
</details>
<details>
  <summary><b>Hospede-o no VPS localmente :</b></summary>


```py
git clone https://github.com/adarsh-goel/filestreambot-pro
cd filestreambot-pro
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 -m Adarsh
```

e para parar todo o bot,
 do <kbd>CTRL</kbd>+<kbd>C</kbd>

Configurando coisas

Se você estiver no Heroku, basta adicioná-los nas Variáveis Ambientais
ou se você estiver hospedando localmente, crie um arquivo chamado `config.env` no diretório raiz (root) e adicione todas as variáveis lá.
Um exemplo de `config.env` Arquivo:

```py
API_ID=12345
API_HASH=esx576f8738x883f3sfzx83
BOT_TOKEN=55838383:yourtbottokenhere
BIN_CHANNEL=-100
PORT=8080
FQDN=your_server_ip
OWNER_ID=your_user_id
DATABASE_URL=mongodb_uri
```
  </details>

<details>
  <summary><b>Variaveis e detalhes :</b></summary>
  
 Variaveis Obrigatótias

`API_ID` : Vamos para [my.telegram.org](https://my.telegram.org) para obter isso.

`API_HASH` : Vamos para [my.telegram.org](https://my.telegram.org) para obter isso.
  
`MY_PASS` : SENHA do bot

`BOT_TOKEN` : Obtenha o token do bot em [@BotFather](https://telegram.dog/BotFather)

`BIN_CHANNEL` : Crie um novo canal (privado/público), adicione [@missrose_bot](https://telegram.dog/MissRose_bot) como administrador do canal e digite /id. Agora copie e cole o ID neste campo.
  
`OWNER_USERNAME` : Vc deveria saber afinal é seu nome de usuário não lembra?  é só ir nas configurações!

`OWNER_ID` : Seu ID de usuário do Telegram

`DATABASE_URL` : URI do MongoDB para salvar IDs de usuário quando eles iniciam o bot pela primeira vez.  Usaremos isso para transmitir para eles. Vou tentar adicionar mais recursos relacionados ao banco de dados.  Se você precisar de ajuda para obter o URI, clique no logotipo abaixo!

[![mongo](https://telegra.ph/file/fd68906852c71fdd68bef.jpg)](https://www.youtube.com/watch?v=HhHzCfrqsoE)

 Variaveis Opcionais

`UPDATES_CHANNEL` : Coloque um nome de usuário de canal público, para que todos os usuários tenham que ingressar nesse canal para usar o bot.  Deve adicionar bot ao canal como Admin para funcionar corretamente.

`BANNED_CHANNELS` : Coloque IDs de Canais Banidos onde o bot não funcionará.  Você pode adicionar vários IDs e separar com <kbd>Space</kbd>.

`SLEEP_THRESHOLD` : Defina um limite de suspensão para exceções de espera de inundação que ocorrem globalmente nesta instância de bot de telegrama, abaixo do qual qualquer solicitação que gere uma espera de inundação será invocada automaticamente novamente após inatividade pelo período de tempo necessário.  Exceções de espera de inundação que exigem tempos de espera mais altos serão geradas.  O padrão é 60 segundos.

`WORKERS` : Número máximo de trabalhadores simultâneos para lidar com atualizações recebidas.  Padrões para `3`

`PORT` : A porta que você deseja que seu webapp seja ouvido.  Padrões para `8080`

`WEB_SERVER_BIND_ADDRESS` : Seu endereço de ligação do servidor.  Padrão para `0.0.0.0`

`NO_PORT` : Se você não quiser que sua porta seja exibida.  Você deve apontar seu `PORT` to `80` (http) or `443` (https) para que os links funcionem.  Ignore isso se você estiver no Heroku.

`FQDN` :  Um nome de domínio totalmente qualificado, se presente.  Padrões para `WEB_SERVER_BIND_ADDRESS` </details>

<details>
  <summary><b>Como usar :</b></summary>

:warning: **Antes de usar o bot, não se esqueça de adicionar o bot ao `BIN_CHANNEL` como administrador**
 
`/start` : Para verificar se o bot está vivo ou não.

Para obter um link de fluxo instantâneo, basta encaminhar qualquer mídia para o bot e boom, é rápido.
  
![image](https://user-images.githubusercontent.com/88939380/145798095-3cdad108-96b0-4391-a540-cad144d6b864.png)


### Canal de Suporte
Bot também suportado com canais.  Basta adicionar o canal do bot como administrador.  Se algum novo arquivo entrar no Canal, ele será editado com **Get Download Link** Botão. </details>

### Créditos : 

- [Eu](https://github.com/adarsh-goel)
- Todos nesta jornada !
