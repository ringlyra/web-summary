<!-- metadata -->

- **title**: Ryzen AI MAX+395（Windows）でWan2.1を動かす
- **source**: https://zenn.dev/robustonian/articles/wan2_1_ryzen_ai
- **author**: 金のニワトリ
- **published**: 2025-06-03T14:32:54+00:00
- **fetched**: 2025-06-04T13:04:15Z
- **tags**: codex
- **image**: https://res.cloudinary.com/zenn/image/upload/s--gUwuc_TI--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Ryzen%2520AI%2520MAX%252B395%25EF%25BC%2588Windows%25EF%25BC%2589%25E3%2581%25A7Wan2.1%25E3%2582%2592%25E5%258B%2595%25E3%2581%258B%25E3%2581%2599%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:%25E9%2587%2591%25E3%2581%25AE%25E3%2583%258B%25E3%2583%25AF%25E3%2583%2588%25E3%2583%25AA%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3plbm4tdXNlci11cGxvYWQvYXZhdGFyLzQ1NmVjZjczNWIuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png

## 要約

Ryzen AI MAX+395 を搭載した Windows 環境で動画生成モデル Wan2.1 を動かす手順をまとめた記事。PyTorch や依存パッケージの導入から ani_Wan2_1 を利用した実行方法、CausVid LoRA による約 9 倍の高速化と生成速度の計測結果、今後の課題などを解説する。AMD GPU ユーザー向けに注意点や tips も紹介。

## 本文 / Article

# はじめに

## 2025/6/4追記内容

- Ryzen AI MAX+395（gfx1151）以外の**AMD GPU向けの説明を追記**
- CausVid LoRAにより**約9倍の高速化**（約83分→約9分）に成功したことを追記
- **workflowのjsonファイルを追記**
- グラフの表示が崩れていたのを修正

## どんな人向けの記事？

- 生成 AI に興味のある方
- AMD Ryzen AI Max+ 395で動画生成をしたい方・高速化したい方
- AMD Ryzen AI Max+ 395の動画生成速度に興味がある方

環境

```
Windows＠EVO-X2（AMD Ryzen AI Max+ 395、128GB）

```

### 背景

- Ryzen AI MAX+395（gfx1151）でUbuntu用のPytorchのビルドを試みたが断念した
- Windowsならgfx1151に対応したPytorchが使えるものの、MIOpenまわりのエラーで動画生成に失敗していた

そんなとき、A-UtaさんがEVO-X2でWan2.1の動画生成に成功したというポストを発見した。

<https://x.com/UtaAoya/status/1929148813240918023>

早速A-Utaさんに教えていただいた方法を試したところ、私のWindows環境でも動画生成に成功！

<https://x.com/gosrum/status/1929384258390442059>

ということで、今回の記事では下記について備忘録的にまとめる。

- Ryzen AI MAX+395（gfx1151）でWan2.1の動画を生成する手順
- 852話さんのani_Wan2_1で動画を生成する方法
- **CausVid LoRA**で動画生成を**高速化**する方法（**83分→9分に約9倍の高速化**）
- **生成速度**まとめ

## Ryzen AI MAX+395（gfx1151）でWan2.1の動画を生成する手順

gitとAMD GPU Driverは導入済みという前提で話を進める。  
<https://gitforwindows.org/>  
<https://www.amd.com/ja/support/download/drivers.html>

途中までは以下の手順通りにPowershellでコマンドを打つだけでよい。

```
PS > powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

```

```
PS > git clone https://github.com/comfyanonymous/ComfyUI.git
PS > cd ComfyUI
PS > uv python pin 3.12
PS > uv init
PS > Start-BitsTransfer -Source https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch/torch-2.7.0a0+git3f903c3-cp312-cp312-win_amd64.whl
PS > Start-BitsTransfer -Source https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch/torchaudio-2.6.0a0+1a8f621-cp312-cp312-win_amd64.whl
PS > Start-BitsTransfer -Source https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch/torchvision-0.22.0+9eb57cd-cp312-cp312-win_amd64.whl
PS > uv add .\torch-2.7.0a0+git3f903c3-cp312-cp312-win_amd64.whl .\torchaudio-2.6.0a0+1a8f621-cp312-cp312-win_amd64.whl .\torchvision-0.22.0+9eb57cd-cp312-cp312-win_amd64.whl
PS > uv add -r .\requirements.txt
PS > uv add numpy<2

```

<https://github.com/scottt/rocm-TheRock/releases/tag/v6.5.0rc-pytorch>

!

上記の.whlファイルでも、`7900(XT), 7800(XT), 7600(XT), Phoenix, 9070(XT) aka Navi48, and the Strix Halo aka 8060s`なら問題なく動くかもしれない。もし失敗した場合は、下記の.whlファイルを使えば上記のGPUでも全く同じ手順でおそらく動くはず。

