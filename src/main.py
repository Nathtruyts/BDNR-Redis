import controladores.cupomControlador as cupomControlador

###Cupons###
cupomControlador.inserir('cupom1', '[{"nome": "Heat25", "Valor": "R$25.00"}]')
cupomControlador.acharCupom('cupom1')
cupomControlador.deletarCupom('cupom1')

