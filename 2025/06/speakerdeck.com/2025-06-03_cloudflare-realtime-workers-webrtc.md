<!-- metadata -->

- **title**: Cloudflare Realtime と Workers でつくるサーバーレス WebRTC
- **source**: https://speakerdeck.com/nekoya3/cloudflare-realtime-to-workers-detukurusabaresu-webrtc
- **author**: Taiyu Yoshizawa
- **published**: 2025-06-03T00:00:00Z
- **fetched**: 2025-06-04T13:28:25Z
- **tags**: codex, webrtc, cloudflare
- **image**: https://files.speakerdeck.com/presentations/e9be246f239c4fdda3ef712ca808212a/slide_0.jpg?35329792

## 要約

Cloudflare Workers と Cloudflare Realtime を用いたサーバーレス **WebRTC** の実装方法を解説するスライド。 **STUN**, **TURN**, **SFU** などの基本概念を説明し、Realtime Kit や Workers KV を活用したサンプルコードを示す。 さらに Serverless SFU の特徴と利点、OBS 配信への応用、今後の展望について触れている。

## 本文

Cloudflare Workers + Realtime

ɴᴇᴋᴏʏᴀsᴀɴ

Who are you?

ɴᴇᴋᴏʏᴀsᴀ

Software Engineer @MIERUNE Inc

Co-founder & Software Engineer @ ReMotiv

GitHub: @NEKOYASA

Web: nekoyasan.me

What is MIERUNE

位置情報技術に特化したプロフェッショナル集

9年前に北海道のOSSコミュニティ (FOSS4G) から創業し

て、現在も本社は札幌市、社員数38

OSSを中心に柔軟な技術選定を実

Hono / Svelte / Maplibre / QGIS などな

HP: https://www.mierune.co.jp/

れきちず：https://rekichizu.jp/

れきちず | MapLibre | 地理院タイル | 『日本歴史地名大系』地名項目データセット

おことわり

今回は Cloudflare Realtime について様々な用語の説明をし

ながらお話しま

用語の中には仕様上はかなり複雑なものもあり、とっつきやす

いように端折っている箇所も多くありま

私自身も専門家というわけではない一利用者に過ぎないため、

誤った箇所などあればお教えください

Cloudflare Realtime とは

Cloudflare Realtime とは

Cloudflare が提供する WebRTC に関連するサービスの総

以前は Cloudflare Calls という名称でサービス提供がされて

いたが、2025年4月に名称変

名称変更と同タイミングで正式リリース & Realtime Kit の

Private Beta が開始

Cloudflare Realtime とは

Cloudflare が提供する WebRTC に関連するサービスの総

以前は Cloudflare Calls という名称でサービス提供がされて

いたが、2025年4月に名称変

名称変更と同タイミングで正式リリース & Realtime Kit の

Private Beta が開始

WebRTCとは

Web RealTime Communication → Web RT

双方向リアルタイム通信を実現するためのAPIやプロトコルのこ

とを指す

RFC8825 ~ 8839 あたりを中心に定義されているが、関連す

る仕様なども合わせると非常に多岐にわた

現在ではブラウザに標準機能として基本的には搭載されており、

双方向リアルタイム通信の手法としては比較的利用しやすい

WebRTCとは

Discord や Google Meet 、 Twitter Spaces など、音声通

話やビデオ通話等に多く利用されている

最近では WHIP や WHEP という規格によってOBSなどソフ

トウェアを使った配信にも活用できるような基盤が整い始めてい

WebRTCの詳しいことは専門の会社さんが記事などでまとめて

くれているのでそちらへ...

WebRTCとは

STU

TUR

SFU

STUNとは

Session Traversal Utilities for NATs = STU

NAT環境下に自身が居る場合にデバイスはプライベートIPしか

わからず、そのままでは自身のグローバルIPがわからない

→ STUNに問い合わせることで知ることができる

STUNとは

私は...どこのだれ...?

クライアント

N
A
T

...

STUNとは

私は...どこのだれ...?

Binding Request

N
A
T

クライアント

STUN サーバー

Binding Response

