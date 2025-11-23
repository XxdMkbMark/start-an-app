import argparse, sys, os, pathlib, magic

def argv_parser():
    parser = argparse.ArgumentParser(description="Choose a method to run the program.")
    parser.add_argument('--type', type=str, default='system', help='Type of run method to use. Options: system (default), startfile')
    parser.add_argument('--path', type=str, required=True, help='Program/Shortcut path to execute.')
    return parser.parse_args()

def is_excutable(file_path):
    mime = magic.Magic(mime=True)
    file_mime = mime.from_file(file_path)
    if file_mime in ['application/x-msdownload', 'application/x-executable', 'application/x-mach-binary']:
        return True
    else:
        return False

def use_system(path):
    os.system(path)

def use_startfile(path):
    os.startfile(path)

def main():
    args = argv_parser()
    
    if args.type == 'system':
        if pathlib.Path(args.path).exists():
            if pathlib.Path(args.path).is_file():
                if is_excutable(args.path):
                    use_system(args.path)
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
        except Exception as e:
            print(f"[Error] Failed to start file: {e}. Please check the path and try again.")
            sys.exit(1)

    else:
        print(f"[Error] Unknown type '{args.type}'. Use 'system' or 'startfile'.")
        sys.exit(1)

if __name__ == "__main__":
    main()