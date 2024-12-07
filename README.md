# 📂 linecode_checker

## 📋 概要

**linecode_checker**は、指定されたディレクトリ内のテキストファイル（`.txt`）をスキャンし、各ファイルの改行コードを検出する Python スクリプトです。  
改行コード（LF、CR、CRLF）が混在している場合、その情報を適切に表示します。

---

## 🚀 主な機能

1. **改行コードの検出**

   - LF（Unix/Linux, `\n`）
   - CR（Mac OS, `\r`）
   - CRLF（Windows, `\r\n`）

2. **改行コードの種類を要約**

   - ファイルに含まれる改行コードの種類を集計し、混在の有無を検出します。

3. **ディレクトリ全体のスキャン**

   - 指定されたディレクトリ内のすべてのテキストファイルを再帰的に探索し、改行コードを調べます。

4. **コンソール出力**
   - ファイルパス、ファイル名、改行コード情報を出力します。

---

## 🛠️ 使用方法

### 必要な環境

- Python 3.x

### 実行手順

1. **スクリプトのダウンロード**  
   このリポジトリをクローンまたはファイルをダウンロードします。

   ```bash
   git clone https://github.com/your-repo/line-ending-detector.git
   cd line-ending-detector
   ```

2. **スクリプトの実行**

   ```bash
   python line_ending_detector.py
   ```

3. **ディレクトリパスの入力**
   実行後、検査対象となるディレクトリのパスを入力します。

   ```
   検査するディレクトリのパスを入力: C:\example\directory
   ```

4. **結果の確認**
   各ファイルのパス、名前、および改行コード情報がコンソールに表示されます。

---

## 📂 サンプル出力

### コンソール出力

```
ファイルパス, ファイル名, 改行コード
C:\example\directory\file1.txt, file1.txt, LF
C:\example\directory\file2.txt, file2.txt, CRLF
C:\example\directory\file3.txt, file3.txt, 混在
```

---

## 📄 コード解説

### 主な関数

1. **`detect_line_ending(file_path)`**

   - ファイル内の改行コードを検出し、種類ごとにカウントします。
   - 対応する改行コード:
     - LF: Unix/Linux
     - CR: Mac OS
     - CRLF: Windows

2. **`summarize_line_endings(line_endings)`**

   - 検出された改行コードを要約し、混在しているか単一かを判断します。

3. **`check_files_in_directory(directory_path)`**

   - 指定されたディレクトリ内のすべてのテキストファイルを探索し、各ファイルの改行コードを調べます。

4. **`main()`**
   - スクリプトのエントリーポイント。ユーザーからディレクトリパスを入力させ、改行コードを検出します。

---

## ⚠️ 注意事項

1. **対象ファイル**
   - `.txt`拡張子のファイルのみが対象です。
2. **権限エラー**
   - アクセス権のないファイルやディレクトリにアクセスするとエラーが発生する可能性があります。