あなたはこのIP / Port

TURNとは

Traversal Using Relays around NAT = TUR

P2P による直接通信が出来ない（STUNだけではP2Pでの接続

が確立できない）or UDPによる接続が確立できない場合に利用

する中継サーバ・プロトコルのこ

サーバを経由するがただのバイパスしか役目がなく、バイパスし

ているデータを読み取ることも、変化させることもな

サーバを経由するため、P2Pに比べて遅延は大きくなってしまう

TURNとは

クライアント

クライアント

TURNとは

クライアント

TURN

サーバー

クライアント

SFUとは

Selective Forwarding Unit = SF

P2P による通信ではメッシュ接続をする必要があるため参加者

が増えるにつれて、1人が接続する接続数が増大する問題があ

SFUサーバとの接続のみを行い、SFUサーバーが必要に応じて

他のクライアントに転送す

転送しか出来ず加工をすることは出来な

対照的に合成・再エンコードを行うMCUも存在する

SFUとは

やばい

SFUとは

SFU

サーバー

WebRTCとは

STU

TUR

SFU

Cloudflare Realtime では

Realtime Ki

TURN Serve

Serverless SFU

Cloudflare Realtime では

Realtime Ki

TURN Serve

Serverless SF

(STUN Server)

Cloudflare Realtime では

Realtime Ki

TURN Serve

Serverless SF

で提供はされている
Realtime Ki

TURN Serve
Serverless SF

(STUN Server) 

で提供はされている
Realtime Ki

TURN Serve

Serverless SF
(STUN Server) 

で提供はされている

TURN サーバーの Cloudflare フルマネージドなも

TURN Key IDと Token から TURN Username と

GraphQL の Analytics API が用意されていて、どれだけ利用

EdgeからのEgress のみが課金対

0.05 USD / GB で 初回1000GBまでは無

カスタムドメインを割り当てることも出来る
Serverless SFU

SFU の Cloudflare フルマネージドなも

PeerConnection で Session を作り、MediaStreamTrack
ルームという概念はなく、トラックそれぞれに一意のIDが付いて

取得していなければ課金もされないので、メディアストリームを

まだPrivate Betaで全容がよくわからないものの..

クライアントのSDK・UIが用意されていた

RecordingやAnalytics、Workers AI との連

Realtime AIと称して Transcription や Agent、Voice AI、

ベース技術としてはServerless SFU / TURN Serverなのは変

Serverless SFU

