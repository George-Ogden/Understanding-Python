from gooey import Gooey, GooeyParser

def encode(text, key=255):
    new_text = ""
    for i in range(len(text)):
        new_text += chr(255 & (key ^ ord(text[i])))
    return new_text

@Gooey(program_name="File Encryption",navigation="TABBED")
def parse_args():
    parser = GooeyParser(description="Encrypt and decrypt files")
    subparsers = parser.add_subparsers(required=True)
    encoder = subparsers.add_parser("encode",help="Encode a text file into an unreadable format")
    decoder = subparsers.add_parser("decode",help="Decode an unreadable format into a text file")

    encoder.add_argument("input",widget="FileChooser",help="File to encode")
    decoder.add_argument("input",widget="FileChooser",help="File to decode")

    encoder.add_argument("output",widget="FileSaver",help="Output file location")
    decoder.add_argument("output",widget="FileSaver",help="Output file location")

    encoder.add_argument("--key",default=85,widget="IntegerField",help="Key to encrypt the file")
    decoder.add_argument("--key",default=85,widget="IntegerField",help="Key to decrypt the file")

    return parser.parse_args()

args = parse_args()
with open(args.output,"w") as output, open(args.input,"r") as input:
    output.write(encode(input.read(),int(args.key)))