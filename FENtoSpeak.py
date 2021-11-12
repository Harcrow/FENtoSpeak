#import pyttsx3
import chess
from gtts import gTTS
from pydub import AudioSegment
import os

path = 'C:\\Users\\tjowaisas\\Documents\\Hobby\\Chess\\FEN to speak\\Audio Files\\'
fenSource = 'C:\\Users\\tjowaisas\\Documents\\Hobby\\Chess\\FEN to speak\\FEN.txt'

readFen = open(fenSource)
fenList = readFen.readlines()
print(fenList)
#initialize the test to speak engine. 
#engine = pyttsx3.init()


#the FEN for our starting position.  This is a basic mate in 1
board = chess.Board()
board.set_fen(testfen)

#Not using the default voice.  this voice is a little easier to understand
#Zira = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

#adjusting the speak rate to a little slower than default.
# speak_rate = 175
# engine.setProperty('rate', speak_rate)
# engine.setProperty('voice', Zira)

#Generating the side announcements
tts_white = gTTS(text="...White's Position...", lang='en')
tts_white.save(path+"whitePrompt.mp3")

tts_black = gTTS(text="...Black's Position...", lang='en')
tts_black.save(path+"blackPrompt.mp3")

#reading the annoucements into memory
whiteIntro = AudioSegment.from_file(path+"whitePrompt.mp3")
blackIntro = AudioSegment.from_file(path+"blackPrompt.mp3")

#generating some delays for a little configurability.  500mS and 2S delays
delay_one = AudioSegment.from_file(path+"silence1.mp3")
delay_five = AudioSegment.from_file(path+"silence5.mp3")
delay_two = delay_one + delay_one
delay_half = delay_one[-500:]

#side annoucement + 2 seconds
WhitePositions = whiteIntro + delay_one
BlackPositions= blackIntro + delay_one

#setting up lists.
"""white_pieces= []
white_squares = []

black_pieces = []
black_squares = []
"""

#white_position = []
#black_position = []

#white_string = " "
#black_string = " " 

#This loops across every square and if there is a piece, it determines the color, type and square.  It appends that information to different lists and is stored.  This is basically sorting the information so that it will be read off as 'all of white's pieces' and then 'all of blacks pieces'

#This *used* to make lists.  Due to needed flexibility in delays in reading off piece positions, I had to break everything into it's own MP3 that will later be concatenated.  
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
            tts.save(path + "White_" + str(TypeofPiece)+"_"+ str(square) + ".mp3")
                        
        else:        
            piece_color = "Black"  
            #black_position.append(TypeofPiece)
            #black_position.append(" on ")
            #black_position.append(square)
            tts = gTTS(str(TypeofPiece) + " on " + str(square), lang='en')
            tts.save(path + "Black_" + str(TypeofPiece)+"_"+ str(square) + ".mp3")
    else:
        None

#generating a list of files that are white or black positions
print("Looking for position mp3 files...")
for root, dirs, files in os.walk(path): 
    for file in files:
        if file.startswith("White_"):
        
            print("Found file " + file)
            temp = AudioSegment.from_file(path+file)
            WhitePositions = WhitePositions + temp + delay_half
            
        elif file.startswith("Black_"):
        
            print("Found file " + file)
            temp = AudioSegment.from_file(path+file)
            BlackPositions = BlackPositions + temp + delay_half
            
        else:
            print("Bro what is this " + str(file))

FinalPosition = WhitePositions + BlackPositions

FinalPosition.export("Final_Fen.mp3", format="mp3")

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