20constnewconstawaitconstreturn peerConnection RTCPeerConnection({
iceServers [
{
urls ,
},
],
bundlePolicy ,

localStream navigator.mediaDevices.({
video ,
audio ,

transceivers localStream.().((track) {
peerConnection.(track, {
direction ,
});
response (
,
{
method ,
headers {
,
Authorization ${appSecret},
},
body .({
sessionDescription {
type ,
sdp peerConnection.localDescription.sdp,
},
}),
},

newSessionResult response.();setLocalDescriptioncreateOfferfetchstringifyjson=::::::::="https://rtc.live.cloudflare.com/v1/apps/${appId}/sessions/new""POST""application/json"`Bearer `"offer""Content-Type"JSON1

15trackObjects transceivers.((transceiver) {
{
location ,
mid transceiver.mid ,
trackName transceiver.sender.track.id,
};
peerConnection.( peerConnection.());
newLocalTrackResult app.(
trackObjects,
peerConnection.localDescription.sdp,
); peerConnection.(
RTCSessionDescription(newLocalTrackResult.sessionDescription),
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
(newRemoteTracksResult.sessionDescription.type) {
.(${sessionId});
peerConnection.(
RTCSessionDescription(newRemoteTracksResult.sessionDescription),
);
peerConnection.(
peerConnection.(),
);
app.(peerConnection.localDescription.sdp);
;
Error();
}
18constnewletifconstawaitconstnewreturn remoteTrackPromise ((resolve) {
tracks [];
response (
,
{
method ,
headers {
,
Authorization ${appSecret},
},
body .({
sessionDescription {
type ,
sdp peerConnection.localDescription.sdp,
},
}),
},
newSessionResult response.();setLocalDescriptioncreateOfferfetchstringifyjson=::::::::="https://rtc.live.cloudflare.com/v1/apps/${appId}/sessions/new""POST""application/json"`Bearer `"offer""Content-Type"JSON1
15trackObjects transceivers.((transceiver) {
{
location ,
mid transceiver.mid ,
trackName transceiver.sender.track.id,
};
peerConnection.( peerConnection.());
newLocalTrackResult app.(
trackObjects,
peerConnection.localDescription.sdp,
); peerConnection.(
RTCSessionDescription(newLocalTrackResult.sessionDescription),
(newRemoteTracksResult.sessionDescription.type) {
.(${sessionId});
peerConnection.(
RTCSessionDescription(newRemoteTracksResult.sessionDescription),
);
15trackObjects transceivers.((transceiver) {
{
location ,
mid transceiver.mid ,
trackName transceiver.sender.track.id,
};
peerConnection.( peerConnection.());
newLocalTrackResult app.(
trackObjects,
peerConnection.localDescription.sdp,
); peerConnection.(
RTCSessionDescription(newLocalTrackResult.sessionDescription),
(newRemoteTracksResult.sessionDescription.type) {
.(${sessionId});
peerConnection.(
RTCSessionDescription(newRemoteTracksResult.sessionDescription),
);
peerConnection.(
peerConnection.(),
);
app.(peerConnection.localDescription.sdp);
;
Error();
}
18constnewletifconstawaitconstnewreturn remoteTrackPromise ((resolve) {
tracks [];
peerConnection. (event) {
tracks.(event.track);
.(${event.track.id}${event.track.mid});
(tracks.length ) {
(tracks);
(newRemoteTracksResult.sessionDescription.type) {
.(${sessionId});
peerConnection.(
RTCSessionDescription(newRemoteTracksResult.sessionDescription),
);
peerConnection.(
app.(peerConnection.localDescription.sdp);
;
Error();
}
}
18constnewletifconstawaitconstnewreturn remoteTrackPromise ((resolve) {
tracks [];
peerConnection. (event) {
tracks.(event.track);
.(${event.track.id}${event.track.mid});
(tracks.length ) {
(tracks);
}
};
remoteTracks remoteTrackPromise;
remoteStream MediaStream();
remoteTracks.((track) {
remoteStream.(track);
remoteStream;
現状だとまだある程度 WebRTC の初期知識が必要で、すぐに
ある意味無限スケーリングするSFU・TURN Serverというもの
DataChannelとかも使える & WHIPの参考実装などもあ
Realtime Kitたのしみ！
Cloudflare Realtime
Realtime Kitたのしみ！
Cloudflare Realtime
       app.(peerConnection.localDescription.sdp);
      ;
             Error();
  }
}

"offer"`Renegotiating for session `"answer""An offer SDP was expected":
console:
logsetRemoteDescriptionsetLocalDescriptioncreateAnswersendAnswerSDP1
2
3
4
5

6
7
8
9
10
11
12
13
14
15
16
17
18constnewletifconstawaitconstnewreturn remoteTrackPromise   ((resolve)  {
   tracks  [];
  peerConnection.  (event)  {
    tracks.(event.track);
    .(${event.track.id}${event.track.mid});
     (tracks.length  ) {
      (tracks);
    }
  };
});

 remoteTracks   remoteTrackPromise;
 remoteStream   MediaStream();
remoteTracks.((track)  {
  remoteStream.(track);
});
 remoteStream;
=Promise=>===>console>====>ontrackpushdebugresolveforEachaddTrack`Got track mid= `2まとめ

 現状だとまだある程度 WebRTC の初期知識が必要で、すぐに

簡単に使える！というものではな

 ある意味無限スケーリングするSFU・TURN Serverというもの

がほぼ初めて存在しているので、何か面白いことが出来そうなも

のではあ

 DataChannelとかも使える & WHIPの参考実装などもあ

 Realtime Kitたのしみ！

Cloudflare Realtime 

ぜひ遊んでみてね！

