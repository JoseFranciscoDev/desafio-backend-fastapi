from api._database.models import Formulario, Pergunta, EnumTipoPergunta


def test_create_form():
    formulario = Formulario(titulo="Meu Form", descricao="Teste de criação", ordem=1)
    pergunta = Pergunta(
        formulario=formulario,
        titulo="Qual sua idade?",
        codigo="Q1",
        orientacao_resposta="Digite sua idade em anos",
        ordem=1,
        obrigatoria=True,
        sub_pergunta=False,
        tipo_pergunta=EnumTipoPergunta.INTEIRO,
    )
    assert formulario.titulo == "Meu Form"
    assert pergunta.titulo == "Qual sua idade?"
    assert pergunta.tipo_pergunta == EnumTipoPergunta.INTEIRO
    assert pergunta.formulario == formulario
