import pyttsx3
import chess

engine = pyttsx3.init()

testfen = 'rnbqkb1r/pppppppp/5n2/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 1 2'
board = chess.Board()

for i in chess.SQUARES:
    piece = board.piece_at(i)
    if piece:
        
        TypeofPiece = chess.piece_name(piece.piece_type)
        piece_color = piece.color
        
        square = chess.square_name(i)
               
        if piece_color is True:
            piece_color = "White"
        else: 
            piece_color = "Black"
            
        print('\n')
        print(TypeofPiece)  
        print(square)
        print(piece_color)
        
    #    if symbol = 'R':
    #       symbol = 'Rook'
    #    elif symbol = 
            
    else:
            None
#piece_color = str(piece_color)
#pyttsx3.speak(TypeofPiece + piece_color)
#print(symbol)