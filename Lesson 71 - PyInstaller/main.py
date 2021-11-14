from gooey import Gooey, GooeyParser
from pydub.playback import play
from pydub import AudioSegment

@Gooey(program_name="Music Player")
def parse_args():
    parser = GooeyParser(description="Play Music")
    parser.add_argument("song",widget="FileChooser",help="Song to play",gooey_options={"wildcard":"MP3 Files |*.mp3","default_dir":"./"})
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    song = args.song
    song = AudioSegment.from_mp3(song)
    play(song)