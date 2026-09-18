import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(("localhost", 5000))

servidor.listen(1)

print("Servidor aguardando conexão...")

conexao, endereço = servidor.accept()

print("Cliente conectado:", endereço)

mensagem = conexao.recv(1024).decode()

print("Mensagem recebida:", mensagem)

conexao.send("Olá! Mensagem recebida pelo servidor do aluno mais Lindo.".encode())

conexao.close()
servidor.close()
