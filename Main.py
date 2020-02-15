try:
    import traceback
    import ExtractDataMaker
    import PronunciationMaker
    import YmmpMaker
    import AdjustYmmp

    while True:
        print(
            '##########################################################################################################################')
        print('1:Scenarioフォルダ内にある。「.txt」ファイル全てを処理対象とし、ExtractDataフォルダにセリフを抽出したファイルを生成します。')
        print(
            '2:ExtractDataフォルダ内にある、_extract.csvという文字を含んだファイルを対象にYMMを用いて発音を付与した後、PronunciationDataフォルダに発音を付与したファイルを生成します。')
        print('3:PronunciationDataフォルダ内にある、_pronunciation.csvという文字を含んだファイルを対象に、Ymmpフォルダにゆっくりムービメーカーで読み込み可能なファイルを生成します。')
        print('4:Ymmpフォルダ内のファイルを対象に、CompleteYmmpフォルダにアイテムの長さを修正したymmpファイルを生成します。')
        number = input('メインメニューです。番号を入力すると該当の処理が作動します。\n')

        if number == '1':
            try:
                ExtractDataMaker.do()

                print('----------------------------------')
                print('処理が完了しました。')
                print('----------------------------------')
            except:
                traceback.print_exc()
                print('エラーが発生しました。サポートを希望する場合は上記のエラーメッセージを開発者に提供してください。')

        elif number == '2':
            try:
                PronunciationMaker.do()
                print('----------------------------------')
                print('処理が完了しました。')
                print('----------------------------------')
            except:
                traceback.print_exc()
                print('エラーが発生しました。サポートを希望する場合は上記のエラーメッセージを開発者に提供してください。')

        elif number == '3':
            try:
                YmmpMaker.do()
                print('----------------------------------')
                print('処理が完了しました。')
                print('----------------------------------')
            except:
                traceback.print_exc()
                print('エラーが発生しました。サポートを希望する場合は上記のエラーメッセージを開発者に提供してください。')

        elif number == '4':
            try:
                AdjustYmmp.do()
                print('----------------------------------')
                print('処理が完了しました。')
                print('----------------------------------')
            except:
                traceback.print_exc()
                print('エラーが発生しました。サポートを希望する場合は上記のエラーメッセージを開発者に提供してください。')
except:
    traceback.print_exc()
    print('エラーが発生しました。サポートを希望する場合は上記のエラーメッセージを開発者に提供してください。')
    input('エンターキーで終了します。')
