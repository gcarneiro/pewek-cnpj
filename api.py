from json import dumps

from flask import Flask, request
from flask_jsonpify import jsonify
from flask_restful import Api, Resource
from sqlalchemy import create_engine
import mysql.connector
import json

f = open("config.json", "r")
cnf = json.load(f)
print(cnf['host'])

app = Flask(__name__)
api = Api(app)

class CNPJ_unico(Resource):
	
	def get(self, cnpj):
		try:
			cnx = mysql.connector.connect(
				host=cnf['host'],
				port=cnf['port'],
				user=cnf['user'],
				password=cnf['password'],
				database=cnf['database']
			)

			cursor = cnx.cursor()
			cursor.execute("SELECT id_empresa, subsidiaria, codigo_verificador, cnpj, matriz_filial as identificador_matriz_filial, fantasia as nome_fantasia, situacao_cadastral as situacao_cadastral, data_situacao_cadastral as data_situacao_cadastral, motivo_situacao_cadastral as motivo_situacao_cadastral, data_abertura as data_inicio_atividade, cnae_principal as cnae_fiscal, endereco_tipo_logradouro as descricao_tipo_logradouro, endereco_logradouro as logradouro, endereco_numero as numero, endereco_complemento as complemento, endereco_bairro as bairro, endereco_cep as cep, endereco_uf as uf, endereco_codigo_municipio as codigo_municipio, telefone1_ddd as ddd_telefone_1, telefone1_numero, telefone2_ddd as ddd_telefone_2, telefone2_numero, fax_ddd as ddd_fax, fax_numero, email as correio_eletronico, email, id, razao_social as razao_social, codigo_natureza_juridica, qualificacao_responsavel as qualificacao_do_responsavel, capital_social, porte as porte, codigo, nome as municipio FROM cnpj.estabelecimento JOIN empresa ON empresa.id=estabelecimento.id_empresa JOIN municipio ON municipio.codigo=estabelecimento.endereco_codigo_municipio WHERE cnpj = '"+cnpj+"'")
			
			row_headers=[x[0] for x in cursor.description] #this will extract row headers
			row = cursor.fetchone()
			cursor.close()

			empresa=[]
			empresa.append(dict(zip(row_headers, row)))

			cursor = cnx.cursor()
			cursor.execute("SELECT * FROM socio WHERE id_empresa = '"+empresa[0]['id_empresa']+"'")
			row_headers=[x[0] for x in cursor.description] #this will extract row headers
			rows = cursor.fetchall()
			cursor.close()

			socio=[]
			socio.append(dict(zip(row_headers, row)))
			socio = [dict(zip(tuple (row_headers) ,i)) for i in rows]
			empresa[0]['socio'] = socio

			cnx.close()
			return jsonify(empresa)
		except:
			return jsonify({'status': 'false', 'message': 'CNPJ nao encontrado na base de dados'})

api.add_resource(CNPJ_unico, '/cnpj/<cnpj>')

#Estas portas / host podem ser sobreescritos ao rodar em CMD
if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5002')
