import pyttsx3
import chess
from gtts import gTTS
from pydub import AudioSegment


test = "regular text speed no pause regular text speed comma pause, regular text speed period pause. regular text speed exclamation pause! regular text speed ellipses pause... regular text speed new line pause \n regular text speed "

board_string = " "
    

#initialize the test to speak engine. 
#engine = pyttsx3.init()

#the FEN for our starting position.  This is a basic mate in 1
testfen = '1k6/8/1K6/8/4Q3/8/8/8 w - - 0 1'
board = chess.Board()
board.set_fen(testfen)

#Not using the default voice.  this voice is a little easier to understand
#Zira = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

#adjusting the speak rate to a little slower than default.
# speak_rate = 175
# engine.setProperty('rate', speak_rate)
# engine.setProperty('voice', Zira)

tts_white = gTTS(text="...White's Position...", lang='en')
tts_white.save("whitePrompt.mp3")

tts_black = gTTS(text="...Black's Position...", lang='en')
tts_black.save("blackPrompt.mp3")

whiteIntro = AudioSegment.from_file(r"whitePrompt.mp3")
blackIntro = AudioSegment.from_file(r"blackPrompt.mp3")

delay_one = AudioSegment.from_file(r"silence1.mp3")
delay_five = AudioSegment.from_file(r"silence5.mp3")
delay_two = delay_one + delay_one
delay_half = delay_one[-500:]

WhiteHeader = whiteIntro + delay_two
BlackHeader = blackIntro + delay_two 

#setting up lists.
"""white_pieces= []
white_squares = []

black_pieces = []
black_squares = []
"""

white_position = []
black_position = []

white_string = " "
black_string = " " 

#This loops across every square and if there is a piece, it determines the color, type and square.  It appends that information to different lists and is stored.  This is basically sorting the information so that it will be read off as 'all of white's pieces' and then 'all of blacks pieces'
for i in chess.SQUARES:
    piece = board.piece_at(i)
    square = chess.square_name(i)
    
    if piece:    
        TypeofPiece = chess.piece_name(piece.piece_type)
        piece_color = piece.color
        
        if piece_color is True:
            piece_color = "White"
            #white_position.append(TypeofPiece)
            #white_position.append(" on ")
            #white_position.append(square)
            tts = gTTS(str(TypeofPiece) + " on " + str(square), lang='en')
            tts.save("White" + str(TypeofPiece)+"_"+ str(square) + ".mp3")
                        
        else:        
            piece_color = "Black"  
            #black_position.append(TypeofPiece)
            #black_position.append(" on ")
            #black_position.append(square)
            tts = gTTS(str(TypeofPiece) + " on " + str(square), lang='en')
            tts.save("Black" + str(TypeofPiece)+"_"+ str(square) + ".mp3")
    else:
        None
        
        
#pyttsx3.speak("Whites Position")
#board_position.append("White's Position. ...")



"""for i in range(len(white_pieces)):
   # engine.say(white_pieces[i] +" on "+ white_squares[i])
   # engine.runAndWait()
   # engine.stop()
    print(white_pieces[i])
    print(white_squares[i])
    print('\n')
    white_position.append(white_pieces[i] +" on "+ white_squares[i])
   # board_position.append(white_pieces[i] +" on "+ white_squares[i])
    
#pyttsx3.speak("Blacks Position")
#board_position.append("Black's Position.")
for i in range(len(black_pieces)):
    #print(i)
    #engine.say(black_pieces[i] +" on "+ black_squares[i])
    #engine.runAndWait()
    #engine.stop()
    print(black_pieces[i])
    print(black_squares[i])
    print('\n')
    black_position.append(black_pieces[i] +" on "+ black_squares[i])
    """


# for x in white_position:
    # white_string = white_string + x + " "



# for x in black_position:
    # black_string = black_string + x + " "

# #intro_plus_five.export("WIntro+Delay.mp3", format="mp3")

# tts_black = gTTS(text=black_string, lang='en')
# tts_black.save("Black_position.mp3")

#WhiteSpokenPosition = AudioSegment.from_file(r"White_position.mp3")
#BlackSpokenPosition = AudioSegment.from_file(r"Black_position.mp3")

#FinalPosition = WhiteHeader + WhiteSpokenPosition + BlackHeader + BlackSpokenPosition

#FinalPosition.export("Final.mp3", format="mp3")

# piece_color = str(piece_color)
# pyttsx3.speak(TypeofPiece)

