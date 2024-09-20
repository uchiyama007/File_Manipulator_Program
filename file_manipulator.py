import sys
import os

def validate_args(args):
    if len(args) < 3:
        print("エラー: コマンドと必要な引数を指定してください。")
        sys.exit(1)

    command = args[1]
    
    if command == "reverse":
        if len(args) != 4:
            print("エラー: reverse コマンドは inputpath と outputpath を必要とします。")
            sys.exit(1)

    elif command == "copy":
        if len(args) != 4:
            print("エラー: copy コマンドは inputpath と outputpath を必要とします。")
            sys.exit(1)

    elif command == "duplicate-contents":
        if len(args) != 4 or not args[3].isdigit():
            print("エラー: duplicate-contents コマンドは inputpath と複製回数 (n) を必要とします。")
            sys.exit(1)

    elif command == "replace-string":
        if len(args) != 5:
            print("エラー: replace-string コマンドは inputpath, needle, newstring を必要とします。")
            sys.exit(1)

    else:
        print("エラー: 無効なコマンドです。")
        sys.exit(1)

def reverse_file(inputpath, outputpath):
    with open(inputpath, 'r') as infile:
        content = infile.read()
    with open(outputpath, 'w') as outfile:
        outfile.write(content[::-1])
    print(f"ファイルを逆にしました: {outputpath}")

def copy_file(inputpath, outputpath):
    with open(inputpath, 'r') as infile:
        content = infile.read()
    with open(outputpath, 'w') as outfile:
        outfile.write(content)
    print(f"ファイルをコピーしました: {outputpath}")

def duplicate_contents(inputpath, n):
    with open(inputpath, 'r') as infile:
        content = infile.read()
    with open(inputpath, 'a') as outfile:
        for _ in range(n):
            outfile.write(content)
    print(f"内容を {n} 回複製しました: {inputpath}")

def replace_string(inputpath, needle, newstring):
    with open(inputpath, 'r') as infile:
        content = infile.read()
    content = content.replace(needle, newstring)
    with open(inputpath, 'w') as outfile:
        outfile.write(content)
    print(f"'{needle}' を '{newstring}' に置き換えました: {inputpath}")

def main():
    validate_args(sys.argv)

    command = sys.argv[1]

    if command == "reverse":
        reverse_file(sys.argv[2], sys.argv[3])
    elif command == "copy":
        copy_file(sys.argv[2], sys.argv[3])
    elif command == "duplicate-contents":
        duplicate_contents(sys.argv[2], int(sys.argv[3]))
    elif command == "replace-string":
        replace_string(sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == "__main__":
    main()