```
PS > Start-BitsTransfer -Source https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch-gfx110x/torch-2.7.0a0+git3f903c3-cp312-cp312-win_amd64.whl
PS > Start-BitsTransfer -Source https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch-gfx110x/torchaudio-2.6.0a0+1a8f621-cp312-cp312-win_amd64.whl
PS > Start-BitsTransfer -Source https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch-gfx110x/torchvision-0.22.0+9eb57cd-cp312-cp312-win_amd64.whl
PS > uv add .\torch-2.7.0a0+git3f903c3-cp312-cp312-win_amd64.whl  .\torchaudio-2.6.0a0+1a8f621-cp312-cp312-win_amd64.whl  .\torchvision-0.22.0+9eb57cd-cp312-cp312-win_amd64.whl

```

それ以外のGPUの場合は、公式の[pytorch](https://pytorch.org/)がWindows+ROCmに対応してなさそうなので、[TheRock](https://github.com/ROCm/TheRock)のソースコードを自分でビルドしかなさそう？

## Wan2.1で動画生成

A-Utaさんに教えていただいたコマンドオプションをつけてComfyUIを起動する。

<https://x.com/UtaAoya/status/1929291297711440249>

```
PS > uv run .\main.py --use-pytorch-cross-attention --force-fp16 --cpu-vae

```

```
PS > uv run .\main.py --use-pytorch-cross-attention --force-fp16 --cpu-vae
Checkpoint files will always be loaded safely.
Total VRAM 89977 MB, total RAM 65175 MB
pytorch version: 2.7.0a0+git3f903c3
AMD arch: gfx1151
ROCm version: (6, 5)
Set vram state to: NORMAL_VRAM
Device: cuda:0 AMD Radeon(TM) 8060S Graphics : native
Using pytorch attention
Python version: 3.12.10 (main, May 22 2025, 02:00:39) [MSC v.1943 64 bit (AMD64)]
ComfyUI version: 0.3.39
****** User settings have been changed to be stored on the server instead of browser storage. ******
****** For multi-user setups add the --multi-user CLI argument to enable multiple user profiles. ******
ComfyUI frontend version: 1.21.6
[Prompt Server] web root: C:\Users\gosrum\Documents\AI\test\ComfyUI\.venv\Lib\site-packages\comfyui_frontend_package\static

Import times for custom nodes:
   0.0 seconds: C:\Users\gosrum\Documents\AI\test\ComfyUI\custom_nodes\websocket_image_save.py

Starting server

To see the GUI go to: http://127.0.0.1:8188

```

無事起動出来たら上記のような表示が出るので、webブラウザで<http://127.0.0.1:8188>にアクセスするとComfyUIが起動できる。

![](https://storage.googleapis.com/zenn-user-upload/87b84ec66d38-20250603.png)

`ワークフロー→テンプレートを参照→ビデオ→Wan 2.1 テキストからビデオへ`を選択すると、モデルがないといわれるので、すべてダウンロードしてから然るべきディレクトリに入れる。

![](https://storage.googleapis.com/zenn-user-upload/2989913a9cd2-20250603.png)

- `ComfyUI\models\vae\wan_2.1_vae.safetensors`
- `ComfyUI\models\text_encoders\umt5_xxl_fp8_e4m3fn_scaled.safetensors`
- `ComfyUI\models\unet\wan2.1_t2v_1.3B_fp16.safetensors`

ファイルの格納が終わったら、ワークフロー下部の`実行する`ボタンを押すことで動画を生成できる。

## ani_Wan2_1を試す

852話さんのani_Wan2_1を試す。

<https://note.com/852wa/n/nba242ef7ef4c>

civitaiでani_Wan2_1_14B_fp8_e4m3fnか1.3Bのt2vモデルをダウンロードし、`ComfyUI\models\unet\`に格納する。

ComfyUIをリロードし、ワークフロー上の`拡散モデルを読み込む`のunet_nameを上記に変更し、プロンプトに`anime style`を追加することで、アニメスタイルの動画を生成できる。

生成時間は1.3Bならモデル差し替え前と同じ10分。14Bは83分程度かかったが、クオリティは明らかに高くなっている。次節では高速化を試みる。

<https://x.com/gosrum/status/1929451150002028948>

## CausVid LoRAを試す

私は、動画生成に関しては完全にド素人であり、動画生成にはこんな時間かかるのか。。。と思っていたのだが、下記のポストによると動画生成を高速化する手段がいくつかあるらしい。

<https://x.com/umiyuki_ai/status/1929460745651020113>  
<https://x.com/8co28/status/1929421784035831840>

どちらにも共通しているのは**CausVid LoRA**で、step数を減らすことで劇的に高速化できるという夢のようなLoRAらしい。

他の手法については追々挑戦するとして、まずは大きな効果を期待できそうな**CausVid LoRA**を早速導入してみる。

まずはLoRAモデルをダウンロードする。とりあえずHuggingfaceから下記の二つのモデルを入手し、`ComfyUI\models\loras`に格納する。

<https://huggingface.co/Kijai/WanVideo_comfy/tree/main>

- `Wan21_CausVid_14B_T2V_lora_rank32.safetensors`
- `Wan21_CausVid_bidirect2_T2V_1_3B_lora_rank32.safetensors`

次にどうやってLoRAを適用するかだが、私はComfyUIでLoRAを適用したことがないのでこのAIエージェント時代にも関わらずweb上でワークフローを探すことにした。

そのまま使えるものは見つからなかったので、どうすれば使えるかを確認したところ、どうもこんな感じでLoRAを読み込めば使えるらしい。

- 変更前  
  ![](https://storage.googleapis.com/zenn-user-upload/81d232967852-20250603.png)
- 変更後  
  ![](https://storage.googleapis.com/zenn-user-upload/5ffd7ef16953-20250603.png)

あとはワークフロー中のパラメータを下記のように変更した。

結論として、**83分→9分に約9倍の高速化**に成功した。品質は多少落ちているように感じるが、同じ時間で9倍試行できるのはかなり大きい。

参考になるかわからないが、一応ワークフローもgithubに公開した。

<https://github.com/robustonian/public_zenn_file/blob/main/ComfyUI/workflow/text_to_video_wan_ani14B_Causvid.json>

## 生成時間まとめ

### VAEをCPUで処理させたことの影響

最初に述べたように、現状Ryzen AI MAX+ 395では動画生成時にVAEをGPUで処理させようとするとエラーが出るため、CPUで処理させている。

CPUで処理するということは生成時間が遅くなるわけだが、その影響がどの程度あるかをFLUX.1の画像生成で検証する。※FLUX.1はGPUでも処理できる

結果は以下の通り（計測したデータをClaude Sonnet 4で可視化したもの）。

![](https://storage.googleapis.com/zenn-user-upload/3a0d70ef3002-20250603.png)

![](https://storage.googleapis.com/zenn-user-upload/9a1b33dd04c0-20250603.png)

上記からわかることとしては、GPUで処理しても**単純に何倍速くなるとはいえず、schnellでもdevでもほとんど同じだけ短くなる**ことぐらい？

とはいえ、GPUで処理することで速くなるであろうことは間違いないので、このあたりの問題も解決する正式なサポートを期待する。できればUbuntuでも使えるようにして欲しい。

### フレーム数依存性

うみゆきさんのポストに長尺動画もいけるのでは？というコメントがあったので、1秒単位で生成時間を計測し可視化してみた。結果はこちら。

![](https://storage.googleapis.com/zenn-user-upload/67d58fad0836-20250604.png)  
![](https://storage.googleapis.com/zenn-user-upload/772e0952aed4-20250604.png)  
![](https://storage.googleapis.com/zenn-user-upload/774ef30f372c-20250604.png)

ここからわかることは下記の通り。

- 支配的なのはKサンプラーの部分で、frame数に対して非線形的に生成時間が増大する。
- 対してVAEの時間は線形的に生成時間が増大する。

上記から、VAEの処理時間は支配的でなく、残念ながらGPUによる高速化もそこまで期待できなさそうであることがわかる。

また、VRAMの容量よりもframe数の増加による非線形的な計算時間の増加が問題になりそうだと分かった。というわけで、慣れるまではデフォルトの33frames（2秒）で運用することにする。

データの詳細はこちら。

![](https://storage.googleapis.com/zenn-user-upload/089982bc79c0-20250603.png)  
![](https://storage.googleapis.com/zenn-user-upload/0a8d325b540d-20250603.png)

# まとめ

今回の記事では、下記についてまとめました。

- Ryzen AI MAX+395（gfx1151）でWan2.1の動画を生成する手順
- 852話さんのani_Wan2_1で動画を生成する方法
- **CausVid LoRA**で動画生成を**高速化**する方法
- **生成速度**まとめ

いよいよRyzen AI MAX+395で動画生成ができるようになりました。

t2vについては色々と検証ができたので、次はi2vにも挑戦したいと思います。

最後まで読んでいただきありがとうございました。次回もぜひよろしくお願いします。

## Wanvideo入門記事（追記）

852話さんが**wanvideoに関するよもやま　導入・小ネタ**に関するnote記事を公開されていました。

動画生成は始めたばかりなので、とても参考になります。ありがとうございます！

<https://note.com/852wa/n/n1ae23891b874?sub_rt=share_pb>
