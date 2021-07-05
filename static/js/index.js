const $mapContainer = document.getElementById('map'); //지도 div element 취득

if (navigator.geolocation) {
  console.log('lalalalal');
  // GeoLocation가 활성화되어있는 경우 접속 위치 취득 및 콜백함수 호출
  navigator.geolocation.getCurrentPosition(function (position) {
    const lat = position.coords.latitude, // 위도 취득
      lon = position.coords.longitude; // 경도 취득
    console.log(lat, lon);

    const mapOption = {
      center: new kakao.maps.LatLng(lat, lon), // 지도의 중심좌표
      level: 3, // 지도의 확대 레벨
    };
    const map = new kakao.maps.Map($mapContainer, mapOption); // 지도 생성 및 할당

    // 마커 생성
    const markerPosition = new kakao.maps.LatLng(lat, lon); // geolocation으로 취득한 위치에 마커 생성

    const marker = new kakao.maps.Marker({
      map: map,
      draggable: true,
      clickable: true,
      position: markerPosition,
      image: new kakao.maps.MarkerImage(
        'https://img.icons8.com/ios-glyphs/60/000000/cat.png',
        new kakao.maps.Size(40, 40),
        { offset: new kakao.maps.Point(27, 40) }
      ),
    }); //마커 생성 및 할당

    // 인포윈도우 생성
    const infowindow = new kakao.maps.InfoWindow({
      content: `<div style="padding:5px;">
        <form action="/crud/add/" method="POST" enctype="multipart/form-data">
      <p>이름 : <input type="text" name="catname" placeholder="길냥이 이름"></p>
      <p>개냥이 지수 : <input type="text" name="friendly" placeholder="사람과의 친밀도 (%)"></p>
      <input type="file" name="img" multiple>
      <div>성별 : <select name="gender">
        <option value="male">수컷</option>
        <option value="female">암컷</option>
        <option value="dont_know">모름</option>
      </select></div>
      <div>색상 : <select name="color">
        <option value="yellow">노란색</option>
        <option value="yellow">검은색</option>
        <option value="yellow">흰색</option>
        <option value="yellow">주황색</option>
        <option value="yellow">회색</option>
      </select></div>
      <div>중성화 여부 : <select name="neutering">
        <option value="O">O</option>
        <option value="X">X</option>
        <option value="dont_know">모름</option>
      </select></div>
      <p>발견 위치 : <input type="text" name="location" placeholder="활동 위치"></p>
      <br>
      <button type="submit">작성하기</button>
    </form>
    </div>`,
      removable: true, //닫기 버튼 활성화
    });

    // 인포윈도우를 마커위에 표시
    infowindow.open(map, marker);

    // 클릭한 위치에 마커 생성
    kakao.maps.event.addListener(map, 'click', function (mouseEvent) {
      // 클릭한 위도, 경도 정보를 가져옵니다
      const latlng = mouseEvent.latLng;

      // 마커 위치를 클릭한 위치로 옮깁니다
      marker.setPosition(latlng);
      infowindow.open(map, marker);
      console.log(latlng.getLat(), latlng.getLng());
    });
  });
} else {
  console.log('lalala');
  const mapOption = {
    center: new kakao.maps.LatLng(37.547076399306, 127.04020267241), // 지도의 중심좌표
    level: 10, // 지도의 확대 레벨
  };
  const map = new kakao.maps.Map($mapContainer, mapOption); // 지도를 생성합니다

  const marker = new kakao.maps.Marker({
    map: map,
    draggable: true,
    clickable: true,
    position: new kakao.maps.LatLng(37.547076399306, 127.04020267241),
    image: new kakao.maps.MarkerImage(
      'https://img.icons8.com/ios-glyphs/60/000000/cat.png',
      new kakao.maps.Size(40, 40),
      { offset: new kakao.maps.Point(27, 40) }
    ),
  }); //마커 생성 및 할당

  // 인포윈도우 생성
  const infowindow = new kakao.maps.InfoWindow({
    content: '<div style="padding:5px;">고양이가 이곳에 있나요?</div>',
    removable: true, //닫기 버튼 활성화
  });

  // 인포윈도우를 마커위에 표시
  infowindow.open(map, marker);

  kakao.maps.event.addListener(map, 'click', function (mouseEvent) {
    // 클릭한 위도, 경도 정보를 가져옵니다
    const latlng = mouseEvent.latLng;

    // 마커 위치를 클릭한 위치로 옮깁니다
    marker.setPosition(latlng);
    infowindow.open(map, marker);
    console.log(latlng.getLat(), latlng.getLng());
  });
}
