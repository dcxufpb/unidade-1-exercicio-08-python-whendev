# coding: utf-8

class Loja:
  
  def __init__(self, nome_loja, logradouro, numero, complemento, bairro, 
               municipio, estado, cep, telefone, observacao, cnpj,
               inscricao_estadual):
    self.nome_loja = nome_loja
    self.logradouro = logradouro
    self.numero = numero
    self.complemento = complemento
    self.bairro = bairro
    self.municipio = municipio
    self.estado = estado
    self.cep = cep
    self.telefone = telefone
    self.observacao = observacao
    self.cnpj = cnpj
    self.inscricao_estadual = inscricao_estadual


def dados_loja_objeto(loja):
    # Implemente aqui
    if (loja.nome_loja == "" or loja.nome_loja == None):
        raise Exception("O campo nome da loja é obrigatório")
    if (loja.logradouro == "" or loja.logradouro == None):
        raise Exception("O campo logradouro do endereço é obrigatório")
    if (loja.numero == 0):
        loja.numero = "s/n"
    if (loja.municipio == "" or loja.municipio == None):
        raise Exception("O campo município do endereço é obrigatório")
    if (loja.estado == "" or loja.estado == None):
        raise Exception("O campo estado do endereço é obrigatório")
    if (loja.cnpj == "" or loja.cnpj == None):
        raise Exception("O campo CNPJ da loja é obrigatório")
    if (loja.inscricao_estadual == "" or loja.inscricao_estadual == None):
        raise Exception("O campo inscrição estadual da loja é obrigatório")
        
    _COMPLEMENTO = ""
    if (loja.complemento != "" and loja.complemento != None):
        _COMPLEMENTO = " " + loja.complemento


    _BAIRRO = ""
    if (loja.bairro != "" and loja.bairro != None) :
        _BAIRRO = loja.bairro + " - "


    _CEP = ""
    _TELEFONE = ""

    if (loja.cep != "" and loja.cep != None) :
        _CEP = "CEP:" + loja.cep
        if (loja.telefone != "" and loja.telefone != None):
            _TELEFONE = " Tel " + loja.telefone
    else :
        _CEP = ""
        if (loja.telefone != "" and loja.telefone != None):
            _TELEFONE = "Tel " + loja.telefone

    _OBSERVACAO = ""

    if(loja.observacao != "" and loja.observacao != None):
        _OBSERVACAO = loja.observacao


    _NUMERO = ""
    if (loja.numero != 0):
        _NUMERO = loja.numero


    if (loja.numero == 0 or loja.numero == None or loja.numero == ""):
        _NUMERO = "s/n"



    show = f'''{loja.nome_loja}
{loja.logradouro}, {_NUMERO}{_COMPLEMENTO}
{_BAIRRO}{loja.municipio} - {loja.estado}
{_CEP}{_TELEFONE}
{_OBSERVACAO}
CNPJ: {loja.cnpj}
IE: {loja.inscricao_estadual}'''
    return show
