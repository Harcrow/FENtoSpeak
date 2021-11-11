import pyttsx3
import chess

engine = pyttsx3.init()

testfen = '1k6/8/1K6/8/4Q3/8/8/8 w - - 0 1'
board = chess.Board()
board.set_fen(testfen)


speak_rate = 175
engine.setProperty('rate', speak_rate)


white_pieces= []
white_squares = []
black_pieces = []
black_squares = []

for i in chess.SQUARES:
    piece = board.piece_at(i)
    square = chess.square_name(i)
    
    if piece:    
        TypeofPiece = chess.piece_name(piece.piece_type)
        piece_color = piece.color
        
        if piece_color is True:
            piece_color = "White"
            white_pieces.append(TypeofPiece)
            white_squares.append(square)
            engine.say(white_pieces[0])
            engine.say(white_squares[0])
            
        else:        
            piece_color = "Black"
            black_pieces.append(TypeofPiece)
            black_pieces.append(square)
            
    else:
        None

i=1  
#pyttsx3.speak("White's Position")
#for i in white_pieces:
#engine.say(white_pieces[i])
#engine.say(white_squares[i])
engine.runAndWait()
engine.stop()
print(white_pieces[i])
print(white_squares[i])
    
    
# piece_color = str(piece_color)
# pyttsx3.speak(TypeofPiece)

