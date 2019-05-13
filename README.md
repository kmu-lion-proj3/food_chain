<h1>먹이사슬 게임</h1>
<h2>부제 : 먹사 in 멋사</h2>
<b>해당 게임은 더 지니어스 게임 룰브레이커 시즌2 1화의 먹이사슬 게임을 기반으로 제작했습니다.</b>
<h2>참여자</h2>
<ul>
    <li>강승원</li>
    <li>김현주</li>
    <li>이정우</li>
    <li>이철희</li>
    <li>조영완</li>
</ul>
<h2>게임 설명</h2>
<p>
    게임의 자세한 링크는 <a
        href="https://namu.wiki/w/%EB%8D%94%20%EC%A7%80%EB%8B%88%EC%96%B4%EC%8A%A4:%EB%A3%B0%20%EB%B8%8C%EB%A0%88%EC%9D%B4%EC%BB%A4/1%ED%99%94">여기</a>를
    클릭하세요.
    <br>
    
</p>
<h2>detail</h2>
<p>
    django를 사용해서 만들었으며, 13인의 계정정보가 있어야 합니다.
    13인보다 적거나 많으면 정상작동하지 않습니다.
    <br>
    동물 정보는 다음 명령어를 통해 db에 저장할 수 있습니다.
</p>
<pre><code>
python manage.py loaddata game/fixtures/data.json
</code></pre>
<p>
    data.json파일 안에 13마리의 동물의 정보를 넣어두었습니다.
    <br>
    role함수는 임의로 지정한 계정에 대해서 게임 시작이 가능합니다.
    아직은 다소 불안정하기에 사용하려면 말을 잘듣고 순서를 잘 지켜야합니다.
    더욱 안정적인 게임의 플레이를 위해선 더 많은 개선이 필요합니다.
</p>