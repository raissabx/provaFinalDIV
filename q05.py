from pymongo import MongoClient

def obter_colecao_mongodb(url_conexao, colecao):
    conn = MongoClient(url_conexao)
    col = conn[colecao]
    return col

if __name__ == '__main__':

    url_conexao = 'mongodb+srv://rai_xavier:201295@cluster0.x45vtu2.mongodb.net/test'
    colecao = 'produto'

    conexao = obter_colecao_mongodb(url_conexao, colecao)
    print(conexao)





