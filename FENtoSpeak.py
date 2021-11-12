#import pyttsx3
import chess
from gtts import gTTS
from pydub import AudioSegment
import os

file = os.getcwd()
print(file)
path = file + '\\Audio Files\\'
fenSource = file + '\\FEN.txt'

readFen = open(fenSource)
fenList = readFen.readlines()
print(fenList)


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

fenNumber = 0

for fen in fenList:
    
    WhitePositions = whiteIntro + delay_half
    BlackPositions= blackIntro + delay_half

    #the FEN for our starting position.  This is a basic mate in 1
    board = chess.Board()
    board.set_fen(fen)

    #This loops across every square and if there is a piece, it determines the color, type and square.  It appends that information to different lists and is stored.  This is basically sorting the information so that it will be read off as 'all of white's pieces' and then 'all of blacks pieces'

    #This *used* to make lists.  Due to needed flexibility in delays in reading off piece positions, I had to break everything into it's own MP3 that will later be concatenated.  
    for i in chess.SQUARES:
        piece = board.piece_at(i)
        square = chess.square_name(i)
        
        if piece:    
            TypeofPiece = chess.piece_name(piece.piece_type)
            piece_color = piece.color
            
            if piece_color:
                tts = gTTS(str(TypeofPiece) + " on " + str(square), lang='en')
                mp3File = path + "White_" + str(TypeofPiece)+"_"+ str(square) + ".mp3"
                tts.save(mp3File)
                temp = AudioSegment.from_file(mp3File)
                WhitePositions = WhitePositions + temp + delay_half
                os.remove(mp3File)               
                            
            else:        
                tts = gTTS(str(TypeofPiece) + " on " + str(square), lang='en')
                mp3File = path + "Black_" + str(TypeofPiece)+"_"+ str(square) + ".mp3"
                tts.save(mp3File)
                temp = AudioSegment.from_file(mp3File)
                BlackPositions = BlackPositions + temp + delay_half
                os.remove(mp3File)
        else:
            None


    FinalPosition = WhitePositions + BlackPositions
    fenFileName = "Fen_"+ str(fenNumber) +".mp3"

    if os.path.exists(fenFileName):
        os.remove(fenFileName)
    else:
        print("No have, homie")
        
    print("*****Generating FEN mp3**************")

    FinalPosition.export(fenFileName, format="mp3")
    fenNumber = fenNumber + 1
        
        
        
"""
    #generating a list of files that are white or black positions
    print("Looking for position mp3 files...")
    for root, dirs, files in os.walk(path): 
        for file in files:
            if file.startswith("White_"):
            
                print("Found file " + file)
                temp = AudioSegment.from_file(path+file)
                print("Concatenating " + file)
                WhitePositions = WhitePositions + temp + delay_half
                os.remove(path+file)
                print("Removing " + file)
            elif file.startswith("Black_"):
            
                print("Found file " + file)
                temp = AudioSegment.from_file(path+file)
                print("Concatenating " + file)
                BlackPositions = BlackPositions + temp + delay_half
                os.remove(path+file)
                print("Removing " + file)
            else:
                print("Bro what is this " + str(file))"""

        