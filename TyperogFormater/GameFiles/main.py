import socket
import ball_game

s = socket.socket()
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(1)     # 1 kan forbinde ad gangen.

print('Waiting for client to connect...')
c, c_addr = s.accept()
print(c_addr, ' has connected!')

game = ball_game.BallGame()
game.start()

while True:
    game.submit_answer(c.recv(1024).decode())


