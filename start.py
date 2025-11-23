import argparse, sys, os, pathlib

def argv_parser():
    parser = argparse.ArgumentParser(description="Choose a method to run the program.")
    parser.add_argument('--type', type=str, default='system', help='Type of run method to use. Options: system (default), startfile')
    parser.add_argument('--path', type=str, required=True, help='Program/Shortcut path to execute.')
    return parser.parse_args()

def is_excutable(file_path):
    pathext_str = os.environ.get('PATHEXT', '.EXE;.BAT;.CMD;.COM')
    valid_extensions = {ext.upper() for ext in pathext_str.split(';')}
    _, ext = os.path.splitext(file_path)
    return ext.upper() in valid_extensions

def is_excutable_strict(file_path): # I didn't check if this method works or not. So if error occurs, fix it yourself.
    try:
        with open(file_path, 'rb') as f:
            header = f.read(2)
            return header == b'MZ'
    except:
        return False

def use_system(path):
    os.system(path)

def use_startfile(path):
    os.startfile(path)

def main():
    args = argv_parser()
    
    if args.type == 'system' or args.type == 'force':
        if pathlib.Path(args.path).exists():
            if pathlib.Path(args.path).is_file():
                if is_excutable(args.path):
                    if args.type == 'force' and not is_excutable_strict(args.path):
                        print(f"[Error] File '{args.path}' didn't pass strict executable check. To run it, use 'system' method instead.")
                        sys.exit(1)
                    use_system(args.path)
                    sys.exit(0)
                else:
                    print(f"[Error] File '{args.path}' is not an executable file. Please check the file and try again.")
                    sys.exit(1)
            else:
                print(f"[Error] Path '{args.path}' is not a file. Please check the path and try again.")
                sys.exit(1)
        else:
            print(f"[Error] Path '{args.path}' does not exist. Please check the path and try again.")
            sys.exit(1)

    elif args.type == 'startfile':
        try:
            use_startfile(args.path)
            sys.exit(0)
        except Exception as e:
            print(f"[Error] Failed to start file: {e}. Please check the path and try again.")
            sys.exit(1)

    else:
        print(f"[Error] Unknown type '{args.type}'. Use 'system' or 'startfile'.")
        sys.exit(1)

if __name__ == "__main__":
    main()