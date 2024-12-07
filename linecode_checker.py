import os

def detect_line_ending(file_path):
    # LF: Unix/Linux (\n)
    # CR: Mac OS (\r)
    # CRLF: Windows (\r\n)
    line_endings = {
        'LF': 0,
        'CR': 0,
        'CRLF': 0
    }

    try:
        with open(file_path, 'rb') as file:
            for line in file:
                if line.endswith(b'\r\n'):  # CRLF
                    line_endings['CRLF'] += 1
                elif line.endswith(b'\r'):   # CR
                    line_endings['CR'] += 1
                elif line.endswith(b'\n'):   # LF
                    line_endings['LF'] += 1
    except FileNotFoundError as fnfe:
        print(f"ファイルが見つかりません: {file_path}")
        print(f"エラー詳細: {fnfe}")
        return None
    except OSError as ioe:
        print(f"ファイルが開けません: {file_path}")
        print(f"エラー詳細: {ioe}")
        return None

    return line_endings

def summarize_line_endings(line_endings):
    try:
        types = [key for key, count in line_endings.items() if count > 0]
        if len(types) > 1:
            # 改行コードが混在されている
            return "混在"
        return types[0] if types else ""
    except OSError as ioe:
        print(f"エラー詳細: {ioe}")
        return ""

def check_files_in_directory(directory_path):
    print("ファイルパス, ファイル名, 改行コード")
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                line_endings = detect_line_ending(file_path)
                if line_endings is not None:
                    summary = summarize_line_endings(line_endings)
                    print(f"{file_path}, {file}, {summary}")

def main():
    directory_path = input("検査するディレクトリのパスを入力: ")
    check_files_in_directory(directory_path)
    print("処理終了")

if __name__ == "__main__":
    main()
