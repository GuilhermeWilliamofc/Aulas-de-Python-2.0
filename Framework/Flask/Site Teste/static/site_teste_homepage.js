var titulo = document.getElementById('titulo')
var imagem = document.getElementById('imagem')
var data_texto = document.getElementById('data')

var coletar_data = new Date()
var dia = coletar_data.getDate()
var mes = coletar_data.getMonth()
var ano = coletar_data.getFullYear()
var hora = coletar_data.getHours()
var minutos = coletar_data.getMinutes()

switch(mes){ // mudar o valor númerico da variavel mês para string
    case 0:
        mes = 'Janeiro'
        break

    case 1:
        mes = 'Fevereiro'
        break

    case 2:
        mes = 'Março'
        break

    case 3:
        mes = 'Abril'
        break

    case 4:
        mes = 'Maio'
        break

    case 5:
        mes = 'Junho'
        break

    case 6:
        mes = 'Julho'
        break

    case 7:
        mes = 'Agosto'
        break

    case 8:
        mes = 'Setembro'
        break

    case 9:
        mes = 'Outubro'
        break

    case 10:
        mes = 'Novembro'
        break

    case 11:
        mes = 'Dezembro'
        break
}


titulo.style.transitionDuration = '2s'
titulo.style.color = 'rgb(54, 130, 136)'

document.body.style.transitionDuration = "2s"
document.body.style.backgroundColor = 'rgb(168, 186, 226)'

data_texto.innerHTML = `Hoje é Dia ${dia} de ${mes} de ${ano}<br>Agora são ${hora}h e ${minutos}min...`
