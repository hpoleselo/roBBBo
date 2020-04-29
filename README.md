<h1 align="center">
  <br>
  <a href="#"><img src="https://pbs.twimg.com/profile_banners/1254066650573410305/1587846642/1500x500" alt="roBBBo" width=600></a>
  <br>
  roBBBo
  <br>
</h1>

<h4 align="center">Bot do Twitter para você virar um BBBer </h4>

<p align="center">
  <a href="https://twitter.com/robbbo20" target="_blank"><img src="https://badgen.net/badge/icon/roBBBo20/blue?icon=twitter&label" alt="Casa do bot"></a>
  <a href="https://github.com/hpoleselo/roBBBo/commits/master" target="_blank">
    <img src="https://badgen.net/github/commits/hpoleselo/roBBBo">
  </a>
  <a href="https://github.com/hpoleselo/roBBBo/graphs/contributors" target="_blank">
    <img src="https://badgen.net/github/contributors/hpoleselo/roBBBo">
  </a>
  <a href="#">
    <img src="https://badgen.net/github/license/hpoleselo/roBBBo">
  </a>
  <img src="https://badgen.net/github/last-commit/hpoleselo/roBBBo">
</p> 

<p align="center"> 
  <img src="https://user-images.githubusercontent.com/24254286/80611432-fa335780-8a10-11ea-9f8f-6b5da93dbb47.gif">
</p>

<p align="center">
  <a href="#project">Projeto</a> •
  <a href="#installation">Instalação | Uso</a> •
  <a href="#authors">Autores</a> •
  <a href="#license">Licença</a> •
  <a href="#credits">Créditos</a>
</p> 

## <a name="project"></a> roBBBo
Programa desenvolvido em Python usando a biblioteca ``` OpenCV ``` e seus classificadores já treinados ``` haarcascade ``` para o reconhecimento das faces nas imagens dadas pelos usuários. Para a obtenção das imagens e uma interação mais interessante, decidimos por usar a API do Twitter ``` tweepy ```, onde o usuário realiza uma postagem com a hashtag do seu participante desejado ``` #robbbobabu ```, ``` #robbbomanu ```, ``` #robbbothelma ``` ou ``` #robbborafa ``` (os atuais finalistas do programa).

## <a name="installation"></a> Instalação | Uso
Caso deseje reproduzir este algorítmo na sua maquina, o uso do ``` Python3 ``` é necessário assim como o ``` pip ``` para instalar algumas bibliotecas, para instalar as dependências do projeto, rode o seguinte comando na pasta do projeto:

``` $ pip3 install -r requirements.txt```

Para usar a API do Twitter você necessitará exportar as credenciais toda vez em um terminal novo que for rodar o programa, por isso, crie um ``` alias ``` para seu ``` .bashrc ```:

``` $ cd ~/ ```

``` $ echo "alias twitter-export='export export API_KEY=SUA_API_KEY ; export API_SECRET_KEY=SUA_API_SECRET_KEY; export ACCESS_TOKEN=SEU_ACCESS_TOKEN ; export ACCESS_TOKEN_SECRET=SEU_ACCESS_TOKEN_SECRET ;'" >> .bashrc ```

Colocando os respectivos valores fornecidos pelo Twitter para ``` SUA_API_KEY ```, ``` SUA_API_SECRET_KEY ```, ``` SEU_ACCESS_TOKEN ``` e ``` SEU_ACCESS_TOKEN_SECRET ```.

Depois é só dar o comando para exportar as chaves da API:

``` $ twitter-export ```

Após exportar as chaves, podemos rodar o programa para escutar as hashtags e realizar a detecção:

``` $ python3 subscriber_bot.py ```

## <a name="authors"></a> Autores

* **Daniel Mascarenhas** - [ielson](https://github.com/ielson)
* **Henrique Poleselo** - [hpoleselo](https://github.com/hpoleselo)


## <a name="license"></a> Licença

Distributed under the BSD 3-Clause License. See `LICENSE` for more information.

<!-- Usando anchor pra poder referenciar este header no menu acima -->
<!-- Para referencia-lo, fazemos: Me leve para [Créditos](#credits) -->
## <a name="credits"></a> Créditos
* [remove.bg](https://www.remove.bg/) - Para deixar o fundo transparente em .png
* [Ezgif](https://ezgif.com/) - Para gerar os gifs usados nesta página
* [Técnica do overlay das imagens](https://gist.github.com/clungzta/b4bbb3e2aa0490b0cfcbc042184b0b4e)
* GIMP - Para o corte de imagens e deixar apenas a face